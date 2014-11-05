var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
    req.getConnection(function (err, connection) {
	console.log("get why");
    });
    res.render('login');
});

router.post('/', function(req, res) {
    var response=req.body;
    req.getConnection(function (err, connection) {
//	var query = "select * from user where name=?", [response['name']];
	console.log(response);
//	console.log(query);
	connection.query('select * from user where email = ?', [response['user']],  function(err, results){
//	connection.query('select getPassword(?)', [response['user']],  function(err, results){ 
            if (err) {
		console.log(err);
	    } else {

		console.log(results);
		console.log(response);
		console.log(response['pass']);
		console.log(results[0]['password']);
		if (response['pass'] == results[0]['password']){
		    console.log("successful login");
		} else {
		    console.log("permission denied");
		}
	    }
        });
    });
    res.render('login', );
});

module.exports = router;
