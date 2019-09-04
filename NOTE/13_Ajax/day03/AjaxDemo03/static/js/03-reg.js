/**
 * Created by tarena on 19-5-11.
 */
/**
 * 检查用户名称是否存在的函数
 * return : 用户名称不存在返回true,存在的话返回false
 * */
function checkuname(){
  var ret = true;
  $.ajax({
    url:'/03-checkuname',
    type:'get',
    data:"uname="+$("#uname").val(),
    async:false,
    dataType:'json',
    success:function(data){
      $("#uname-tip").html(data.text);
      if(data.status == 0){
        ret = false;
      }
    }
  });
  return ret;
}

/**
 * 完成用户的注册功能
 * */
function regUser(){
  //调用checkuname,根据返回值决定是否要继续进行注册
  if(checkuname()){
    $.ajax({
      url:'/03-reguser',
      type:'post',
      data:{
        uname:$("#uname").val(),
        upwd:$("#upwd").val(),
        nickname:$("#nickname").val(),
        email:$("#email").val()
      },
      dataType:'json',
      success:function(data){
        alert(data.text);
        if(data.status == 1){
          $("#uname").val('');
          $("#upwd").val('');
          $("#nickname").val('');
          $("#email").val('');
        }
      }
    });
  }else{
    alert("用户名称已存在");
  }
}


$(function(){
  //1.为#uname绑定blur事件
  $("#uname").blur(function(){
    var uname = $("#uname").val();
    if(uname.trim().length == 0){
      $("#uname-tip").html("用户名称不能为空");
    }else{
      checkuname();
    }
  });

  //2.为#btnReg 绑定 click 事件
  $("#btnReg").click(function(){
    regUser();
  });
});














