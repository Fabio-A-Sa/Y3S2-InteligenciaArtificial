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

