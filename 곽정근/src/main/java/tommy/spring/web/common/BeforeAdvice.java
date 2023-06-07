package tommy.spring.web.common;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Service;

@Service // <bean id="beforeAdvice" class="tommy.spring.web.common.BeforeAdvice"/>
@Aspect  // <aop:aspect ref="beforeAdvice"/>
public class BeforeAdvice {
	// <aop:before method="beforLog" pointcut-ref="allPointcut()"/>
	@Before("PointcutCommon.allPointcut()")
	public void beforeLog(JoinPoint joinPoint) {
		String method = joinPoint.getSignature().getName();
		Object[] args = joinPoint.getArgs();
		System.out.println("[����ó��] : " + method + "() �޼����� ARGS ���� : " + args[0].toString());
	}
}
