// sign up and login page

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add('right-panel-active');
});

signInButton.addEventListener('click', () => {
	container.classList.remove('right-panel-active');
});


// ----- code for form validation ------


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