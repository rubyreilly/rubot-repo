// This is the init function for all the JQuery effects

$.fn.addEffects = function(){
	$.fn.addOnHover();
	$.fn.addOnMouseOver();
	$.fn.addOnClick();
	$.fn.addStop();
}

$.fn.addOnHover = function(){
	$('.hover-area').on('mouseenter', function(){
		$.fn.chooseDirection($(this).attr('id'));
	});
/*
	$('.hover-area').on('mouseleave', function(){
		$.fn.stopMotion();
	});
*/
}

$.fn.addOnMouseOver = function(){

	$('.hover-area').on('mouseover', function(){
		$.fn.chooseDirection($(this).attr('id'));
	});
	/*
	$('.hover-area').on('mouseleave', function(){
		if(!window.sticky){
			$.fn.stopMotion();
		}
	});*/
}

$.fn.addOnClick = function(){
	$('.hover-area').on('mousedown', function(){
		$.fn.chooseDirection($(this).attr('id'));
	});
	/*
	$('.hover-area').on('mouseup', function(){
		$.fn.stopMotion();
	}); */
}

$.fn.chooseDirection = function(direction){
	switch(direction){
		case 'top': $.fn.moveForward();break;
		case 'right': $.fn.rotateRight();break;
		case 'bottom': $.fn.moveBackward();break;
		case 'left': $.fn.rotateLeft();break;
	}
}


$.fn.moveForward = function(){
	if(window.currentDirection != 'forward'){ // !window.moving){
		//console.log('moving forward');
		$.fn.trackHistory("Moved forward");
		window.moving = true;
		window.currentDirection = 'forward';
		xml_http_post("web/index.html", "forward", req_handler);
	}
}

$.fn.moveBackward = function(){
	if(window.currentDirection != 'backward'){ // !window.moving){
		//console.log('moving backward');
		$.fn.trackHistory("Moved backward");
		window.moving = true;
		window.currentDirection = 'backward';
		xml_http_post("web/index.html", "backward", req_handler);
	}
}
$.fn.rotateRight = function(){
	if(window.currentDirection != 'right'){ // !window.moving){
		$.fn.trackHistory('rotating right');
		window.moving = true;
		window.currentDirection = 'right';
		xml_http_post("web/index.html", "CW", req_handler);
	}
}

$.fn.rotateLeft = function(){
	if(window.currentDirection != 'left'){ // !window.moving){
		$.fn.trackHistory('rotate left');
		window.moving = true;
		window.currentDirection = 'left';
		xml_http_post("web/index.html", "CCW", req_handler);
	}
}

$.fn.stopMotion = function(){
	if(window.moving){
		$.fn.trackHistory('motion halted!');
		window.moving = false;
		window.currentDirection = 'none';
		xml_http_post("web/index.html", "stop", req_handler);
	}
}

$.fn.addStop = function(){
	$('#hault_section').on('click',function(){
	$.fn.trackHistory('stopped motion');
		$.fn.stopMotion();
	});
}
