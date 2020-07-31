<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link type="text/css" href="css/css.css" rel="stylesheet" />
<script type="text/javascript" src="js/jquery.js"></script>
<script type="text/javascript" src="js/js.js"></script>
<style type="text/css">
	thead {
		font-size: 13px;
	}
	tbody{
		font-size: 10px;
	}
	table, thead, th, td {
		border-collapse: collapse;
		margin: auto;
		border: 1px solid gray;
		border-collapse: collapse;
		min-height: 30px;
		min-width: 60px;
	}
</style>
</head>
<script type="text/javascript">
	function add_page() {
		window.location.href = "storage.add";
	}
</script>
<body>
 <div class="hrader" id="header">
  <a href="login.html" style="color:#FD7306;margin-left:20px;">请登录</a> 
  <a href="storage.list">库存查询</a>
  <a href="storage.add">入库登记</a>
  <!-- <a href="reg.html">出库存查询</a> -->
   <div class="topNav">
   <a href="#" class="lan">中文</a>
   <a href="#" class="lan">English</a>
  </div><!--topNav/-->
  </div>
<form action="storage.do" method="post">
   	<div align="center"><h1>库存查询</h1></div>
    <div align="center">
    	<table>
	    	<thead>
	    		<tr>
	    			<th>操作</th>
	    			<th id="storage_time">日期</th>
	    			<th id="code">单据编号</th>
	    			<th id="material_classes">材料类别</th>
	    			<th id="small_class_material">材料小类</th>
	    			<th id="materialName">材料名称</th>
	    			<th id="brand_specification_model" width="100">品牌/规格/型号</th>
	    			<th id="manufacturer_name">厂家名称</th>
	    			<th id="chengs">成色</th>
	    			<th id="unit">单位</th>
	    			<th id="rate">税率</th>
	    			<th id="number">数量</th>
					<th>
						<table>
							<tr><td colspan="4" align="center">材料费</td></tr>
							<tr>
				    			<td id="no_tax_price">不含税单价</td>
				    			<td id="deduction_tax_fee">抵扣税额</td>
				    			<td id="no_tax_total_fee">不含税金额</td>
				    			<td id="contain_tax_total_fee">含税金额</td>
							</tr>
						</table>
					</th>
					<th>
						<table>
							<tr><td colspan="3" align="center">运杂费</td></tr>
							<tr>
				    			<td id="transport_fee_price">单价</td>
				    			<td id="transport_fee_item">金额</td>
				    			<td id="transport_fee_etc">其他</td>
							</tr>
						</table>
					</th>
					<th>
						<table>
							<tr><td colspan="2" align="center">账目与结算相符</td></tr>
							<tr>
				    			<td id="etc_fee">其他费用</td>
				    			<td id="total_fee">合计金额</td>
							</tr>
						</table>
					</th>
	    			<th id="attachment">附件(张)</th>
	    			<th id="procurement">采购人</th>
	    			<th id="inspector">验收员</th>
	    			<th id="supply_unit">供货单位</th>
	    			<th id="belongs_project">所属项目</th>
	    			<th id="remark">备注</th>
	    			
	    		</tr>
    		</thead>
   			<tbody align="center">
   			<% for(int i =0; i < result.size(); i++) { %>
   				<tr>
   					<td style="width: 200px;"><a href="storage.out" style="color: blue; font: menu;">出库登记</a></td>
	    			<td id="storage_time">日期</td>
	    			<td id="code">单据编号</td>
	    			<td id="material_classes">材料类别</td>
	    			<td id="small_class_material">材料小类</td>
	    			<td id="materialName">材料名称</td>
	    			<td id="brand_specification_model">品牌/规格/型号</td>
	    			<td id="manufacturer_name">厂家名称</td>
	    			<td id="chengs">成色</td>
	    			<td id="unit">单位</td>
	    			<td id="rate">税率</td>
	    			<td id="number">数量</td>
					<td>
						<table>
							<tr>
								<td id="no_tax_price">不含税单价</td>
				    			<td id="deduction_tax_fee">抵扣税额</td>
				    			<td id="no_tax_total_fee">不含税金额</td>
				    			<td id="contain_tax_total_fee">含税金额</td>
							</tr>
						</table>
					</td>
					<td>
						<table>
							<tr>
				    			<td id="transport_fee_price">单价</td>
				    			<td id="transport_fee_item">金额</td>
				    			<td id="transport_fee_etc">其他</td>
							</tr>
						</table>
					</td>
					<td>
						<table>
							<tr>
				    			<td id="etc_fee">其他费用</td>
				    			<td id="total_fee">合计金额</td>
							</tr>
						</table>
					</td>
	    			<td id="attachment">附件(张)</td>
	    			<td id="procurement">采购人</td>
	    			<td id="inspector">验收员</td>
	    			<td id="supply_unit">供货单位</td>
	    			<td id="belongs_project">所属项目</td>
	    			<td id="remark">备注</td>
	    		</tr>
	    		<%}%>
   			</tbody>
		</table>
    </div>
    <div class="regSubs">
    </div><!--regSub/-->
   </form><!--/-->
</body>
</html>