package tommy.spring.exam03;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

public class HelloSpring {
	public static void main(String[] args) {
		AbstractApplicationContext factory = 
				new GenericXmlApplicationContext("applicationContext.xml");
		MyBean bean = (MyBean) factory.getBean("myBean");
		bean.sayHello("Spring");
		factory.close();
	}
}
