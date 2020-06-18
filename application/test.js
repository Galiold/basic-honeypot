const geoip = require('geoip-lite')

// let ip = '::1'
let ip = '178.32.236.93'
ip = ip.split(':')
ip = ip[ip.length - 1]

console.log(ip);


let geoinfo = geoip.lookup(ip)
console.log(geoinfo === null);


// console.log(geoinfo.hasOwnProperty('country'));

console.log(geoinfo)
