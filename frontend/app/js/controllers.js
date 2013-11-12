'use strict';

/* Controllers */

angular.module('pioALDemo.controllers', []).
  controller('StartupCtrl', ['$scope', '$filter', 'Startup', 'SimilarStartups', function($scope, $filter, Startup, SimilarStartups) {
    var startupsHash = new Object();
    var startups = Startup.query(function() {
      for (var i = 0; i < startups.length; i++) {
        var id = startups[i].id;
        var name = startups[i].name;
        var url = startups[i].url;
        var markets = startups[i].markets;
        startupsHash[id] = {name: name, url: url, markets: markets};
      }
      $scope.totalItems = startups.length;
      $scope.query = "";
      $scope.incubator = "";
    });

    $scope.startups = startups;

    $scope.currentPage = 1;

    $scope.getSimilarStartups = function(startupId) {
      var similarStartupResult = SimilarStartups.get({
        pio_iid: startupId,
        pio_appkey: 'DsutdlQe8wYUmYpdyAIkI1YKxCHehUTkRPDN3SyTYPBRtjzbfeqCAgoSao8pLBJA',
        pio_n: 10,
        pio_itypes: startupsHash[startupId].markets.join()
      }, function() {
        var similarStartupIds = similarStartupResult["pio_iids"];
        var similarStartups = new Array();
        for (var i = 0; i < similarStartupIds.length; i++) {
          similarStartups.push(startupsHash[similarStartupIds[i]]);
        }
        $scope.similarStartups = similarStartups;
      });
    }

    $scope.setIncubator = function(incubator) {
      $scope.incubator = incubator;
    }

    var filterChanged = function(newQuery) {
      $scope.startups = $filter('filter')(startups, {name: $scope.query, incubator: $scope.incubator});
      $scope.currentPage = 1;
      $scope.totalItems = $scope.startups.length;
    };

    $scope.$watch('query', filterChanged);
    $scope.$watch('incubator', filterChanged);
  }]);
