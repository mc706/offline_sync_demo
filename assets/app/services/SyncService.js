app.service('SyncService', function ($indexeddb) {
    "use strict";
    return {
        getTasks: function () {
            console.log('service called');
            return [
                {'title': 'this is a task'},
                {'title': 'this is a task'},
                {'title': 'this is a task'},
                {'title': 'this is a task'}
            ];
        }
    };
});