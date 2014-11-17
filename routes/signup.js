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

/*
* 
*   Make sure we check the input to make sure everything is clean
*
*/

//	console.log(response);
	connection.query('insert into user(name, email, password, professor) values(?, ?, ?, 0)', [response['name'], response['email'], response['pass']], function(err, result) {
	    if (err) console.log(err);

	    console.log(result);
	});
	
    });
    res.render('signup');
});
module.exports = router;
