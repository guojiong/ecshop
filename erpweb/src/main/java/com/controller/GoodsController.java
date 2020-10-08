package com.controller;

import java.io.PrintWriter;
import java.util.List;

import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import com.common.ServerResponse;
import com.pojo.Goods;
import com.service.IGoodsService;

import net.sf.json.JSONArray;

@Controller
public class GoodsController {
	
	@Autowired
	IGoodsService iGoodsService;
	
	@RequestMapping(value="/queryAllStudent")
    public void query(HttpServletResponse resp) {
        try {
            /*list集合中存放的是好多student对象*/
        	ServerResponse<List<Goods>> students = iGoodsService.getQueryStorage(); //getAllStudentInfo();
            /*将list集合装换成json对象*/
            JSONArray data = JSONArray.fromObject(students.getData());
            //接下来发送数据
            /*设置编码，防止出现乱码问题*/
            resp.setCharacterEncoding("utf-8");
            /*得到输出流*/
            PrintWriter respWritter = resp.getWriter();
            /*将JSON格式的对象toString()后发送*/
            respWritter.append(data.toString());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
