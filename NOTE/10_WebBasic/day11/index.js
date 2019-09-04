function $(tagName,index){
	if(index){//index非零时
		var elem = document.getElementsByTagName(tagName)[index];

	}else{ //index==undefined index == 0
		var elem = document.getElementsByTagName(tagName)[0];
	}
	return elem;
} 
