package com.pojo;

public class Goods {
	private Integer id;
	private String storageTime; //入库日期
	
	public Goods() {
		super();
	}
	
	public Goods(int id, String storageTime) {
		this.id = id;
		this.storageTime = storageTime;
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
	
}
