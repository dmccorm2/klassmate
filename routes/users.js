var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res) {
  res.send({ user1: 'Michael Powers', user2: 'Zach Lipp'});
});

module.exports = router;
