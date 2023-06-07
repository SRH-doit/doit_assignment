<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title><spring:message code="user.login.title" /></title>
<link href="/myboard/resources/css/style.css" rel="stylesheet"/>
</head>
<body>
<h1><spring:message code="user.login.title" /></h1>
<h3><a href="login.do?lang=en"><spring:message code="user.login.language.en" /></a>&nbsp;&nbsp;
<a href="login.do?lang=ko"><spring:message code="user.login.language.ko" /></a></h3>
<hr>
<form action="login.do" method="post">
<table>
	<tr>
		<td><spring:message code="user.login.id" /></td>
		<td><input type="text" name="id"  value="${userVO.id}"/></td>
	</tr>
	<tr>
		<td><spring:message code="user.login.password" /></td>
		<td><input type="password" name="password" value="${userVO.password}"/></td>
	</tr>
	<tr><td colspan="2"><input type="submit" value="<spring:message code="user.login.loginBtn" />"  /></td></tr>
</table>
</form>  
</body>
</html>