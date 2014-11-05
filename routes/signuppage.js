var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
    req.getConnection(function (err, connection) {
        connection.query('select * from user', function(err,results) {
            if (err) console.log(err);

            console.log(results);
        });
    });
    res.render('signuppage');
});

module.exports = router;
