var app = angular.module('tasks', ['ngRoute']);

app.config(function ($routeProvider) {
    'use strict';
    console.log('routes setup');
    $routeProvider
        .when('/', {
            controller: 'TaskController',
            templateURL: '/static/app/views/home1.html',
            resolve: {
                tasks: function (TaskService) {
                    console.log('resolving tasks');
                    return TaskService.getTasks();
                }
            }
        })
        .otherwise({
            redirectTo: '/'
        });
});

