# Otimization

Os problemas de otimização são muitas vezes de maximização ou de minimização. O conjunto de estados possíveis para um problema é finito embora possa ser muito grande, pelo que a pesquisa total é impossível: recorre-se à aproximação. Exemplos de algoritmos:
- Knapsack Problem;
- Travelling Salesman Problem (TSP);
- COP - Combinatorial Optimization Problem;

Para os problemas de otimização normalmente usa-se a **vizinhança** de modo a poder saltar de solução em solução para tentar atingir um ótimo local. Para fugir do ótimo local é necessário usar outro tipo de mecanismos, como remover um elemento da solução, adicionar um elemento na solução ou trocar elementos da sua ordem original. Um ótimo global é também um ótimo local no que diz respeito à sua vizinhança. É importante definir um critério de paragem.

- `Best accept`: seleciona o melhor vizinho da vizinhança;
- `Fist accept`: seleciona o primeiro melhor vizinho;

No entanto estes dois algoritmos acabam por ficar presos num `ótimo local`, pois param quando não encontram nenhum melhoramento próximo. Para isso usam-se as meta-heurísticas. Pode ser um **random descent** quando selecionamos uma solução vizinha aleatória ou um **random walk** quando adquirimos o estatuto da solução vizinha aleatória.

### Classificação de Meta-heurísticas X/Y/Z

`X` -> se têm memória (A) ou não (M)
`Y` -> random (S) ou pesquisa por vizinhos (N)
`Z` -> uma única solução (1) ou um conjunto de soluções que representam uma população (P)

Os algoritmos mais utilizados são:
- Simulated Annealing;
- Iterated Local Search;
- Tabu Search;
- Genetic Algorithms;

### Arrefecimento Simulado

- Escolha de um vizinho aleatório;
- Os movimentos de melhoria são sempre aceites;
- Os movimentos de pioria são aceites com probabilidade que varia de acordo com a quantidade de deteorioração da solução e a temperatura;
- A capacidade de mudar para uma situação pior diminui com o tempo;
- Pode ser necessário fazer várias iterações e recomeçar o algoritmo. Se a pesquisa for determinística então não vale a pena;

### Iterated Local Search

Há uma perturbação grande no espaço de estados e vizinhança, pelo que o sistema passa a reconhecer um novo ótimo local independente do anterior. Define um conjunto de soluções admissíveis.

### Tabu Search

Permite movimentos que não melhoram a solução e usa memória extra para diversificar a pesquisa. Movimentos dentro da memória tabu não podem ser escolhidos durante X jogadas, embora possam sê-lo se melhorarem drasticamente a situação: critério de aspiração. Permite até que se mova para uma zona que piora a solução, dado um critério mais extenso e demorado. 

### Genetic Algorithms

- Mutações: troca e inversão de cromossomas. Movimenta o espaço de pesquisa e pode reavivar informações sobre a população entretanto perdidas;
- Crossover: operação binária de recombinação que retira partes de um cromossoma e de outro cromossoma;

Aqui a população mais eficiente e que arranja melhores soluções acaba por dominar e prevalecer para as gerações futuras, tal como acontece com a Natureza. Os pais podem ser escolhidos por torneio (aleatório, serve para reproduzir mais rapidamente a população), ou pela roleta, que tem fatias de acordo com o valor relativo da população. 