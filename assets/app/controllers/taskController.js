app.controller('TaskController', function ($scope, tasks) {
    "use strict";
    console.log('controller called');
    $scope.tasks = tasks;
    console.log($scope.tasks);

});