let promptSync = require('prompt-sync')();

function Index(number) {
    let sum = 0;
    let prev = 0;
    let next = 1;

    for (let i = 0; i < number; i++) {
        sum = prev + next;
        prev = next;
        next = sum;
    };
    return (`The number at the index ${number} is ${next}`);
};

function Main() {
    try {
        console.log('Search for a number position at fibonacci sequence');
        process.stdout.write('Insert an index: ');
        let r = promptSync();
        let sender = Index(r);
        console.log(sender);
    } catch (Exception) {
        console.log('An error ocurred during the process...')
        console.log(Exception.message);
    }
};
Main();