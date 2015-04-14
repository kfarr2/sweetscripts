
var page = require('webpage').create();
var system = require('system'), address;
if(system.args !== null){
    address = system.args[1];
    if(address.search('http://') === -1){
        address = 'http://' + address;
    }
}
page.viewportSize = { width: 800, height: 500 };
page.open(address, function() {

    var name = 'konstantin/static/img/screenshots/'+ address.substring(address.lastIndexOf("//")+2, address.lastIndexOf("/")) + '.png';
    page.render(name);
    phantom.exit();
});

