# Machine Learning

Campo da Inteligência Artificial que dá capacidade aos sistemas computacionais de aprender com os dados e com a experiência, para ter capacidade de prever resultados sem estarem explicitamente programados.

## Tipos de Machine Learning

- `Supervised`: os dados usados são já pré-catalogados corretamente. Podem ser problemas de **classificação**, com categorias (cores, por exemplo) ou problemas de **regressão**, com números reais (distâncias, dinheiro, por exemplo);
- `Unsupervised`: os dados não contêm classes definidas. Podem ser problemas de **clustering** e de **associações**;
- `Reinforcement`: de acordo com os outputs o sistema recebe feedback, com recompensas e penalidades;

A aprendizagem supervisionada deve usar dados pré-processados. O pré-processamento tem três etapas:
- `Integração` de dados de várias fontes e de vários formatos;
- `Limpeza` dos dados, lidar com dados parciais, dados-lixo, dados duplicados, incompletos e inconsistentes;
- `Transformação` dos dados, extrair as features importantes, reduzir a dimensão dos dados e balancear os tipos e categorias de dados;

## Extração de conhecimento a partir de dados

### KDD - Knowledge Discovery in Databases

Seleciona os dados, pré-processa, transforma, aplicação de *data mining* através de algoritmos e avalia no final o resultado obtido, ou seja, perceber se originou uma boa solução.

### SEMMA - Sample Explore Modify Model and Access

Através de uma amostra significativa de dados, pré-processa e transforma, cria um modelo genérico (padrões) e avalia.

###  CRISP-DM - Cross Industry Standard for Data Mining

Após perceber o problema, processa os dados. Os dados usados no pré-processamento podem ser modificados na próxima iteração se a avaliação controlada não for satisfatória. É o modelo mais standard.

## Dados

Os dados são pré-processados (extração de features, redução e normalização), para que a etapa de *Data Mining* possa garantir corretas:
- Previsões;
- Descrições;
- Classificações;
- Regressões;

Os dados são uma coleção de objetos e os seus atributos. Os atributos podem ser de vários tipos:
- `Nominais`, como identificadores, cor dos olhos...
- `Ordinais`, como notas, altura (pequeno, médio, grande)...
- `Intervalos`, como datas, temperaturas...
- `Racio`, como altura em centímetros, temperatura em Kelvin...

Os dados também podem ser discretos (incluindo binários) ou contínuos.

### Qualidade dos dados

A qualidade dos dados depende de quatro fatores principais:
- *Outliers*, dados errados;
- Valores duplicados;
- Valores em falta, ou eliminar os objetos ou estimar os atributos em falta;
- Ruído;

Dois objetos podem ser classificados através da sua proximidade, de acordo com duas medidas:
- `Similaridade`
- `Dissimilaridade`
Em geral, dois objetos são próximos se a distância dos seus atribuitos for pequena (distância em linha reta, ortogonal, minkowski). A partir daqui dá para ter uma ideia da **correlação** entre os dados, que pode variar entre -1 a 1:
- **-1**, são inversamente proporcionais
- **0**, os valores são independentes
- **1**, são diretamente proporcionais 

## Data Preprocessing

- `Agregação`, combinação de dois ou mais atributos de objetos num único atributo para ser mais facilmente manipulável e reduzir a quantidade de dados;

- `Sampling`, amostragem, com recolha de um conjunto representativo dos dados em geral. Pode ser de dois tipos:
    - **Random Sampling**, com ou seu reposição na população;
    - **Stratified Sampling**, através da divisão dos dados em várias partição e escolha de alguns valores entre cada classe;

- `Discretização`, converte um valor contínuo num valor ordinal, classificando os dados de acordo com intervalos pré-definidos;

- `Binarização`, converte valores inteiros para um valor binário;

### Transformação de Atributos

Através de transformações logarítmicas, exponenciais, modulares, para poder comparar atributos de objetos inicialmente distintos. <br>
Redução também de dimensionalidade, usando apenas as variávels que têm mais influência nos resultados que se querem obter, com o algoritmo PCA (*Principal Components Analysis*).

## Supervised Learning - Classification

Dado um conjunto de registos (conjunto de treino) e um conjunto de respostas pré-determinadas, o objetivo é encontrar um modelo para classificar corretamente futuros inputs, através de algoritmos de aprendizagem. O modelo deve ser testado para avaliar a sua eficiência com outro conjunto de dados com classificação também conhecida.

### Técnicas de Classificação

#### Decision Tree

Escolhe o atributo que parece separar melhor os dados em cada iteração. Pode haver mais de uma árvore que representa os dados selecionados. Inicialmente há a construção da árvore de decisão através do `algoritmo de Hunt`:

Em cada iteração, separa os valores por nó/atributo em duas categorias binárias ou não (depende do tipo da variável). O melhor *split* é escolhido com base no ganho antes e depois do split, com a diferença da impureza nas duas situações. O algoritmo termina com uma profundidade fixa, ou quando já não houver atributos, ou quando houver um split total dos dados. A impureza é descrita por três indicadores:

- Gini Index

```note
c  - número de classes
xi - número de objetos classificados como pertencentes à classe i
xt - número total de objetos classificados

gini_index() = 1 - sum((xi/xt)^2, for i in [0..c])
```

- Entropia

```note
c  - número de classes
xi - número de objetos classificados como pertencentes à classe i
xt - número total de objetos classificados

entropia() = sum(-(xi/xt) * log2 (xi/xt), for i in [0..c])
```

- Erro de classificação

```note
c  - número de classes
xi - número de objetos classificados como pertencentes à classe i
xt - número total de objetos classificados

classification_error() = 1 - max(xi/xt, for i in [0..c])
```

Por um lado é um algoritmo simples de implementar a nível de complexidade temporal e espacial, é robusto ao ruído e à distribuição dos atributos. Por outro lado um pequeno desvio nos dados de input compromete a estrutura da árvore e a separação dos ramos depende unicamente de um atributo e não de um conjunto ponderado destes.

### Erros de classificação

A ideia é ter um modelo generalizado, que não se adapte totalmente aos dados de treino e possa classificar correctamente os dados de teste. Temos de evitar *overfitting* do modelo, parando a otimização da árvore de decisão quando o erro de teste começa a subir (perde a generalização).

`Holdout` - Reserva uma percentagem para teste, o resto é para treino. A principal desvantagem é não treinar o modelo com todos os dados disponíveis, o que pode ser limitativo;

`Cross Validation` - Permite treinar com todos os dados, em cada iteração separa os dados em X partições, faz vários modelos com cada um e escolhe o melhor;

## Avaliação de Modelos

Permite avaliar a capacidade de previsão do modelo. A **Matriz de Confusão** permite organizar os valores em:
- Verdadeiros negativos
- Falsos negativos
- Verdadeiros positivos
- Falsos positivos

A partir da tabela conseguimos calcular a percentagem de acertos. No entanto, se os dados forem desbalanceados, esta medida não pode ser usada. Para dados desbalanceados podemos usar custos aos dados que importam prever.

### K-Nearest Neighbor

Seleciona os K vizinhos mais próximos do objeto a analisar e atribui a classificação da moda desses vizinhos. Não precisa de treino, embora precise de pré-processamento dos dados.

### Suport Vector Machines

Numa distribuição dos dados é possível criar vectores que separam os valores em dois grupos. O vetor de suporte é tanto melhor quanto mais largo, que significa que consegue separar com mais exatidão os valores.

### ANN - Artificial Neural Networks

Uma complexa função não-linear pode ser aprendida com base em unidades de processamento, com pesos associados a cada aresta. Os pesos depois são afinados com base na retro-propagação com valores finais corretos.