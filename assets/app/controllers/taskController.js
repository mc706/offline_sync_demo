app.controller('TaskController', function ($scope, $location, $timeout, TaskService, SyncService, tasks) {
    "use strict";

    $scope.tasks = tasks;

    $scope.addTask = function () {
        TaskService.createTask($scope.newTask);
        $scope.tasks = TaskService.getTasks();
        $scope.newTask = "";
        $timeout(function () {
            $location.path('/tasks');
        }, 400);
    };

    $scope.toggleComplete = function (task) {
        console.log(task);

        task.completed = !task.completed;
        TaskService.updateTask(task);
    };

    $scope.deleteTask = function (task) {
        task.deleted = true;
        TaskService.updateTask(task);
    };

    $scope.sync = function () {
        var matched;
        SyncService.sync($scope.tasks).then(function (data) {
            angular.forEach(data, function (task) {
                matched = false;
                angular.forEach($scope.tasks, function (t) {
                    if (t.uuid === task.uuid && task.timestamp > t.timestamp) {
                        matched = true;
                        TaskService.updateTask(task);
                    }
                });
                if (!matched) {
                    TaskService.updateTask(task);
                }
            });
        });
        TaskService.getTasks().then(function (data) {
            $scope.tasks = data;
        });

        $timeout($scope.sync, 60000);
    };

    $timeout($scope.sync, 1000);

});