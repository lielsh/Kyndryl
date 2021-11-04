const axios = require('axios');
const readlineSync = require('readline-sync');

let flag = true;
const server = 'http://localhost:5000/';

(async () => {
    while(flag) {

        const menu = readlineSync.question('\nPlease enter a number:\n 1. Add a new user\n 2. Show all users\n 3. Exit\n').trim();

        switch(menu) {
    
            case '1':
                const user = readlineSync.question('\nPlease enter an ID number, first and last name\n').trim().replace(/\s+/g, ' ');

                if (
                    user.split(' ').length !== 3
                    || Number.isNaN(parseInt(user.split(' ')[0]))
                    || !user.split(' ')[1].match(/^[A-Za-z]+$/)
                    || !user.split(' ')[2].match(/^[A-Za-z]+$/)) {

                    console.log('\nInvalid input!');
                }

                else {
                    await axios({
                        url: server,
                        method: 'POST',
                        data: { 'id': parseInt(user.split(' ')[0]), 'first': user.split(' ')[1], 'last': user.split(' ')[2] }
                    })
                    .then(res => console.log(`\n${res.data.message}`))
                    .catch(err => console.log(`\n${err}`));
                }

                break;
    
            case '2':
                await axios({
                    url: server,
                    method: 'GET'
                })
                    .then(res => console.log(`\nID\tFirst Name\tLast Name\n${res.data.users.map(elem => `${elem[0]}\t${elem[1]}\t\t${elem[2]}\n`)}`.replace(/\,/g, '')))
                    .catch(err => console.log(`\n${err}`));
                    
                break;
            
            case '3':
                flag = false;
                console.log('\nBye-Bye!');
                break;
            
            default:
                console.log('\nInvalid input!');
                break;
        }
    }
})();