const email = require('emailjs')
 

const client = email.server.connect({
    user: 'goldani.ali@gmail.com',
    password: 'emu2.twang',
    host: 'smtp.gmail.com',
    ssl: true,
});
 
// send the message and get a callback with an error or details of the message that was sent
client.send(
    {
        text: 'Another test',
        from: 'no-reply@galiold.ir',
        to: 'ali.goldani97@gmail.com',
        subject: 'testing emailjs',
    },
    (err, message) => {
        console.log(err || message);
    }
);