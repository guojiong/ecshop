package com.pojo;

public class Goods {
	private Integer id;
	private String storageTime; //入库日期
	private String code; //单据编号 
	private String material_classes; //材料类别
	private String small_class_material; //材料小类
	private String materialName; //材料名称
	private String  brand_specification_model; //品牌/规格/型号
	private String  manufacturer_name; //厂家名称
	private String chengs; //成色
	private String  unit; //单位
	private Float  rate; //税率
	private Integer number; //数量

//	  material_fee; /材料费
	private Float no_tax_price; //不含税单价	 
	private Float deduction_tax_fee; //抵扣税额
	private Float no_tax_total_fee; //不含税金额
	private Float contain_tax_total_fee; //含税金额
	 
//	 	transport_fee /运杂费
	private Float transport_fee_price; //单价
	private Float transport_fee_item; //	 金额
	private Float transport_fee_etc; //其他
	 
//	  账目与结算相符 /accounts_settlement_consistent
	private Float  etc_fee; //其他费用
	private Float total_fee; //合计金额 = 含税金额(contain_tax_total_fee) + 其他费用(etc_fee) 
	  
	private Integer attachment; //附件(张)
	private String procurement; //采购人
	private String inspector; //验收员
	private String supply_unit; //供货单位
	private String belongs_project; //所属项目
	private String remark; //备注
	
	public Goods(int id, String storageTime, String code, String material_classes, String small_class_material, 
			String materialName, String brand_specification_model, String manufacturer_name, String chengs, 
			String unit, float rate, int number, float no_tax_price, float deduction_tax_fee, float no_tax_total_fee, 
			float contain_tax_total_fee, float transport_fee_price, float transport_fee_item, float transport_fee_etc, 
			float etc_fee, float total_fee, int attachment, String procurement, String inspector, String supply_unit, String belongs_project, 
			String remark) {
		this.id=id;
		this.storageTime=storageTime; //入库日期
		this.code=code; //单据编号 
		this.material_classes=material_classes; //材料类别
		this.small_class_material=small_class_material; //材料小类
		this.materialName=materialName; //材料名称
		this. brand_specification_model=brand_specification_model; //品牌/规格/型号
		this. manufacturer_name=manufacturer_name; //厂家名称
		this.chengs=chengs; //成色
		this.unit=unit; //单位
		this.rate=rate; //税率
		this.number=number; //数量

//		  material_fee /材料费
		this.no_tax_price=no_tax_price; //不含税单价	 
		this.deduction_tax_fee=deduction_tax_fee; //抵扣税额
		this.no_tax_total_fee=no_tax_total_fee; //不含税金额
		this.contain_tax_total_fee=contain_tax_total_fee; //含税金额
		 
//		 	transport_fee /运杂费
		this.transport_fee_price=transport_fee_price; //单价
		this.transport_fee_item=transport_fee_item; //	 金额
		this.transport_fee_etc=transport_fee_etc; //其他
		 
//		  账目与结算相符 /accounts_settlement_consistent
		this.etc_fee=etc_fee; //其他费用
		this.total_fee=total_fee; //合计金额 = 含税金额(contain_tax_total_fee) + 其他费用(etc_fee) 
		  
		this.attachment=attachment; //附件(张)
		this.procurement=procurement; //采购人
		this.inspector=inspector; //验收员
		this.supply_unit=supply_unit; //供货单位
		this.belongs_project=belongs_project; //所属项目
		this.remark=remark; //备注
	}
	
    public Goods() {
        super();
    }
    
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	
	public String getStorageTime() {
		return storageTime;
	}

	public void setStorageTime(String storageTime) {
		this.storageTime = storageTime;
	}

	public String getCode() {
		return code;
	}
	public void setCode(String code) {
		this.code = code;
	}
	public String getMaterial_classes() {
		return material_classes;
	}
	public void setMaterial_classes(String material_classes) {
		this.material_classes = material_classes;
	}
	public String getSmall_class_material() {
		return small_class_material;
	}
	public void setSmall_class_material(String small_class_material) {
		this.small_class_material = small_class_material;
	}
	
	public String getMaterialName() {
		return materialName;
	}

	public void setMaterialName(String materialName) {
		this.materialName = materialName;
	}

	public String getBrand_specification_model() {
		return brand_specification_model;
	}
	public void setBrand_specification_model(String brand_specification_model) {
		this.brand_specification_model = brand_specification_model;
	}
	public String getManufacturer_name() {
		return manufacturer_name;
	}
	public void setManufacturer_name(String manufacturer_name) {
		this.manufacturer_name = manufacturer_name;
	}
	public String getChengs() {
		return chengs;
	}
	public void setChengs(String chengs) {
		this.chengs = chengs;
	}
	public String getUnit() {
		return unit;
	}
	public void setUnit(String unit) {
		this.unit = unit;
	}
	public Float getRate() {
		return rate;
	}
	public void setRate(Float rate) {
		this.rate = rate;
	}
	public Integer getNumber() {
		return number;
	}
	public void setNumber(Integer number) {
		this.number = number;
	}
	public Float getNo_tax_price() {
		return no_tax_price;
	}
	public void setNo_tax_price(Float no_tax_price) {
		this.no_tax_price = no_tax_price;
	}
	public Float getDeduction_tax_fee() {
		return deduction_tax_fee;
	}
	public void setDeduction_tax_fee(Float deduction_tax_fee) {
		this.deduction_tax_fee = deduction_tax_fee;
	}
	public Float getNo_tax_total_fee() {
		return no_tax_total_fee;
	}
	public void setNo_tax_total_fee(Float no_tax_total_fee) {
		this.no_tax_total_fee = no_tax_total_fee;
	}
	public Float getContain_tax_total_fee() {
		return contain_tax_total_fee;
	}
	public void setContain_tax_total_fee(Float contain_tax_total_fee) {
		this.contain_tax_total_fee = contain_tax_total_fee;
	}
	public Float getTransport_fee_price() {
		return transport_fee_price;
	}
	public void setTransport_fee_price(Float transport_fee_price) {
		this.transport_fee_price = transport_fee_price;
	}
	public Float getTransport_fee_item() {
		return transport_fee_item;
	}
	public void setTransport_fee_item(Float transport_fee_item) {
		this.transport_fee_item = transport_fee_item;
	}
	public Float getTransport_fee_etc() {
		return transport_fee_etc;
	}
	public void setTransport_fee_etc(Float transport_fee_etc) {
		this.transport_fee_etc = transport_fee_etc;
	}
	public Float getEtc_fee() {
		return etc_fee;
	}
	public void setEtc_fee(Float etc_fee) {
		this.etc_fee = etc_fee;
	}
	public Float getTotal_fee() {
		return total_fee;
	}
	public void setTotal_fee(Float total_fee) {
		this.total_fee = total_fee;
	}
	public Integer getAttachment() {
		return attachment;
	}
	public void setAttachment(Integer attachment) {
		this.attachment = attachment;
	}
	public String getProcurement() {
		return procurement;
	}
	public void setProcurement(String procurement) {
		this.procurement = procurement;
	}
	public String getInspector() {
		return inspector;
	}
	public void setInspector(String inspector) {
		this.inspector = inspector;
	}
	public String getSupply_unit() {
		return supply_unit;
	}
	public void setSupply_unit(String supply_unit) {
		this.supply_unit = supply_unit;
	}
	public String getBelongs_project() {
		return belongs_project;
	}
	public void setBelongs_project(String belongs_project) {
		this.belongs_project = belongs_project;
	}
	public String getRemark() {
		return remark;
	}
	public void setRemark(String remark) {
		this.remark = remark;
	}
}
