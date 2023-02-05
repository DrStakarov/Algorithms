// N = ESTUDANTES
// D = MILILITROS POR ESTUDANTES
// L = CAPACIDADE DA GARRAFA EM LITROS

function myCoffe (n, l, d) {
    let calc = ((n*d) /1000);
    let output = l;

    while(calc > output) {
        output+=l
    }
    console.log(output)
}

myCoffe(8, 5, 2000)