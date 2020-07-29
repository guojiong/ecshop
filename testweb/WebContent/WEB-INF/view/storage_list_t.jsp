<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style type="text/css">
	thead {
		font-size: 13px;
	}
	tbody{
		font-size: 10px;
	}
	table, thead, th {
		border-collapse: collapse;
		margin: auto;
		border: 1px solid gray;
	}
	td{
		align-content:center;
		min-width: 60px;
		max-width: 150px;
	}
</style>
</head>
<body>
<form action="storage.do" method="post">
    <div align="center">
    	<a href="storage.add">入库登记</a>
    	<table>
	    	<thead>
	    		<tr>
	    			<th id="storage_time">日期</th>
	    			<th id="code">单据编号</th>
	    			<th id="material_classes">材料类别</th>
	    			<th id="small_class_material">材料小类</th>
	    			<th id="materialName">材料名称</th>
	    			<th id="brand_specification_model">品牌/规格/型号</th>
	    			<th id="manufacturer_name">厂家名称</th>
	    			<th id="chengs">成色</th>
	    			<th id="unit">单位</th>
	    			<th id="rate">税率</th>
	    			<th id="number">数量</th>
				<!-- <tr><td colspan="8" align="center"><h3>材料费</h3></td></tr> -->
	    			<th id="no_tax_price">不含税单价</th>
	    			<th id="deduction_tax_fee">抵扣税额</th>
	    			<th id="no_tax_total_fee">不含税金额</th>
	    			<th id="contain_tax_total_fee">含税金额</th>
				<!-- <tr><td colspan="8" align="center"><h3>运杂费</h3></td></tr> -->
	    			<th id="transport_fee_price">单价</th>
	    			<th id="transport_fee_item">金额</th>
	    			<th id="transport_fee_etc">其他</th>
				<!-- <tr><td colspan="8" align="center"><h3>账目与结算相符</h3></td></tr> -->
	    			<th id="etc_fee">其他费用</th>
	    			<th id="total_fee">合计金额</th>
	    			<th id="attachment">附件(张)</th>
	    			<th id="procurement">采购人</th>
	    			<th id="inspector">验收员</th>
	    			<th id="supply_unit">供货单位</th>
	    			<th id="belongs_project">所属项目</th>
	    			<th id="remark">备注</th>
	    		</tr>
    		</thead>
   			<tbody>
   				<tr>
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
				<!-- <tr><td colspan="8" align="center"><h3>材料费</h3></td></tr> -->
	    			<td id="no_tax_price">不含税单价</td>
	    			<td id="deduction_tax_fee">抵扣税额</td>
	    			<td id="no_tax_total_fee">不含税金额</td>
	    			<td id="contain_tax_total_fee">含税金额</td>
				<!-- <tr><td colspan="8" align="center"><h3>运杂费</h3></td></tr> -->
	    			<td id="transport_fee_price">单价</td>
	    			<td id="transport_fee_item">金额</td>
	    			<td id="transport_fee_etc">其他</td>
				<!-- <tr><td colspan="8" align="center"><h3>账目与结算相符</h3></td></tr> -->
	    			<td id="etc_fee">其他费用</td>
	    			<td id="total_fee">合计金额</td>
	    			<td id="attachment">附件(张)</td>
	    			<td id="procurement">采购人</td>
	    			<td id="inspector">验收员</td>
	    			<td id="supply_unit">供货单位</td>
	    			<td id="belongs_project">所属项目</td>
	    			<td id="remark">备注</td>
	    		</tr>
   			</tbody>
		</table>
     <input type="submit" value=" 确认入库 " />
     <input type="button" value=" 取消并返回 " />
    </div>
    
    <div class="regSubs">
    </div><!--regSub/-->
   </form><!--/-->
</body>
</html>