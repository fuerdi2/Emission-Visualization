var express = require("express"); //加载express模块
var fs = require("fs");
var application = express();
var server = require("http").createServer(application); //请求http模块并且使得回调函数为application(express())
var io = require("socket.io").listen(server); //socket监听
var interval = -1;
server.listen(8080);
application.use(express.static(__dirname));
io.sockets.on("connection", function() {
            if (interval < 0) {
                interval = setInterval(function() { 
                	console.log("I am working");
                    var results = {}
                    var obj = JSON.parse(fs.readFileSync('baidumap_Gym.json', 'utf8')); 
                    results.data = obj.data;
                    results.NoX = obj.NoX;
                    io.sockets.emit("transmit", results);
                    }, 3000);
        }
    }
        );

console.log("computer performance server running");
