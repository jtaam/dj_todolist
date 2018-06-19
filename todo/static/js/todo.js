var app = angular.module('toDo',[]);
app.controller('toDoController', function($scope, $http){
    // $scope.todoList = [{todoText: 'finish this app', done:false}];
    $http.get('/todo/api/').then(function (response) {
        $scope.todoList = [];
        for (var i = 0; i < response.data.length; i++){
            var todo = {};
            todo.id = response.data[i].id
            todo.todoText = response.data[i].todo_text
            todo.done = response.data[i].todo_done
            $scope.todoList.push(todo);
        }
        console.log(response.data);
    });
    $scope.todoAdd = function () {
      $scope.todoList.push({todoText:$scope.todoInput, done:false});
      $scope.todoInput = '';
    };
    $scope.remove = function () {
        var oldList = $scope.todoList;
        $scope.todoList = [];
        angular.forEach(oldList, function (todo) {
            if (todo.done){
                $http.delete('/todo/api/'+todo.id+'/');
            } else {
                $scope.todoList.push(todo);
            }
        })
    }
})