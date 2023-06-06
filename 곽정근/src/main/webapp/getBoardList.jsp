<%@ page import="java.util.List"%>
<%@ page import="tommy.spring.web.board.impl.BoardDAO"%>
<%@ page import="tommy.spring.web.board.BoardVO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link href="/myboard/resources/css/style.css" rel="stylesheet"/>
<title><spring:message code="board.list.mainTitle" /></title>
</head>
<body>
<h1><spring:message code="board.list.mainTitle" /></h1><hr>
<h3>곽정근 <spring:message code="board.list.welcomeMsg" />...<a href="logout.do">Log-Out</a></h3>
<!-- 검색 시작 -->
<form action="getBoardList.do" method="post">
<table>
<tr>
	<td>
		<select class="box" name="searchCondition">
			<c:forEach items="${conditionMap }" var="option">
				<option value="${option.value }">${option.key }</option>
			</c:forEach>
		</select>
	</td>
	<td><input type="text" name="searchKeyword" /></td>
	<td><input type="submit" value="<spring:message code="board.list.search.condition.btn" />" /></td>
</tr>
</table>
</form><br/>
<!-- 검색 종료 -->
<table>
<tr>
	<th><spring:message code="board.list.table.head.seq" /></th>
	<th><spring:message code="board.list.table.head.title" /></th>
	<th><spring:message code="board.list.table.head.writer" /></th>
	<th><spring:message code="board.list.table.head.regDate" /></th>
	<th><spring:message code="board.list.table.head.cnt" /></th>
</tr>
<c:forEach var="board" items="${boardList }">
<tr>
	<td>${board.seq }</td>
	<td><a href="getBoard.do?seq=${board.seq }">${board.title }</a></td>
	<td>${board.writer }</td>
	<td><fmt:formatDate value="${board.regDate }" pattern="yyyy-MM-dd"/></td>
	<td>${board.cnt }</td>
</tr>
</c:forEach>
</table><br/>
<a href="insertBoard.jsp"><input type="submit" value="<spring:message code="board.list.link.insertBoard" />" /></a>
</body>
</html>