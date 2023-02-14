# Search

Criação de um agente para resolução de problemas de pesquisa. Um problema pode ser caracterizado por:

- Conjunto de estados;
- O estado inicial;
- Conjunto de estados objectivo/finais;
- Transições entre estados possíveis;

O problema pode ser formulado de acordo com os seguintes tópicos:

- Representação de estado;
- O estado inicial;
- O estado objectivo;
- Os operadores (com nome, pré-condições, efeitos e custo associados);
- Custo total da solução;

Os problemas podem ser:

- Problemas de `estado único` (são determinísticos e com ambiente acessível);
- Problemas de `estados múltiplos` (determinísticos mas com ambiente não acessível);
- Problemas de `contingência` (não determinísticos com ambiente inacessível, os sensores devem ser usados durante a execução, a pesquisa é realizada com uma árvore ou regras bem definidas);
- Problemas de `exploração` (quando o espaço de estados não é definido);

### Classificação de estratégias de pesquisa

- Completo: se a solução existir será encontrada;
- Complexidade temporal;
- Complexidade espacial;
- Optimalidade: se o algoritmo encontrar sempre a solução ótima (com menor custo);

As complexidades temporais e espaciais são medidas em termos de:
- Fator de ramificação;
- Profundidade da árvore de pesquisa;
- Profundidade da solução de menor custo / ótima;

## Algoritmos de pesquisa não informada

### Breadth-First Search (BFS)

O principal problema está na utilização de recursos, onde todos os estados possíveis têm de estar obrigatoriamente na memória. Tem custo exponencial em tempo e espaço, O(B^N), sendo  <TODO>

### Dijkstra / Pesquisa de custo uniforme

<TODO>

### Depth-First Search (DFS)

Só funciona eficientemente se a pesquisa tiver uma profundidade limite. Por outro lado é possível eliminar parte do espaço de estados / da memória manipulada quando uma subárvore não contém a solução desejada. A complexidade no espaço passa a ser O(BN) e não O(B^N), embora gaste mais tempo do que o BFS.

### Iterative Deepening Search (IDS)

Método ótimo e completo, com  <TODO>

### Pesquisa bidirecional

<TODO>

## Algoritmos de pesquisa informada

### Greedy-Search

Expande o nó que parece estar mais próximo da solução. Por exemplo a distância em linha reta num mapa. Não garante chegar à solução e muito menos chegar à solução ótima, pode chegar em ciclos infinitos se houver nós repetidos. Por outro lado é rápido, apesar de manter todos os nós pesquisados em memória.a

### A*

Soma o custo com o <TODO>
Não necessita de testar estados repetidos. 
Desde que a eurística (distância em linha reta), o algoritmo é ótimo e completo.

