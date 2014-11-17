var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var mysql = require('mysql'), myConnection = require('express-myconnection');

var index = require('./routes/index');
var users = require('./routes/users');
var loginpage = require('./routes/loginpage');
var signuppage = require('./routes/signuppage');
var signup = require('./routes/signup');
var login = require('./routes/login');
var homepage = require('./routes/homepage');
var profile = require('./routes/profile');
var classpage = require('./routes/classpage');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
//app.use(favicon(__dirname + '/public/favicon.ico'));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());

app.use(function(req,res,next){
    console.log(req.cookies);
    next();
});

app.use(express.static(path.join(__dirname, 'public')));

app.use(myConnection(mysql, {
    host: 'localhost',
    user: 'root',
    password: 'Klassmate',
    database: 'Klassmate'
}, 'single'));

app.use('/', index);
app.use('/loginpage', loginpage);
app.use('/users', users);
app.use('/signuppage', signuppage);
app.use('/signup', signup);
app.use('/login', login);
app.use('/homepage', homepage);
app.use('/profile', profile);
app.use('/classpage', classpage);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
    app.use(function(err, req, res, next) {
        res.status(err.status || 500);
        res.render('error', {
            message: err.message,
            error: err
        });
    });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
        message: err.message,
        error: {}
    });
});


var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'Klassmate'
});

connection.connect(function(err) {
  if (err) {
    console.error('error connecting: ' + err.stack);
    return;
  }

  console.log('connected as id ' + connection.threadId);
});

module.exports = app;
