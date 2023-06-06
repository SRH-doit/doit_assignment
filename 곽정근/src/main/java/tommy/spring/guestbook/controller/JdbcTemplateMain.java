package tommy.spring.guestbook.controller;

import java.util.Date;
import java.util.List;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import tommy.spring.guestbook.dao.JdbcTemplateGuestMessageDao;
import tommy.spring.guestbook.vo.GuestMessage;

public class JdbcTemplateMain {
	private GuestMessage makeGuestMessage(String guestName, String message) {
		GuestMessage msg = new GuestMessage();
		msg.setGuestName(guestName);
		msg.setMessage(message);
		msg.setRegistryDate(new Date());
		return msg;
	}

	public static void main(String[] args) {
		String[] configLocations = new String[] { "applicationContext.xml" };
		AbstractApplicationContext context = new ClassPathXmlApplicationContext(configLocations);
		JdbcTemplateGuestMessageDao dao = (JdbcTemplateGuestMessageDao) context.getBean("jdbcTemplateGuestMessageDao");
		JdbcTemplateMain myTest = new JdbcTemplateMain();
		dao.insert(myTest.makeGuestMessage("이승재", "하이방가"));
		dao.insert(myTest.makeGuestMessage("javaline", "Hi, Hello"));
		dao.insert(myTest.makeGuestMessage("Spring", "안녕하세요?"));
		int count = dao.count();
		System.out.println("전체글수 : " + count);
		List<GuestMessage> list = dao.select(1, count);
		for (GuestMessage msg : list) {
			System.out.println(msg.getId() + " : " + msg.getGuestName() + " : " + msg.getMessage() + " : "
					+ msg.getRegistryDate());
		}
		context.close();
	}
}
