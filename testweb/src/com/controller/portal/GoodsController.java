package com.controller.portal;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
import com.pojo.Goods;
import com.service.IGoodsService;

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
		mav.setViewName("storage_list_t");
        return mav;
    }
    
    @RequestMapping(value = "/demo")
    public ModelAndView demo() {
    	ModelAndView mav = new ModelAndView();
		mav.setViewName("demo");
        return mav;
    }
}