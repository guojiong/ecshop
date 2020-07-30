<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2020/7/30
  Time: 9:05
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
  String path = request.getContextPath();
  String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
<html>
  <head>
    <base href="<%=basePath%>">
    <title>$Title$</title>
    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="cache-control" content="no-cache">
    <meta http-equiv="expires" content="0">
    <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
    <meta http-equiv="description" content="This is my page">
  </head>
  <body>
  <form action="servlet/Login" method="post">
    用户名：<input type="text" name="username" value=""><br>
    密 码：<input type="password" name="password" value=""><br>
    用户类型：
    <select name="type">
      <option value="管理员">管理员</option>
      <option value="普通用户">普通用户</option>
    </select><br>
    <input type="submit" value="提交">
    <input type="reset" value="取消">
  </form>
  </body>
</html>
