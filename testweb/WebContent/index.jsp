<!-- <script language="javascript" type="text/javascript">
    window.location.href="login.page";
</script> -->
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    String path = request.getContextPath();
    String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
<DOCTYPE html>
<html>
<head>
<title></title>
<script type="text/javascript" src="js/jquery.js"></script>
<script type="text/javascript" src="js/js.js"></script>
<script type="text/javascript">
	function requestsData(){
		$.ajax({
			url: "queryAllStudent",
			type: "post",
			dataType: "json",
			success: function(data){
				/*这个方法里是ajax发送请求成功之后执行的代码*/
				showData(data);//我们仅做数据展示
			},
			error: function(msg){
				alert("ajax连接异常："+msg);
			}
		});
	}
	
	//展示数据
	function showData(data) {
		var str = "";//定义用于拼接的字符串
		for (var i = 0; i < data.length; i++) {
	 	//拼接表格的行和列
		str = "<tr><td>" + data[i].name + "</td><td>" + data[i].password + "</td></tr>";
		//追加到table中
		$("#tab").append(str);         }
	}
</script>
</head>
<body>
<a href="demo/login.jsp">demo_login</a><br>
<a href="storage/query_storage.jsp">erp</a><br>
<a href="demo/query.jsp">demo_query</a><br>
<a href="login.page">test</a><br>
<a href="storage.list">erp</a><br>
<a href="demo">demo</a><br>
<a href="query.do">query.do</a><br>
	<input type="button" value="查询" onclick="requestsData()"/>
	<table id="tab">
		<tr>
			<th>姓名</th>
			<th>密码</th>
			<th>性别</th>
		</tr>
		<tr>
			<th>姓名</th>
			<th>密码</th>
			<th>性别</th>
		</tr>
	</table>
</body>
</html>
