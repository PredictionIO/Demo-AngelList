'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('pioALDemo.services', ['ngResource']).
  factory('Startup', ['$resource', function($resource) {
    return $resource('http://angellist-demo.prediction.io/startups:startupId.json', {}, {
      query: {method: 'GET', params: {startupId: ''}, isArray: true, tracker: 'startups'}
    });
  }]).
  factory('SimilarStartups', ['$resource', function($resource) {
    return $resource('http://angellist-demo.prediction.io/engines/itemsim/similarstartups/topn.json', {}, {
      get: {method: 'GET', tracker: 'similarStartups'}
    });
  }]);
