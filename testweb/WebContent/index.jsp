<!-- <script language="javascript" type="text/javascript">
    window.location.href="login.page";
</script> -->
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    String path = request.getContextPath();
    String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
<a href="demo/login.jsp">demo_login</a><br>
<a href="storage/query_storage.jsp">erp</a><br>
<a href="demo/query.jsp">demo_query</a><br>
<a href="login.page">test</a><br>
<a href="storage.list">erp</a><br>
<a href="demo">demo</a><br>

<a href="query.do">query.do</a><br>