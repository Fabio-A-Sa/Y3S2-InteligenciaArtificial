# Otimization

Os problemas de otimização são muitas vezes de maximização ou de minimização. O conjunto de estados possíveis para um problema é finito embora possa ser muito grande, pelo que a pesquisa total é impossível: recorre-se à aproximação. Exemplos de algoritmos:
- Knapsack Problem;
- Travelling Salesman Problem (TSP);
- COP - Combinatorial Optimization Problem;

Para os problemas de otimização normalmente usa-se a **vizinhança** de modo a poder saltar de solução em solução para tentar atingir um ótimo local. Para fugir do ótimo local é necessário usar outro tipo de mecanismos, como remover um elemento da solução, adicionar um elemento na solução ou trocar elementos da sua ordem original. Um ótimo global é também um ótimo local no que diz respeito à sua vizinhança. É importante definir um critério de paragem.

- `Best accept`: seleciona o melhor vizinho da vizinhança;
- `Fist accept`: seleciona o primeiro melhor vizinho;

No entanto estes dois algoritmos acabam por ficar presos num `ótimo local`.



Classificação

x/y/z

x -> se têm memória ou não
y -> random ou pesquisa por vizinhos
z -> uma única solução ou um conjunto de soluções

Os algoritmos mais utilizados são:
- Simulated Annealing - Arrefecimento Simulado
- Tabu Search
- Genetic Algorithms

### Arrefecimento Simulado