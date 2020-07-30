<%@ page language="java" import="java.util.*" pageEncoding="ISO-8859-1"%>
<%@ page import="java.sql.*"%>
<%@ page import="nuc.test.user.User" %>
<%@page import="nuc.test.Dao.UserDao"  %>

<%
    String path = request.getContextPath();
    String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
    <base href="<%=basePath%>">

    <title>My JSP 'doUpdateBean.jsp' starting page</title>

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
<%request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="use" class="nuc.test.user.User">
    <jsp:setProperty name="use" property="*"/>
</jsp:useBean>
<%
    UserDao user=new UserDao();
    //User usera=new User();
    use.setId(request.getParameter("id"));

    int rs=0;
    rs=user.Update(use);
%>
<jsp:forward page="queryBean.jsp"/>
</body>

</html>
