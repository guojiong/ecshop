package com.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;

import com.common.ServerResponse;
import com.dao.GoodsMapper;
import com.pojo.Goods;
import com.service.IGoodsService;

public class GoodsServiceImpl implements IGoodsService{
	
	@Autowired
	private GoodsMapper goodsMapper;
	
	public ServerResponse<List<Goods>> getQueryStorage() {
		ServerResponse<List<Goods>> list = goodsMapper.getQueryStorage();
		return list;
	}

}
