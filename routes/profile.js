var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
    req.getConnection(function (err, connection) {
	console.log("Cookies: ", req.cookies);
//	console.log("Homepage");
    });
    res.render('profile');
});

module.exports = router;
