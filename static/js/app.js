'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngAnimate',
  'ngDialog',

])

.controller('myCtrl', function($scope, ngDialog){

	$scope.details = function(pid){
		ngDialog.open({ template: pid, });
	};
});