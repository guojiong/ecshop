package com.dao;

import java.util.List;

import com.common.ServerResponse;
import com.pojo.Goods;

public interface GoodsMapper {
	ServerResponse<List<Goods>> getQueryStorage();
}
