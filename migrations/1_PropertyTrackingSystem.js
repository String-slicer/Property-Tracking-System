const PropertTrackingSystem=artifacts.require('PropertyTrackingSystem');

module.exports=function(deployer){
    deployer.deploy(PropertTrackingSystem);
}