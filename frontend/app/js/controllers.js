'use strict';

/* Controllers */

angular.module('pioALDemo.controllers', []).
  controller('StartupCtrl', ['$scope', 'Startup', 'SimilarStartups', function($scope, Startup, SimilarStartups) {
    var startupsHash = new Object();
    var startups = Startup.query(function() {
      for (var i = 0; i < startups.length; i++) {
        var id = startups[i].id;
        var name = startups[i].name;
        var url = startups[i].url;
        startupsHash[id] = {name: name, url: url};
      }
      $scope.totalItems = startups.length;
    });

    $scope.startups = startups;

    $scope.currentPage = 1;

    $scope.getSimilarStartups = function(startupId) {
      var similarStartupResult = SimilarStartups.get({
        pio_iid: startupId,
        pio_appkey: 'QOxO1EGRYzfmTROjKFpkVVHLxy13EOak7GSfDdvcwxR2ukc8UuvrH3u5GWJS07er',
        pio_n: 10
      }, function() {
        var similarStartupIds = similarStartupResult["pio_iids"];
        var similarStartups = new Array();
        for (var i = 0; i < similarStartupIds.length; i++) {
          similarStartups.push(startupsHash[similarStartupIds[i]]);
        }
        $scope.similarStartups = similarStartups;
      });
    }
  }]);
