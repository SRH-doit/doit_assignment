package tommy.spring.web.common;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Service;

@Service
@Aspect
public class AfterAdvice {
	@After("PointcutCommon.allPointcut()")
	public void finallyLog(JoinPoint joinPoint) {
		String method = joinPoint.getSignature().getName();
		System.out.println("[����ó��] : " + method + "() �޼��� ���� �� ������ ����");
	}
}
