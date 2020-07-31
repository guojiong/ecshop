package com.controller.portal;

import java.io.PrintWriter;
import java.util.List;
import javax.servlet.http.HttpServletResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
import com.common.ServerResponse;
import com.pojo.Goods;
import com.service.IGoodsService;
import net.sf.json.JSONArray;

@Controller
public class GoodsController {
    @Autowired
    private IGoodsService iGoodsService;
    
    @RequestMapping(value = "/storage.add")
    public ModelAndView erpStorageAdd(Goods goods) {
    	ModelAndView mav = new ModelAndView();
        if (goods.getId()==null) {
        	if(goods.getMaterialName()==null){
        		mav.setViewName("storage_add");
	        }else {
	        	iGoodsService.add(goods);
	        	mav.setViewName("success");
	        	mav.addObject("message", "storage.list");
		    }
        }else {
        	iGoodsService.update(goods);
        	mav.setViewName("success");
        	mav.addObject("message", "storage.list");
    	}
        return mav;
    }
    
    @RequestMapping(value = "/storage.list")
    public ModelAndView erpStorageList(Goods goods) {
    	ModelAndView mav = new ModelAndView();
    	ServerResponse<List<Goods>> results = iGoodsService.queryStorage();
		mav.setViewName("success");
		mav.addObject("result", results);
        return mav;
    }
    
    @RequestMapping(value = "/demo")
    public ModelAndView demo(Goods goods) {
    	ModelAndView mav = new ModelAndView();
		mav.setViewName("demo");
        return mav;
    }
    
    @RequestMapping(value="/queryAllStudent")
    public void query(HttpServletResponse resp) {
        try {
            /*list集合中存放的是好多student对象*/
            List<Goods> students = (List<Goods>) iGoodsService.queryStorage(); //getAllStudentInfo();
            /*将list集合装换成json对象*/
            JSONArray data = JSONArray.fromObject(students);
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