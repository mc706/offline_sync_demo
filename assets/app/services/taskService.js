app.service('TaskService', function ($indexedDB, rfc4122) {
    "use strict";
    var OBJECT_STORE_NAME = 'tasks',
        myObjectStore = $indexedDB.objectStore(OBJECT_STORE_NAME);

    return {
        getTasks: function () {
            return myObjectStore.getAll();
        },
        createTask: function (title) {
            var uuid = rfc4122.newuuid(),
                timestamp = Date.now();
            return myObjectStore.insert({
                uuid: uuid,
                title: title,
                completed: false,
                deleted: false,
                timestamp: timestamp
            });
        },
        updateTask: function (data) {
            data.timestamp = Date.now();
            return myObjectStore.upsert(data);
        },
        deleteTask: function (data) {
            return myObjectStore.delete(data.uuid);
        }
    };
});