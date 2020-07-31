<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>unique</title>
<link type="text/css" href="css/css.css" rel="stylesheet" />
<script type="text/javascript" src="js/jquery.js"></script>
<script type="text/javascript" src="js/js.js"></script>
<style type="text/css">
input {width: 150px}
tr {line-height: 25px}
label {display:block; text-align:right;}
</style>
</head>


<body>
 <div class="hrader" id="header">
  <a href="login.html" style="color:#FD7306;margin-left:20px;">请登录</a> 
   <a href="storage.list">库存查询</a>
  <a href="storage.add">入库登记</a>
   <div class="topNav">
   <a href="#" class="lan">中文</a>
   <a href="#" class="lan">English</a>
  </div><!--topNav/-->
  </div>
<div class="mainCont">
  <div class="loginBuy">
   <form action="storage.add" method="post">
    <div align="center">
    	<h1>入库登记</h1>
    	<table>
    		<tr>
		    	<td><label for="storage_time">日期：</label></td>
		    	<td><input type="text" id="storageTime"/></td>
		    	<td><label for="code">单据编号：</label></td>
		    	<td><input type="text" id="code" /></td>
    			<td><label for="material_classes">材料类别：</label></td>
		    	<td><input type="text" id="material_classes" /></td>
    			<td><label for="small_class_material">材料小类：</label></td>
		    	<td><input type="text" id="small_class_material" /></td>
    		</tr>
			<tr>
    			<td><label for="materialName">材料名称：</label></td>
    			<td><input type="text" name="materialName" /></td>
    			<td><label for="brand_specification_model">品牌/规格/型号：</label></td>
    			<td><input type="text" id="brand_specification_model" /></td>
    			<td><label for="manufacturer_name">厂家名称：</label></td>
    			<td><input type="text" id="manufacturer_name" /></td>
    			<td><label for="chengs">成色：</label></td>
    			<td><input type="text" id="chengs" /></td>
    		</tr>
			<tr>
    			<td><label for="unit">单位：</label></td>
				<td><input type="text" id="unit" /></td>
    			<td><label for="rate">税率：</label></td>
				<td><input type="text" id="rate" /></td>
    			<td><label for="number">数量：</label></td>
				<td><input type="text" id="number" /></td>
    			<td></td>
    		</tr>
			<tr><td colspan="8" align="center"><h3>材料费</h3></td></tr>
			<tr>
    			<td><label for="no_tax_price">不含税单价：</label></td>
				<td><input type="text" id="no_tax_price" /></td>
    			<td><label for="deduction_tax_fee">抵扣税额：</label></td>
				<td><input type="text" id="deduction_tax_fee" /></td>
    			<td><label for="no_tax_total_fee">不含税金额：</label></td>
				<td><input type="text" id="no_tax_total_fee" /></td>
    			<td><label for="contain_tax_total_fee">含税金额：</label></td>
				<td><input type="text" id="contain_tax_total_fee" /></td>
    		</tr>
			<tr><td colspan="8" align="center"><h3>运杂费</h3></td></tr>
			<tr>
    			<td><label for="transport_fee_price">单价：</label></td>
    			<td><input type="text" id="transport_fee_price" /></td>
    			<td><label for="transport_fee_item">金额：</label></td>
				<td><input type="text" id="transport_fee_item" /></td>
    			<td><label for="transport_fee_etc">其他：</label></td>
				<td><input type="text" id="transport_fee_etc" /></td>
    			<td></td>
    		</tr>
			<tr><td colspan="8" align="center"><h3>账目与结算相符</h3></td></tr>
			<tr>
    			<td><label for="etc_fee">其他费用：</label></td>
				<td><input type="text" id="etc_fee" /></td>
    			<td><label for="total_fee">合计金额：</label></td>
				<td><input type="text" id="total_fee" /></td>
    		</tr>
			<tr>
    			<td><label for="attachment">附件(张)：</label></td>
				<td><input type="text" id="attachment" /></td>
    			<td><label for="procurement">采购人：</label></td>
				<td><input type="text" id="procurement" /></td>
    			<td><label for="inspector">验收员：</label></td>
				<td><input type="text" id="inspector" /></td>
    			<td><label for="supply_unit">供货单位：</label></td>
				<td><input type="text" id="supply_unit" />
    			</td>
    		</tr>
			<tr>
    			<td><label for="belongs_project">所属项目：</label></td>
				<td><input type="text" id="belongs_project" /></td>
    			<td><label for="remark">备注：</label></td>
				<td><input type="text" id="remark" /></td>
    		</tr>
		</table>
     <input type="submit" value=" 确认入库 " />
     <input type="button" value=" 取消并返回 " />
    </div>
    
    <div class="regSubs">
    </div><!--regSub/-->
   </form><!--/-->
   
  <div class="loginBuyRight">
  </div><!--loginBuyRight/-->
  <div class="clears"></div>
  </div><!--loginBuy/-->
 </div><!--mainCont/-->
 <div class="footer" style="text-align:left;">
  <a href="#">关于我们</a>
  <a href="#">友情链接</a>
  <a href="#">版权声明</a>
  <a href="#">网站地图</a>
  <br />
 </div><!--footer/-->
</body>
</html>
