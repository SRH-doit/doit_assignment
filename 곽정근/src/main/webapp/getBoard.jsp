<%@ page import="tommy.spring.web.board.impl.BoardDAO"%>
<%@ page import="tommy.spring.web.board.BoardVO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link href="/myboard/resources/css/style.css" rel="stylesheet"/>
<title>Board Article Content</title>
</head>
<body>
<h1>글 상세</h1><hr><h3><a href="logout.do">Log Out</a></h3>
<form action="updateBoard.do" method="post">
<input name="seq" type="hidden" value="${board.seq }" />
<table>
<tr>
	<td>제목</td>
	<td><input name="title" type="text" value="${board.title }" /></td>
</tr>
<tr>
	<td>작성자</td>
	<td>${board.writer }</td>
</tr>
<tr>
	<td>내용</td>
	<td><textarea name="content">${board.content }</textarea></td>
</tr>
<tr>
	<td>등록일</td>
	<td>${board.regDate }</td>
</tr>
<tr>
	<td>조회수</td>
	<td>${board.cnt }</td>
</tr>
<tr>
	<td colspan="2"><input type="submit" value="글수정" /></td>
</tr>
</table>
</form><hr>
<a href="insertBoard.jsp"><input type="submit" value="글등록" /></a>&nbsp;&nbsp;&nbsp;
<a href="deleteBoard.do?seq=${board.seq }"><input type="submit" value="글삭제" /></a>&nbsp;&nbsp;&nbsp;
<a href="getBoardList.do"><input type="submit" value="글목록" /></a>
</body>
</html>