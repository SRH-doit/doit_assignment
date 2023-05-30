set_velx(1000), set_accx(2000), set_velj([150, 150, 180, 225, 225, 225]), set_accj([300, 300, 360, 450, 450, 450])
set_tool('tool'), set_tcp('tcp')
set_motion_end(DR_CHECK_OFF)

task_point_pareta = posx(-187.47, 281.32, 45.25, 0.71, -180, -89.29)
task_point_paretb = posx(342.62, 317.22, 15.87, 113.66, 179.78, 113.12)
task_point_paretc1 = posx(-1.72, 559.9, 49.3, 90.22, -179.99, 0.22)
task_point_paretc2 = posx(9.49, 559.94, 34.66, 179.99, 133.57, 89.99)
task_point_paretc3 = posx(9.5, 560.03, 18.21, 0.09, 136.43, -89.94)
task_point_paretc4 = posx(34.81, 560.02, 16.87, 15.65, 179.72, -74.36)

drl_report_line(OFF)

tp, tools, ml, mj, mjx, w = tp_log, set_tool_digital_outputs, movel, movej, movejx, wait

from queue import PriorityQueue as pqueue
from collections import deque
from itertools import product
    
def move(task_point, y=0, x=0, z=0, lz=0, gr=0, val=0, n=0, l=0) :
    max_r = lambda r : r if r < 10 else 9
    task_point_now = get_current_posx()[0]
    task_point_next = trans(task_point, [-40 * x, 40 * y, z, 0, 0, 0])
    r = [get_distance(task_point_now, task_point_next) / 15 if get_distance(task_point_now, task_point_next) > 2 else 0, (z / 2 - 0.5) if z > 2 else 0, (lz / 2 - 0.5) if lz > 2 else 0]
    mjx(task_point_next, sol=2, r=max_r(r[0])) if r[0] and not l else(ml(task_point_next, r=max_r(r[0])) if l else ...)
    ml([0, 0, -z, 0, 0, 0], mod=1, r=max_r(r[1]) if gr else 2) if r[1] else ...
    (tools([1, -2]), w(0.13)) if gr else tools([-1, 2])
    ml([0, 0, lz, 0, 0, 0], mod=1, r=max_r(r[2]) if gr else 2) if r[2] else ...
    plc("DW{}".format(val), str(n)) if val else ...
        
def movels(task_point, r, route, n=5) :
    global pareta_tmp
    move(task_point, r[0] // n, r[0] % n, 50, 15, 1, 100 + r[0], 0)
    line_move(task_point, route[1: ])
    move(task_point, r[1] // n, r[1] % n, 15, 50, 0, 100 + r[1], pareta_tmp[r[0]])
    pareta_tmp[r[1]], pareta_tmp[r[0]] = pareta_tmp[r[0]], 0

def hwacksan(paret, start, end, r_check=1, m=5, n=5, re_paret=0) :
    if re_paret : paret = [0 if x != 9 else 9 for x in paret]
    dq, paret[start], paret[end] = deque([end]), 0, -1
    while dq :
        node = dq.popleft()
        for c1, c2 in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            if 0 <= node // n + c1 < m and 0 <= node % n + c2 < n and not paret[node + c1 * n + c2] :
                paret[node + c1 * n + c2] = paret[node] - 1
                dq.append(node + c1 * n + c2)
                if node + c1 * n + c2 == start :
                    dq.clear()
                    break
    if not paret[start] : return 0
    if not r_check : return 1
    move_route, node = [start], start
    for plus, (c1, c2) in product(range(paret[node] + 1, 0), ((-1, 0), (1, 0), (0, -1), (0, 1))) :
        if paret[node] == plus : continue
        if 0 <= node // n + c1 < m and 0 <= node % n + c2 < n and paret[node + c1 * n + c2] == plus :
            node += c1 * n + c2
            move_route.append(node)
    return move_route

def paret_sort(paret_a, move_route, check_len, m=5, n=5) :
    h = lambda paret, route, _len : sum(list(map(lambda r: 5 if paret[r] and paret[r] != 10 else 0, route[_len: ])))
    pos_list = [pos for pos in range(m * n) if 0 < paret_a[pos] < 9]
    pq, paret_ex = pqueue(), {tuple(paret_a): h(paret_a, move_route, check_len)}
    pq.put([h(paret_a, move_route, check_len), 0, tuple(paret_a), pos_list, ()])
    while not pq.empty() :
        node = pq.get()
        paret_tmp = list(node[2])
        for P, Zp in product(node[3], [pos for pos in range(m * n) if not node[2][pos]]) :
            if not hwacksan(paret_tmp[:], P, Zp, False) : continue
            paret_tmp[Zp], paret_tmp[P] = paret_tmp[P], paret_tmp[Zp]
            weight = node[1] + 1 + h(paret_tmp, move_route, check_len)
            tuple_PR = tuple(paret_tmp)
            if not (tuple_PR in paret_ex) or paret_ex[tuple_PR] > weight :
                paret_ex[tuple_PR] = weight
                pos_list_tmp = node[3][:]
                pos_list_tmp.remove(P)
                pos_list_tmp.append(Zp)
                if weight == node[1] + 1 : return paret_tmp, node[4] + tuple([(P, Zp)])
                pq.put([weight, node[1] + 1, tuple_PR, pos_list_tmp, node[4] + tuple([(P, Zp)])])
            paret_tmp[Zp], paret_tmp[P] = paret_tmp[P], paret_tmp[Zp]

def thread_a(m=5, n=5):
    global paret_a, move_route_a
    end_route_check = lambda paret, move_route, check_len=1: all(not paret[r] for r in move_route[check_len:])
    check_point = {3: big_pack_pos, 2: middle_pack_pos, 1: small_pack_pos}
    a_count = 0
    for _ in range(3, 0, -1):
        while 1 :
            num_pos = [pos for pos in range(m * n) if paret_a[pos] == _]
            if not num_pos: break
            pos = None
            for p in num_pos:
                if paret_a[check_point[_]] and check_point[_] != p: continue
                if hwacksan(paret_a[:], p, check_point[_], False):
                    pos = p
                    move_route_a[a_count][1] = hwacksan(paret_a[:], pos, check_point[_])
                    paret_a[pos] = 0
                    break
            if pos is None:
                pos = num_pos[0]
                route = hwacksan(paret_a[:], pos, check_point[_], re_paret=True)
                paret_a[pos] = 9
                paret_a, move_route_a[a_count][0] = paret_sort(paret_a[:], route, 1)
                move_route_a[a_count][1] = route[:]
                paret_a[pos] = 0
            if not end_route_check(paret_a, end_route, 0):
                paret_a[check_point[_]] = 10
                paret_a, move_route_a[a_count][2] = paret_sort(paret_a[:], end_route, 0)
                paret_a[check_point[_]] = 0
            a_count += 1
            
plc("DW900", '5')
mj([90, 0, 90, 0, 90, 0], r=20), tools([-1, 2]), mjx(trans(task_point_pareta, [0, 0, 50, 0, 0, 0]), sol=2, r=10)
line_move = lambda task_point, move_route, n=5: [mjx(trans(task_point, [r % n * -40, r // n * 40, 15, 0, 0, 0]), sol=2, r=19.5) for r in move_route]
movea = lambda task_point, move_route: [movels(task_point, r, hwacksan(pareta_tmp[:], r[0], r[1])) for r in move_route]
paret_a = [plc("DW" + str(100 + i)) for i in range(25)]

for i in range(25) :
    num = plc("DW" + str(200 + i))
    if num == 5 : big_pack_pos = i
    elif num == 4 : middle_pack_pos = i
    elif num == 3 : small_pack_pos = i
    elif num == 2 : end_pos = i
    elif num == 1 : start_pos = i
    
move_route_a = [[[] for i in range(3)] for j in range(9)]
end_route = hwacksan(paret_a[:], start_pos, end_pos, re_paret=1)
    
for pos in [_pos for _pos in range(25) if paret_a[_pos] == 5] :
    mjx(trans(task_point_pareta, [pos % 5 * -40, pos // 5 * 40, 50, 0, 0, 0]), sol=2, r=10)
    count = 3 
    for z in [25, 15] :
        ml([0, 0, -z, 0, 0, 0], mod=1, r=2)
        tools([1, -2]), w(0.2)
        if not get_tool_digital_input(1) : break
        count -= 1
        tools([-1, 2]), w(0.1)
    tools([-1, 2]), w(0.1)
    plc("DW{}".format(100 + pos), str(count))
    paret_a[pos] = count
    ml([0, 0, 40, 0, 0, 0], mod=1, r=5)
    
pareta_tmp = paret_a[:]
thread_a()
count = 0
loop_l = [[0, 0, 0, 3], [0, 20, 1, 3], [0, 40, 2, 3], [1, 0, 10, 2], [1, 20, 11, 2], [1, 40, 12, 2], [2, 0, 20, 1], [2, 20, 21, 1], [2, 40, 22, 1]]

for r in move_route_a :
    if r[0] : movea(task_point_pareta, r[0])
    movels(task_point_pareta, [r[1][0], r[1][-1]], r[1])
    pareta_tmp[r[1][-1]] = 0
    if r[2] : movea(task_point_pareta, r[2])
    move(task_point_pareta, r[1][-1] // 5, r[1][-1] % 5, 50, 100, 1, 100 + r[1][-1], 0)
    mjx(trans(task_point_pareta, [start_pos % 5 * -40, start_pos // 5 * 40, 100, 0, 0, 0]), sol=2, r=10)
    ml([0, 0, -85, 0, 0, 0], mod=1, r=10)
    line_move(task_point_pareta, end_route[1: ])
    ml([0, 0, 85, 0, 0, 0], mod=1, r=5)
    move(task_point_paretc1, 0, 0, 60, 60, 0)
    move(task_point_paretc2, 0, 0, 0, 50, 1, l=1)
    move(task_point_paretc3, 0, 0, 0, 20, 0, l=1)
    move(task_point_paretc4, 0, 0, 0, 50, 1, l=1)
    move(trans(task_point_paretb, [0, 0, loop_l[count][1], 0, 0, 0]), 0, loop_l[count][0], 50, 50, 0, 300 + loop_l[count][2], loop_l[count][3])
    count += 1
plc("DW900", '5')
