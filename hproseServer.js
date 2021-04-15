var hprose = require("hprose");
const ipAddress =  require('ip');
function getIp() {
    return "ip address --> " + ipAddress.address() + "!";
}
var server = hprose.Server.create("http://0.0.0.0:8080");
server.addFunction(getIp);
server.start();