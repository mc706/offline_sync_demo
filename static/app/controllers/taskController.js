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
        TaskService.updateTask(task, true);
    };

    $scope.deleteTask = function (task) {
        task.deleted = true;
        TaskService.updateTask(task, true);
    };

    $scope.sync = function () {
        var newly;
        SyncService.sync($scope.tasks).then(function (data) {
            angular.forEach(data.deleted, function (del) {
                console.log('deleting:', del);
                TaskService.deleteTask(del);
            });
            angular.forEach(data.tasks, function (task) {
                newly = false;
                angular.forEach($scope.tasks, function (t) {
                    if (t.uuid === task.uuid && task.timestamp > t.timestamp) {
                        console.log('updating:', task.uuid);
                        newly = true;
                        TaskService.updateTask(task, false);
                    }
                    if (t.uuid === task.uuid) {
                        newly = true;
                    }
                });
                if (!newly) {
                    console.log('creating locally:', task.uuid);
                    TaskService.updateTask(task, false);
                }
            });
        });
        TaskService.getTasks().then(function (data) {
            $scope.tasks = data;
        });

        $timeout($scope.sync, 5000);
    };

    $timeout($scope.sync, 1000);

});