// contact form js


$(document).ready(function() {
	$(".input").click(function() {
		$(this).css({border: '1px solid #b71c1c'});
	});

	$(".input").blur(function() {
		$(this).css({border: 'none'});
	});

});


function isAlphabet(elem, helperMsg) {
    var alphaExp = /^[a-zA-Z]+$/;    //use forward slashes and not string since JS syntax for regex is forward slash
    if(elem.value.match(alphaExp)) {
        return true;
   	}
	else {        
		alert(helperMsg);       
		elem.focus();
    	return false;
    }
}

function emailValidator(elem, helperMsg) {
    var emailExp = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
	if(elem.value.match(emailExp)) {
        return true;
    }
    else {
        alert(helperMsg);
        elem.focus();
		return false;
   	}
}

