(function(){

	'use strict';

	angular.module('app.auth')
	.factory('authService',authService);

	function authService(authorization){

	var service = {
      firebaseAuthObject: firebaseAuthObject,
      register: register,
      login: login,
      logout: logout,
      isLoggedIn: isLoggedIn,
      sendWelcomeEmail: sendWelcomeEmail
    };

	return service;

	function register(){

	}

	function logout(){

	}

    function sendWelcomeEmail(emailAddress) {
      
     }
 }
      
})();