package tommy.spring.exam02;

public class MyBeanOne implements MyBean {

	@Override
	public void sayHello(String name) {
		System.out.println("Hello, " + name + "!!!");
	}

}
