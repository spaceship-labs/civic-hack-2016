(function(){
	'use strict';
	angular.module('app.auth')
	.controller('authController', authController);

	AuthController.inject = ['authService','$state'];

	function AuthController(authService){
		var vm = this;

	function register(){
			return authService.register(authorization).then(function(){
				return //vm.login.user;
			})
			.then(function() {
          	return authService.sendWelcomeEmail();
        	})
        	.catch(function(error) {
          	//vm.error = error;
        	});
		}
	}

	function login(user) {
      return authService.login(user)
        .then(function() {
          $location.path('/denuncias');
        })
        .catch(function(error) {
          vm.error = error;
        });
    }
})