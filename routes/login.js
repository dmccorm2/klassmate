var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
    req.getConnection(function (err, connection) {
	console.log("get why");
    });
    res.render('loginpage');//when url /login in search bar
});

router.post('/', function(req, res) {
    var response=req.body;
    req.getConnection(function (err, connection) {
	console.log(response);
	connection.query('select * from user where email = ?', [response['user']],  function(err, results){
            if (err) {
		console.log(err);
	    } else {

//		console.log(results);
//		console.log(response);
//		console.log(response['pass']);
//		console.log(results[0]['password']);
		if (response['pass'] == results[0]['password']){
//		    console.log("successful login");
		    res.cookie('user_id', results[0]['user_id']);
		    res.redirect("/homepage");
//		    res.render('homepage', {result: 'Succesful login'});
//		    res.redirect("/homepage");
		} else {
//		    console.log("permission denied");
		    res.render('loginpage', {result: 'Login failed'});
		}
	    }
        });
    });
});

module.exports = router;
