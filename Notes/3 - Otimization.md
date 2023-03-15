# Otimization

Os problemas de otimização são muitas vezes de maximização ou de minimização. O conjunto de estados possíveis para um problema é finito embora possa ser muito grande, pelo que a pesquisa total é impossível: recorre-se à aproximação. Exemplos de algoritmos:
- Knapsack Problem;
- Travelling Salesman Problem (TSP);
- COP - Combinatorial Optimization Problem;

Para os problemas de otimização normalmente usa-se a **vizinhança** de modo a poder saltar de solução em solução para tentar atingir um ótimo local. Para fugir do ótimo local é necessário usar outro tipo de mecanismos, como remover um elemento da solução, adicionar um elemento na solução ou trocar elementos da sua ordem original. Um ótimo global é também um ótimo local no que diz respeito à sua vizinhança. É importante definir um critério de paragem.

- `Best accept`: seleciona o melhor vizinho da vizinhança;
- `Fist accept`: seleciona o primeiro melhor vizinho;

No entanto estes dois algoritmos acabam por ficar presos num `ótimo local`, pois param quando não encontram nenhum melhoramento próximo. Para isso usam-se as meta-heurísticas.

### Classificação de Meta-heurísticas X/Y/Z

`X` -> se têm memória (A) ou não (M)
`Y` -> random (S) ou pesquisa por vizinhos (N)
`Z` -> uma única solução (1) ou um conjunto de soluções que representam uma população (P)

Os algoritmos mais utilizados são:
- Simulated Annealing;
- Tabu Search;
- Genetic Algorithms;

### Arrefecimento Simulado