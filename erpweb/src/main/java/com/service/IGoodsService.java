package com.service;

import java.util.List;

import com.common.ServerResponse;
import com.pojo.Goods;

public interface IGoodsService {
	ServerResponse<List<Goods>> getQueryStorage();
}
