package com.service.impl;

import com.common.ServerResponse;
import com.dao.GoodsMapper;
import com.pojo.Goods;
import com.service.IGoodsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Created by geely
 */
@Service("iGoodsService")
public class GoodsServiceImpl implements IGoodsService {

    @Autowired
    private GoodsMapper goodsMapper;

    /**
     *用户注册
     * @param user
     * @return
     */
    public ServerResponse<String> add(Goods goods){
        int resultCount = goodsMapper.insert(goods);
        if(resultCount == 0){
            return ServerResponse.createByErrorMessage("注册失败");
        }
        return ServerResponse.createBySuccessMessage("注册成功");
    }



    /**
     * 更新用户信息
     * @param user
     * @return
     */
    public ServerResponse<Goods> update(Goods goods){
    	Goods updateGoods = new Goods();
        updateGoods.setId(goods.getId());

        int updateCount = goodsMapper.updateByPrimaryKeySelective(updateGoods);
        if(updateCount > 0){
            return ServerResponse.createBySuccess("更新成功",updateGoods);
        }
        return ServerResponse.createByErrorMessage("更新失败");
    }

}
