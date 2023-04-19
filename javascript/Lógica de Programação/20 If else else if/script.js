/*
Entre 0 - 11 - Bom dia
Entre 12 - 17 - Boa Tarde
entre 18 - 23 - Boa noite
*/

// If pode ser executado sozinho
// O else e else if só pode ser adicionado depois de um If
// Posso ter varios else ifs checagem
// If e Else só podemos ter um.


const hora = 10;

if (hora >= 0 && hora < 12) {
    console.log('Bom dia!');
} else if (hora >= 12 && hora <= 17) {
    console.log('Boa tarde!');
} else if (hora >= 17 && hora <= 23) {
    console.log('Boa noite!')
} else {
    console.log('Olá!');
}