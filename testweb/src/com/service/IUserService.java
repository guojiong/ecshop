package com.service;

import java.util.List;

import com.common.ServerResponse;
import com.pojo.User;

/**
 * Created by geely
 */
public interface IUserService {

    ServerResponse<User> login(String username, String password);
    
    ServerResponse<String> register(User user);

    ServerResponse<String> checkValid(String str,String type);

    ServerResponse selectQuestion(String username);

    ServerResponse<String> checkAnswer(String username,String question,String answer);

    ServerResponse<String> forgetResetPassword(String username,String passwordNew,String forgetToken);

    ServerResponse<String> resetPassword(String passwordOld,String passwordNew,User user);

    ServerResponse<User> updateInformation(User user);

    ServerResponse<User> getInformation(Integer userId);
    
    ServerResponse<List<User>> Query();

    ServerResponse checkAdminRole(User user);
}
