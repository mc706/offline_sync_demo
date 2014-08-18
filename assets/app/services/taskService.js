app.service('TaskService', function () {
    "use strict";
    return {
        getTasks: function () {
            console.log('service called');
            return [
                {
                    'title': 'Task1',
                    'date_created': 'date',
                    'completed': false,
                    'deleted': false
                },
                {
                    'title': 'Task2',
                    'date_created': 'date',
                    'completed': false,
                    'deleted': false
                },
                {
                    'title': 'Task3',
                    'date_created': 'date',
                    'completed': true,
                    'deleted': false
                }
            ];
        }
    };
});