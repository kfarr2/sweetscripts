
var page = require('webpage').create();
var system = require('system'), address;
if(system.args !== null){
    address = system.args[1];
    if(address.search('http://') === -1){
        address = 'http://' + address;
    }
}
page.viewportSize = { width: 1000, height: 800 };
page.open(address, function() {
    page.render('page.png');
    phantom.exit();
});

