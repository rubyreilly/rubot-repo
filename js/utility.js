$.fn.clearHistory = function(){
	$('#executed-command-list').empty().append("<li>Started robot</li>");
}

$.fn.trackHistory = function(item){
	$('#executed-command-list').append("<li>"+item+"</li>");
}
