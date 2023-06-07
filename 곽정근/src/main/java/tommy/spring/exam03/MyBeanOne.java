package tommy.spring.exam03;

public class MyBeanOne implements MyBean {

	@Override
	public void sayHello(String name) {
		System.out.println("Hello, " + name + "!!!");
	}

}
