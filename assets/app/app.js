var app = angular.module('tasks', ['ngRoute']);

app.config(function ($routeProvider) {
    'use strict';
    console.log('routes setup');
    $routeProvider
        .when('/', {
            controller: 'TaskController',
            templateURL: '/static/app/views/home.html',
            resolve: {
                tasks: function (TaskService) {
                    return TaskService.getTasks();
                }
            }
        })
        .when('/edit', {
            controller: 'TaskController',
            templateURL: 'editor.html'
        })
        .otherwise({
            redirectTo: '/'
        });
});

