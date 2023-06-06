package tommy.spring.web.user;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class LogoutController {

	@RequestMapping("/logout.do")
	public String logout(HttpSession session) {
		System.out.println("�α׾ƿ� ó��");
		// 1. �������� ����� ���� ����
		session.invalidate();

		// 2. ���� ���� �� ����ȭ������ �̵�
		return "login.jsp";
	}

}
