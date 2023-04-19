/*

&& -> Todas as expressãoes precisam ser verdadeiras para que o AND retorne true.
|| -> Todas as expressões precisam ser falsas para que o OR retorne false. Retorna o valor falso e se for true ele retorna a ultima expressão.

A partir do momento que uma expressão dentro da expressão ela vai retornar false e nada mais vai ser checado isso e isso se chama short-circuit. 

*/

console.log('Luiz' && 0 && 'Maria'); // Retorna 0. Quando o AND encontra uma expressão que avalia em falso ele vai retornar o valor falso. 

console.log('Luiz' && true && 'Maria'); // Quando a expressão é verdadeira ele retorna o ultimo valor: 'Maria'.