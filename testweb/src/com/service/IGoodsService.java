package com.service;

import com.common.ServerResponse;
import com.pojo.Goods;

/**
 * Created by geely
 */
public interface IGoodsService {

    ServerResponse<String> add(Goods goods);
    ServerResponse<Goods> update(Goods goods);

}
