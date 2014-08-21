app.service('SyncService', function ($http, $q) {
    "use strict";
    return {
        sync: function (data) {
            var defer = $q.defer();
            $http({
                method: 'POST',
                url: '/sync/',
                headers: {'Content-Type': 'application/json'},
                data: data
            }).success(function (data, status, headers, config) {
                if (status === 302) {
                    window.location('/login/');
                }
                defer.resolve(data);
            }).error(function (data, status, headers, config) {
                if (status === 302) {
                    window.location('/login/');
                }
                defer.reject(status);
            });
            return defer.promise;
        }
    };
});