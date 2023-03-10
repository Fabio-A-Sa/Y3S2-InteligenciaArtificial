# Introdução

A Inteligência Artificial é a ciência que se ocupa da construção de máquinas inteligentes, ou seja, máquinas que são capazes de realizar tarefas que quando realizadas por humanos requerem inteligência.

## Tipos de inteligência Artificial

- `Fraca`: focada em resolver um conjunto de tarefas específicas, como jogar um jogo, escolhas, etc;
- `Forte`: máquina mais geral que consegue realizar qualquer tarefa intelectual que um humano consiga, como o ChatGPT;

## Áreas da Inteligência Artificial

- Resolução de problemas;
- Machine Learning, quando a máquina aprende com dados e/ou as suas próprias ações sem estarem explicitamente programados. Pode ser *supervised* (quando aprende antes), *unsupervised* (aprende fazendo) ou *reinforcement* (dá-se pontos positivos ou negativos de acordo com as ações);
- Planeamento e Escalonamento;
- Processamento de linguagem Natural;
- Robótica inteligente;

## Agentes Inteligentes

Percebe o ambiente através de sensores e atua com motores, rodas, câmaras, (atuadores) para interagir com o mesmo. Um **agente racional** atua para ser o mais seguro, económico, maximizando a resolução do problema de acordo com as medidas de sucesso. Toma a ação correcta de acordo com a informação finita que tem. Um sistema **múltiplo-agente** reune dois ou mais agentes do tipo, que além de reagirem conforme o ambiente também podem interagir entre si.

São classificados de acordo com o método PEAS (Performance measure, Environments, Actuators, Sensors).

### Tipos de agentes

Para caracterizar o agente, é necessário primeiro saber as características do ambiente em que está inserido:

- `Simple Reflex/Reactive`: baseado em fórmulas if-then, com ambiente controlado e com as tarefas bem definidas. Reage ao ambiente atual;
- `With world representation`: baseado em agentes de reflexo que contém uma representação do estado do mundo (memória) em conjunto com as suas ações. Em cada iteração atualiza o estado;
- `Objective Based`: tem descrição interna do estado atual do mundo, do objectivo a alcançar e dos efeitos que as suas ações têm no ambiente. Usado para problemas de pesquisa;
- `Utility Based`: a medida de sucesso é com base na utilidade, uma medida de desempenho. Orienta uma sequência de ações que incrementem a sua utilidade;
- `Learning`: aprende com o ambiente de modo a aumentar cada vez mais a sua performance;
- `BDI`: beliefs, desires and intentions, de modo a ter informações, motivações e deliberações;

### Propriedades dos ambientes

- Acessível ou não acessível: quando os sensores do agente consegue detectar tudo que é relevante no ambiente;
- Determinístico ou não determinístico: se o próximo estado é determinado pelo ambiente e por ações anteriores do agente;
- Episódico e não episódico: quando os episódios seguintes dependem ou não dos anteriores;
- Estático e dinâmico: se o estado do ambiente muda quando o agente está a analisar a próxima ação;
- Discreto e contínuo: quando há um número finito de ações e percepções possíveis;
- Agente único e múltiplos agentes. Estes último permite eliminar os pontos de falha, ser escalável, com componentes independentes, ter uma distribuição da informação pelo ambiente;

