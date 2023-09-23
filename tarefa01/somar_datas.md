a) O conjunto de entradas são: a data inicial e o número de dias que se deseja somar a esta data inicial. Sendo o conjunto de saida a data inicial somada ao numero de dias desejado e compatível com o formato padrão de nosso calendário.

b) 
Pergunte uma data inicial (no formato dd/mm/aaaa) e anote, 
sendo "dd" pertencente ao conjunto dos números naturais e esteja de acordo com as seguintes limitações:
0<dd<32 se "mm" = 3,5,7,8,10,12 ou 0<dd<31 se mm = 4,6,9,11 ou 0<dd<29 se mm = 2
e 0<mm<13;

Pergunte um número de dias (que faça parte do conjunto dos números inteiros) e anote;

Pegue o valor "dd" obtido de "data inicial" e some com o valor obtido em "numero de dias"
se o dd obtido no resultado superar o valor limite imposto, adicionar 1 em mm até que as limitações sejam respeitadas, se mm obtido superar o limite imposto adicione 1 em aaaa até que mm se enquadre nas limitações impostas novamente;

Se o dd obtido no resultado for inferior ao valor limite imposto, subtrair 1 em mm até que as limitações sejam respeitadas, se mm obtido for inferior ao limite imposto, subtraia 1 em aaaa até que mm se enquadre nas limitações impostas novamente;

Devolva um resultado no formato (dd/mm/aaaa) que se todas as instruções foram seguidas corretamente estará de acordo com o formato do calendário gregoriano.


