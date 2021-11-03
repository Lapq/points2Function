# points2Function
Classe python que computa a função de uma reta e sua inversa, dado uma entrada de 2 pontos de coordenadas 2d

Pode ser instanciado com a entrada dos valores float de x e y do primeiro ponto, e os valores de x e y do segundo (todos separadamente, não é compatível com arrays e similares).
Ou pode ser instanciado sem argumentos, e são setados os valores posteriormente com .setPoints seguindo a mesma estrutura descrita acima.
Mesmo em caso de já ter setado os pontos, pode-se setar novos.

Após os pontos serem setados, compute o Y de algum valor X qualquer de sua escolha usando o método "function".
Ou se quiser a computação da função inversa, compute o X de algum valor Y qualquer de sua escolha usando o método "inverse".
