'use strict';

/* Filters */

angular.module('pioALDemo.filters', []).
  filter('startFrom', [function() {
    return function(input, start) {
      start = +start; //parse to int
      return input.slice(start);
    }
  }]);
