<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%
    String path = request.getContextPath();
    String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<%@ page import="java.sql.*"%>
<%@ page import="nuc.test.user.User" %>
<%@page import="nuc.test.Dao.UserDao"  %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
    <base href="<%=basePath%>">

    <title>My JSP 'updateBean.jsp' starting page</title>

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
<%
    request.setCharacterEncoding("utf-8");
    UserDao user=new UserDao();
    User usera=new User();
    usera.setId(request.getParameter("id"));
    ResultSet rs=user.Select(usera);
    if(rs.next()){
%>
<form action="doUpdateBean.jsp?id=<%=rs.getString("id")%>" method="post">
    用户名:<input type="text" value="<%=rs.getString("username") %>" name="username"><br>
    密 码:<input type="text" value="<%=rs.getString("password") %>" name="password"><br>
    用户类型:<select name="type">
    <option value="管理员">管理员</option>
    <option value="普通用户">普通用户</option>
</select><br>
    <input type="submit" value="提交">
    <input type="reset" value="取消">
</form>


%} %>

</body>

</html>
