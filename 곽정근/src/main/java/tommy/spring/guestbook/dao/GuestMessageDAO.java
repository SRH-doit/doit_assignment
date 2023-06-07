package tommy.spring.guestbook.dao;

import java.util.List;

import tommy.spring.guestbook.vo.GuestMessage;

public interface GuestMessageDAO {
	public int count();

	public List<GuestMessage> select(int begin, int end);

	public int insert(GuestMessage message);

	public int delete(int id);

	public int update(GuestMessage message);
}
