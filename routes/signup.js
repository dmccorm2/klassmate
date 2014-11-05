var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
    req.getConnection(function (err, connection) {
	console.log(connection);
    });
    res.render('signup');
});

router.post('/', function(req, res) {
    req.getConnection(function (err, connection) {
        var response=req.body;
	console.log(response['user']);
	connection.query('insert into user values',  function(err, result) {
	    if (err) console.log(err);

	    console.log(result);
	});
	
    });
    res.render('signup');
});
module.exports = router;
