package com.dao;

import com.common.ServerResponse;
import com.pojo.Goods;
import com.pojo.User;

import java.util.List;

import org.apache.ibatis.annotations.Param;

public interface GoodsMapper {
    int deleteByPrimaryKey(Integer id);

    int insert(Goods record);

    int insertSelective(Goods record);
    
    ServerResponse<List<Goods>> queryStorage();

    User selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(Goods record);

    int updateByPrimaryKey(Goods record);

}