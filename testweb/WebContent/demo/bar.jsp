
<%@ page language="java" import="java.util.*" pageEncoding="ISO-8859-1"%>
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

    <title>My JSP 'Bar.jsp' starting page</title>

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
    int pages;
    int currpage=1;
    if(request.getParameter("page")!=null){
        currpage=Integer.parseInt(request.getParameter("page"));
    }
    Find find=new Find();
    int count=find.SelectCount();
    if(count%User.PAGESIZE==0){
        pages=count/User.PAGESIZE;
    }
    else{
        pages=count/User.PAGESIZE+1;
    }
    StringBuffer sb=new StringBuffer();
    for(int i=1;i<=pages;i++){
        if(i==currpage){
            sb.append("["+i+"]");
        }else{
            sb.append("<a href='showPage.jsp?page="+i+"'>"+i+"</a>");
        }
        sb.append("  ");
    }
    out.print(sb);

    request.setAttribute("bar",sb.toString());

%>

</body>

</html>
