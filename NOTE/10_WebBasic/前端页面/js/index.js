$(function (){
	//轮播图
	var index = 0;//下标
	var timer;//保存定时器ID
	timer = setInterval(autoPlay,1000);
	function autoPlay(){
		//当前显示的图片隐藏/修改索引背景色
		$("#banner img").eq(index).css("display","none");
		$("#banner li").eq(index).css("background","green");
		//下标后移
		index = ++index == $("#banner img").length ? 0 : index;
		//下一张图片显示/修改索引背景色
		$("#banner img").eq(index).css("display","block");
		$("#banner li").eq(index).css("background","blue");

	}
	//鼠标移入移出
	$("#banner").mouseover(function (){
		//停止定时器
		clearInterval(timer);
	});
	$("#banner").mouseout(function (){
		//重启定时器
		timer = setInterval(autoPlay,1000);
	});
	//点击切图
	$("#banner .left").click(function (){
		$("#banner img").eq(index).css("display","none");
		$("#banner li").eq(index).css("background","green");
		//切换前一张图
		index--;
		if(index < 0){
			index = $("#banner img").length -1;
		}
		//切换样式
		$("#banner img").eq(index).css("display","block");
		$("#banner li").eq(index).css("background","blue");
	});
	$("#banner .right").click(function (){
		//当前显示的图片隐藏/修改索引背景色
		$("#banner img").eq(index).css("display","none");
		$("#banner li").eq(index).css("background","green");
		//下标后移
		index = ++index == $("#banner img").length ? 0 : index;
		//下一张图片显示/修改索引背景色
		$("#banner img").eq(index).css("display","block");
		$("#banner li").eq(index).css("background","blue");
	});


});