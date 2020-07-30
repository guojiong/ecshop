<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ajax获取集合</title>
<script src="../js/jquery-3.1.1.min.js"></script>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>id</th>
                <th>姓名</th>
                <th>生日</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>
    名字:<input type="text" placeholder="请输入姓名" id="name">
    生日:年<select>
    <option>1992</option>
    <option>1993</option>
    <option>1994</option>
    <option>1995</option>
    </select>
    月<select>
    <option>1</option>
    <option>2</option>
    <option>3</option>
    <option>4</option>
    </select>
    日<select>
    <option>2</option>
    <option>12</option>
    <option>22</option>
    <option>23</option>
    </select>
    <button>点击获取数据</button>
    <button>点击插入数据</button><br>
    请输入删除的名字:<input type="text" id="removename">
    <button>点击删除数据</button><br>
    请输入需要修改的id号:<input type="text" id="updateid"><br>
    请输入需要修改后的名字:名字:<input type="text" placeholder="请输入姓名" id="updatename"><br>
    请输入需要修改的后生日:生日:年<select>
    <option>1992</option>
    <option>1993</option>
    <option>1994</option>
    <option>1995</option>
    </select>
    月<select>
    <option>1</option>
    <option>2</option>
    <option>3</option>
    <option>4</option>
    </select>
    日<select>
    <option>2</option>
    <option>12</option>
    <option>22</option>
    <option>23</option>
    </select><br>
    <button>点击跟新数据</button>
    
    <script>
    $(function(){
        var str;
         //serverIndex区分增删改查的变量
       var serverIndex;
        //点击查看数据
        $("button").eq(0).click(function(){
            var str;
            serverIndex=1;
            //{serverIndex:serverIndex}是拼在地址栏上的,从后端获取他的值
            $.get("http://localhost:8080/jquery/servlet/OneServlet",{serverIndex:serverIndex},function(data){
            console.log(data);
            var num=eval(data);
            for(var i=0;i<num.length;i++)
                {
                str+=" <tr> <td>"+num[i].id+"</td> <td>"+num[i].name+"</td> <td>"+num[i].birthday+"</td></tr>";
            }
         $("tbody").html(str); 
         
            })
        })
        //点击插入数据
        $("button").eq(1).click(function(){
          //获取输入名字的值
          serverIndex=2;
          var name=$("#name").val();
          var year=$("select:eq(0) option:selected").val();
           var mouth=$("select:eq(1) option:selected").val();
           var day=$("select:eq(2) option:selected").val();
          var birthday=year+"/"+mouth+"/"+day;
           console.log(birthday);
           $.get("http://localhost:8080/jquery/servlet/OneServlet",{serverIndex:serverIndex,name:name,birthday:birthday},function(data){
               console.log(data);
           })
        
        })
        
        //点击删除数据
        $("button").eq(2).click(function(){
          //获取输入名字的值
          serverIndex=3;
          var name=$("#removename").val();
           $.get("http://localhost:8080/jquery/servlet/OneServlet",{serverIndex:serverIndex,name:name},function(data){
               console.log(data);
           })
          
        })
        //点击跟新数据
        $("button").eq(3).click(function(){
          //获取输入名字的值
          serverIndex=4;
          var id=$("#updateid").val();
          var name=$("#updatename").val();
          var year=$("select:eq(3) option:selected").val();
           var mouth=$("select:eq(4) option:selected").val();
           var day=$("select:eq(5) option:selected").val();
          var birthday=year+"/"+mouth+"/"+day;
           $.get("http://localhost:8080/jquery/servlet/OneServlet",{serverIndex:serverIndex,name:name,id:id,birthday:birthday},function(data){
               console.log(data);
           })
          
        })
        })
         
</script>
</body>
</html>