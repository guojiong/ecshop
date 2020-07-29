<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>goods_list</title>
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
  <a href="reg.html">入库存查询</a>
  <a href="reg.html">出库存查询</a>
   <div class="topNav">
   <a href="#" class="lan">中文</a>
   <a href="#" class="lan">English</a>
  </div><!--topNav/-->
  </div>
<div class="mainCont">
  <div class="loginBuy">
   <form action="storage.do" method="post">
    <div align="center">
    	<a href="storage.add">入库登记</a>
    	<table border="1">
    	<thead>
    		<tr>
    			<th for="storage_time">日期</th>
    			<th for="code">单据编号</th>
    			<th for="material_classes">材料类别</th>
    			<th for="small_class_material">材料小类</th>
    			<th for="materialName">材料名称</th>
    			<th for="brand_specification_model">品牌/规格/型号</th>
    			<th for="manufacturer_name">厂家名称</th>
    			<th for="chengs">成色</th>
    			<th for="unit">单位</th>
    			<th for="rate">税率</th>
    			<th for="number">数量</th>
			<!-- <tr><td colspan="8" align="center"><h3>材料费</h3></td></tr> -->
    			<th for="no_tax_price">不含税单价</th>
    			<th for="deduction_tax_fee">抵扣税额</th>
    			<th for="no_tax_total_fee">不含税金额</th>
    			<th for="contain_tax_total_fee">含税金额</th>
			<!-- <tr><td colspan="8" align="center"><h3>运杂费</h3></td></tr> -->
    			<th for="transport_fee_price">单价</th>
    			<th for="transport_fee_item">金额</th>
    			<th for="transport_fee_etc">其他</th>
			<!-- <tr><td colspan="8" align="center"><h3>账目与结算相符</h3></td></tr> -->
    			<th for="etc_fee">其他费用</th>
    			<th for="total_fee">合计金额</th>
    			<th for="attachment">附件(张)</th>
    			<th for="procurement">采购人</th>
    			<th for="inspector">验收员</th>
    			<th for="supply_unit">供货单位</th>
    			<th for="belongs_project">所属项目</th>
    			<th for="remark">备注</th>
    		</tr>
    		</thead>
    		<tr>
    			<tbody></tbody>
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
