$(function (){
	//1.全选和取消全选
	var isChecked = false;
	//2.1自定义属性，为图片添加标签属性
	$(".check").prop("checked",false);
	$(".checkall").click(function (){
		isChecked = !isChecked;
		if(isChecked){
			$(this).attr("src","../images/cart/product_true.png");
			//修改商品自身的checked属性
			$(".check").prop("checked",true);
			$(".check").attr("src","../images/cart/product_true.png");
		}else{
			$(this).attr("src","../images/cart/product_normal.png");
			//修改商品自身的checked属性
			$(".check").prop("checked",false);
			$(".check").attr("src","../images/cart/product_normal.png");
		}
		total();
	});
	//2.反选
	
	//2.2添加单击事件，自身图片修改，判断是否实现全选
	$(".check").click(function (){
		//修改自身的checked属性
		var flag = !$(this).prop("checked");
		$(this).prop("checked",flag);
		//自身图片修改
		if($(this).prop("checked")){
			$(this).attr("src","../images/cart/product_true.png");
		}else{
			$(this).attr("src","../images/cart/product_normal.png");
		}
		//反选
		var i = 0;
		$(".check").each(function (){
			if($(this).prop("checked") == false){
				//return
			}else{
				i++;
			}
		});
		//被选中的商品数量等于数组长度->全选
		//未被选中的商品数量为0->全选
		if(i == $(".check").length){
			//全选
			$(".checkall").attr("src","../images/cart/product_true.png");
			isChecked = true;
		}else{
			//未全选
			$(".checkall").attr("src","../images/cart/product_normal.png");
			isChecked = false;
		}
		total();
	});
	//3.数量加减 $(".count a").eq(1)
	$(".add").click(function (){
		//获取前一个兄弟元素(input)
		var value = $(this).prev().val();
		$(this).prev().val(++value);
		//总价联动
		//获取单价
		var str = $(this).parents(".content").find(".price span").html();
		//去掉人民币符号
		var price = str.substring(1);
		//计算后显示到总价
		$(this).parents(".content").find(".sum").html("￥"+value*price);
		total();
	});
	$(".minus").click(function (){
		//获取后一个兄弟元素(input)
		var value = $(this).next().val();
		if(value > 1){
			value--;
		}
		$(this).next().val(value);
		//价格联动
		//获取单价
		var str = $(this).parents(".content").find(".price span").html();
		//去掉人民币符号
		var price = str.substring(1);
		//计算后显示到总价
		$(this).parents(".content").find(".sum").html("￥"+value*price);
		total();
	});
	//4. 移除
	$(".content .action").click(function (){
		$(this).parents(".content").remove();
		total();
	});
	//5. 被选中的商品总数量和总价格计算
	function total(){
		var sum = 0;//总价
		var num = 0;//数量
		$(".check").each(function (){
			if($(this).prop("checked") == true){
				//数量累加，总价累加
				num += Number($(this).parents(".content").find(".count input").val());
				var str = $(this).parents(".content").find(".sum").html();
				var price = Number(str.substring(1));
				sum += price;
			}
		});
		//修改显示
		$(".total .total-sum").html(sum+"元");
		$(".total .total-num").html(num);
	}


});