
<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@ page import="java.sql.*"%>
<%@ page import="nuc.test.user.User" %>
<%@page import="nuc.test.Dao.*"  %>
<%@page import="java.util.*"  %>
<%
    String path = request.getContextPath();
    String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
    <base href="<%=basePath%>">

    <title>My JSP 'showPage.jsp' starting page</title>

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
<table align="center" width="800" border="1">
    <tr>
        <td align="center" colspan="5">
            <h2>所有用户信息</h2>
        </td>
    </tr>
    <tr align="center">
        <td>用户名</td><td>密码</td><td>用户类型</td><td colspan="2">操作方法</td>
    </tr>

    <%
        int currpage=1;
        if(request.getParameter("page")!=null){
            currpage=Integer.parseInt(request.getParameter("page"));
        }
        Find find=new Find();
        List<User> listall=new ArrayList<User>();
        listall=find.Selectcontent(currpage);
        Iterator<User> it=listall.iterator();
        while(it.hasNext()){
            User usera=it.next();

    %>
    <tr align="center">
        <td><%=usera.getUsername() %></td>
        <td><%=usera.getPassword() %></td>
        <td><%=usera.getType() %></td>
        <td><a href="servlet/Update?id=<%=usera.getId()%>">修改</a></td>
        <td><a href="servlet/Delete?id=<%=usera.getId()%>">删除</a></td>
    </tr>
    <%} %>
    <tr>
        <td align="center" colspan="3">
            <jsp:include page="Bar.jsp"/>
        </td>
    </tr>
    <tr align="center"><td colspan="5"><a href="first.jsp">添加用户</a></td></tr>
</table>

</body>

</html>
