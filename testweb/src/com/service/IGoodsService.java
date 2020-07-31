package com.service;

import java.util.List;
import com.common.ServerResponse;
import com.pojo.Goods;

/**
 * Created by geely
 */
public interface IGoodsService {

    ServerResponse<String> add(Goods goods);
    ServerResponse<Goods> update(Goods goods);
    ServerResponse<List<Goods>> queryStorage();

}
