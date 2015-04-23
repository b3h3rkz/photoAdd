var app = angular.module('app', []);

app.controller("AppCtrl", function ($http) {
    var app = this;
    app.message  = "test";


    $http.get("/api/pin").success(function (data){

        app.pins = data.objects;
});

    app.addPin = function () {

        $http.post("api/pin", {"title":"new", "image":"upload feature" + app.pins.length})
        .success (function (data)

        {

            app.pins.push(data);
        })
    }
})