var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
    req.getConnection(function (err, connection) {
	console.log("Cookies: ", req.cookies);
//	console.log("Homepage");
    });

    var url = require('url');
    var url_parts = url.parse(req.url, true); 
    var query = url_parts.query;

    res.render('classpage', { id : query.id });
});

module.exports = router;
