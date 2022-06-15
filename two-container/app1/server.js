'use strict';

const express = require('express');

const PORT = 8080;
const HOST = '0.0.0.0';

const app = express();
app.get('/', (req, res) => {
    let date_ob = new Date();
    res.send(date_ob.getMilliseconds() + '_' + date_ob.getUTCMilliseconds());
});

app.listen(PORT, HOST);
