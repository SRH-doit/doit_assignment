package tommy.spring.guestbook.dao;

import java.sql.Types;
import java.util.List;

import javax.sql.DataSource;

import org.springframework.jdbc.core.JdbcTemplate;

import tommy.spring.guestbook.vo.GuestMessage;

public class JdbcTemplateGuestMessageDao implements GuestMessageDAO {

	private JdbcTemplate jdbcTemplate;

	public JdbcTemplateGuestMessageDao(DataSource dataSource) {
		jdbcTemplate = new JdbcTemplate(dataSource);
	}

	public int count() {
		return jdbcTemplate.queryForObject("select count(*) from GUESTBOOK", Integer.class);
	}

	public int delete(int id) {
		return jdbcTemplate.update("delete from GUESTBOOK where MESSAGE_ID = ?", id);
	}

	public int insert(final GuestMessage message) {
		int insertedCount = jdbcTemplate.update(
				"insert into GUESTBOOK(MESSAGE_ID, GUEST_NAME, "
						+ "MESSAGE, REGISTRY_DATE) values (guest_seq.nextval, ?, ?, ?)",
				message.getGuestName(), message.getMessage(), message.getRegistryDate());
		return insertedCount;
	}

	public List<GuestMessage> select(int begin, int end) {
		return jdbcTemplate.query(
				"select * from (select ROWNUM rnum, MESSAGE_ID, GUEST_NAME," + "MESSAGE, REGISTRY_DATE "
						+ "from (select * from GUESTBOOK order by MESSAGE_ID desc)) " + "where rnum>=? and rnum<=?",
				new GuestMessageRowMapper(), new Object[] { begin, end });
	}

	public int update(GuestMessage message) {
		return jdbcTemplate.update("update GUESTBOOK " + "set MESSAGE = ? where MESSAGE_ID = ?",
				new Object[] { message.getMessage(), message.getId() }, new int[] { Types.VARCHAR, Types.INTEGER });
	}
}
