<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@ page import="java.sql.*"%>
<%@ page import="com.pojo.User" %>
<%@page import="com.dao.UserMapper"  %>

<%
    String path = request.getContextPath();
    String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
    <base href="<%=basePath%>">

    <title>My JSP 'queryBean.jsp' starting page</title>

    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="cache-control" content="no-cache">
    <meta http-equiv="expires" content="0">
    <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
    <meta http-equiv="description" content="This is my page">
    <!--
    <link rel="stylesheet" type="text/css" href="styles.css">
    -->

</head>
<body>
<table border=1>
    <tr><td>用户名</td><td>密码</td><td>用户类型</td><td colspan="2" align="center">数据操作</td></tr>
    <%while(rst.next()) {%>
    <tr><td><%=rst.getString("username") %></td><td><%=rst.getString("password") %></td><td><%=rst.getString("type") %></td><td><a href="deleteBean.jsp?id=<%=rst.getString("id")%>">删除操作</a></td><td><a href="updateBean.jsp?id=<%=rst.getString("id")%>">更新操作</a></td></tr>
    <%} %>
</table>

</body>
</html>
