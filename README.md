# Sudoku

## Como vai ser a modelagem / testes

## Descrição do trabalho

O próximo trabalho será a resolução do sudoku usando os algoritmos genético e hillclimbing.

Entrada: o tabuleiro de entrada está em anexo.
Saida: a solução (se for possível encontrá-la :-))

O trabalho consiste em:

- modele o problema para que ele possa ser resolvido usando 

  a - hillclimbing 
    - defina como será representado uma configuração do tabuleiro
    - qual será a função heurística usada

  b - AG
    - como serão representados os indivíduos
    - qual será a função de adaptação usada

- Experimentos - hillclimbing

Neste experimento você deve gerar aleatoriamente uma configuração e aplicar o hillclimbing até que o programa não consiga melhorar a função heurística que você escolheu.
Quando isso ocorrer, o programa deve parar, salvando como ficou o tabuleiro e o valor da função heurística.
Como você pode não encontrar a solução em uma execução do algoritmo, você deve definir quantas vezes este experimento deve ser repetido.
Os resultados obtidos devem ser analisados. 

- Experimentos - AG

Neste experimento, você deve definir os parâmetros dos AGs :
- probabilidade de crossover e mutação
- tamanho da população
- critério de parada (número de gerações ou estabilidade da população)
- utilização ou não de elitismo

Note que o desempenho do AG depende da escolha de tais parâmetros. Portanto, várias combinações de parâmetros devem ser usadas. Ao final de cada execução, deve ser guardado o melhor indivíduo gerado.
Aqui também, os resultados obtidos devem ser analisados.

O trabalho deve ser feito em grupos de 3 (18 alunos -> 6 grupos).

Os resultados serão apresentados na aula do dia 4/2. Cada grupo terá no máximo 15 minutos para apresentar os seus resultados. As apresentações devem ser enviadas, depois da aula do dia 4/2, para a lista de discussão. Não esqueçam de colocar as referências (dos artigos e/ou programas) usadas.

## Como deve ser a apresentação

Primeiro Slide:

 - Representacao:

Hill -> como tabuleiro tá representado?

AG -> como tab tá representado?

 - Função:

Hill -> como tá a função? MAX ou MIN?

AG -> mesma coisa

Segundo Slide

Exp Hill Clibing

- Número de tabuleiros vc gerou? # de buscas
- Qual critério de parada?
- Quantas vezes achou o resultado ótimo?
- Quantas vezes não achou?
- Explicar: achou alguma vez? Quanto demorava? A representação tá ruim?
- Fazer uma análise.

**Não é bizarro não achar nunca a solução ótima. Mas tem que explicar o porque vc acha que não achou.**

Terceiro Slide

Alg Genético

- Mesma coisa, mas tem que explicar os parâmetros.

Pode fazer um gráfico de conjunto de parâmetros e do melhor individuo para mostrar o aumento da qualidade do Alg para cada conjunto.

A nota depende da qualidade dos exemplos.

Fechar a modelagem e perguntar para ele.

Anotar as referências e apontar para as biografias

Registrar os dados dos testes(quantos, quais?)

Não botar código, a não ser que vc garanta que esteja visível

E também as pessoas não vão entender provavelmente

Usar PDF pois garante abrir em qualquer lugar

Não conte com a internet
