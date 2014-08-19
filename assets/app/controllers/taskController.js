app.controller('TaskController', function ($scope, $location, $timeout, TaskService, tasks) {
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

});