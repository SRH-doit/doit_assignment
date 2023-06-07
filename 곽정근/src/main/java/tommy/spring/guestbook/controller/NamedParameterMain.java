package tommy.spring.guestbook.controller;

import java.util.Date;
import java.util.List;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import tommy.spring.guestbook.dao.NamedParamGuestMessageDao;
import tommy.spring.guestbook.vo.GuestMessage;

public class NamedParameterMain {
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
		NamedParamGuestMessageDao dao = (NamedParamGuestMessageDao) context.getBean("namedParamGuestMessageDao");
		NamedParameterMain myTest = new NamedParameterMain();
		dao.insert(myTest.makeGuestMessage("홍길동", "호부호형"));
		dao.insert(myTest.makeGuestMessage("jspline", "Whats up"));
		dao.insert(myTest.makeGuestMessage("Framework", "반갑습니다^^"));
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
