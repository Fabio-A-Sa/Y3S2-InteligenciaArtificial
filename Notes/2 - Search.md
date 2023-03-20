# Search

Um problema de pesquisa pode ser formulado de acordo com os seguintes tópicos:

- Representação do estado;
- O estado inicial;
- O estado objectivo;
- Os operadores (com nome, pré-condições, efeitos e custo associados);
- Custo total da solução;

Os problemas podem ser:

- Problemas de `estado único` (são determinísticos e com ambiente acessível);
- Problemas de `estados múltiplos` (determinísticos mas com ambiente não totalmente acessível);
- Problemas de `contingência` (não determinísticos com ambiente inacessível, os sensores devem ser usados durante a execução, a pesquisa é realizada com uma árvore ou regras bem definidas);
- Problemas de `exploração` (quando o espaço de estados não é definido);

### Classificação de estratégias de pesquisa

- Completo: se a solução existir será encontrada;
- Complexidade temporal;
- Complexidade espacial;
- Optimalidade: se o algoritmo encontrar sempre a solução ótima (com menor custo);

As complexidades temporais e espaciais são medidas em termos de:
- Fator de ramificação (b, *branch factor*);
- Profundidade da solução de menor custo / ótima (d, *depth factor*);
- Profundidade da árvore de pesquisa (m, pode ser infinito);

## Algoritmos de pesquisa não informada

### Breadth-First Search (BFS)

O principal problema está na utilização de recursos, onde todos os estados possíveis têm de estar obrigatoriamente na memória. Tem custo exponencial em tempo e espaço, O(b^d). É uma algoritmo sistemático e útil para pequenas pesquisas num espaço de estados bem definidos.

### Dijkstra / Pesquisa de custo uniforme

A estratégia é expandir o nó com melhor custo acumulado. Se o custo for proporcional à profundidade alcançada, então trata-se de um BFS normal.

### Depth-First Search (DFS)

Só funciona eficientemente se a pesquisa tiver uma profundidade limite (m). Por outro lado é possível eliminar parte do espaço de estados / da memória manipulada quando uma subárvore não contém a solução desejada. A complexidade no espaço passa a ser O(bm) e a complexidade temporal depende da profundidade máxima, O(b^m).

### Iterative Deepening Search (IDS)

Método ótimo e completo. É a melhor solução quando a profundidade da solução não é conhecida e queremos minimizar os custos de uma pesquisa em profundidade. Iterativamente aumentamos a profundidade de pesquisa, tornando a complexidade temporal O(b^d) e a complexidade espacial O(bd).

### Pesquisa bidirecional

Enquanto parte do algoritmo pesquisa da origem ao destino, outra parte pesquisa do destino à origem. Serve somente para problemas onde dá para gerar os nós parentes e se houver um número finito de soluções. Reduz a complexidade temporal em metade, O(b^(d/2)).

## Algoritmos de pesquisa informada

### Greedy-Search

Algoritmo que não é ótimo nem completo. Expande o nó que parece estar mais próximo da solução. Por exemplo a distância em linha reta num mapa. Não garante chegar à solução e muito menos chegar à solução ótima, pode ficar em ciclos infinitos se houver nós repetidos. Manter todos os nós pesquisados em memória causa um problema a nível de complexidade temporal O(b^m) e complexidade espacial O(b^m), com m potencialmente infinito pois é a profundidade da árvore de pesquisa. 

### A*

É um algoritmo ótimo e completo desde que a eurítica seja admissível e otimista, como por exemplo a distância em linha reta para atingir o objectivo. Não necessita de testar os estados repetidos. Soma entre o custo para chegar ao estado atual e o custo estimado para atingir o objetivo. 

A variante `Weighted A*` permite expandir menos nós, expandido só aqueles que garantam uma solução satisfatória gastando menos tempo e espaço, mas que pode não ser a ótima. 

## Adversarial Search

Quando um oponente imprevisível e racional é inserido no mundo, jogando da melhor forma possível.

