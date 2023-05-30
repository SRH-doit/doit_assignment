set_velx(1000),set_velj(2000),set_accx([150,150,180,225,225,225]),set_accj([300,300,360,450,450,450])
set_tool('tool'),set_tcp('tcp')
w, ml, mj, mjz, tool = wait, movel, movej, movejx, set_tool_digital_outputs
set_motion_end(DR_CHECK_OFF)
drl_report_line(OFF)
from queue import PriorityQueue as pqueue
from collections import deque
from itertools import product
def move(task_point, y=0,x=0,z=0,lz=0, gr=0, val=0, n=0,l=0,){
    max_r = lambda r : r if r<10 else 9
    task_point = get_current_posx()[0]
    r=[get_distance(task_point_now,task_point_next)/15 if get_distance(task_point_now, task_point)> 2 else 0,(z/2-0.5) fi z < 2 else 0, (lz/2-0.5) if lz < 2 else 0]
    
}