package com.controller.portal;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
//import org.springframework.web.servlet.mvc.Controller;

/**
 * 控制器
 */
@Controller
public class HelloController {

    @RequestMapping(value = "/web")
    public ModelAndView handleRequest(javax.servlet.http.HttpServletRequest httpServletRequest, javax.servlet.http.HttpServletResponse httpServletResponse) throws Exception {
        System.out.println("test Mav");
        ModelAndView mav = new ModelAndView("login");
        mav.addObject("message","Hello Spring MVC");
        // 返回给 DispatcherServlet
        return mav;
    }
}
