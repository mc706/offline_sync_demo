var app = angular.module('tasks', ["ngCookies", 'ngRoute', 'xc.indexedDB', 'uuids']);

app.run(function ($http, $cookies) {
    "use strict";
    $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
});

app.config(function ($indexedDBProvider) {
    "use strict";
    $indexedDBProvider
        .connection('myIndexedDB')
        .upgradeDatabase(1, function (event, db, tx) {
            var objStore = db.createObjectStore('tasks', {keyPath: 'uuid'});
            objStore.createIndex('title_idx', 'title', {unique: false});
            objStore.createIndex('completed_idx', 'completed', {unique: false});
            objStore.createIndex('deleted_idx', 'deleted', {unique: false});
            objStore.createIndex('timestamp_idx', 'timestamp', {unique: false});
        });
});

app.config(function ($routeProvider) {
    'use strict';
    console.log('routes setup');
    $routeProvider
        .when('/', {
            controller: 'TaskController',
            templateUrl: '/static/app/views/home.html',
            resolve: {
                tasks: function (TaskService) {
                    return TaskService.getTasks();
                }
            }
        })
        .when('/tasks', {
            controller: 'TaskController',
            templateUrl: '/static/app/views/tasks.html',
            resolve: {
                tasks: function (TaskService) {
                    return TaskService.getTasks();
                }
            }
        })
        .when('/tasks/new', {
            controller: 'TaskController',
            templateUrl: '/static/app/views/task-new.html',
            resolve: {
                tasks: function () {
                    return false;
                }
            }
        })
        .otherwise({
            redirectTo: '/'
        });
});
