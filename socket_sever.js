var express = require("express");//加载express模块
var fs = require("fs")
var application = express();
var server = require("http").createServer(application);//请求http模块并且使得回调函数为application(express())
var io = require("socket.io").listen(server);//socket监听
var interval = -1;
var baseState = Number(fs.statSync("./googledata.json").mtime)-1;
function getdata(s){
	data = require(s);
	return(data);
}
server.listen(8080);
application.use(express.static(__dirname));
io.sockets.on("connection",function(){
	if(interval<0){

		interval = setInterval(function(){
			
			var recentState = fs.statSync("./googledata.json").mtime
			if(recentState>baseState==true){
				baseState = recentState;
				var results = {}
			    var obj = JSON.parse(fs.readFileSync('googledata.json', 'utf8'));
			    results.data = obj.data
				
				console.log(results);
			io.sockets.emit("transmit",results);
		}
		},500);
	};
});

console.log("computer performance server running");