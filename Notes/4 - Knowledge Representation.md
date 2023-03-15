# Knowledge Representation

Codificação das formas de raciocínio para os programas de computador usando lógica ao implementar agentes baseados em conhecimento.
A base de dados usada (*Knowledge Base, KB*) é um conjunto de factos sobre o sistema numa determinada linguagem que vai ser importante para a resolução do problema:

- `TELL`, adicionar novos dados ao conjunto;
- `ASK`, pesquisa com base no que se sabe;

Os **mecanismos de inferência** garantem que o raciocínio criado a partir do conjunto de dados é coerente. No caso a seguir, 'a' é uma proposição lógica mais forte que 'b', pelo que pode ser adicionada à base de conhecimento. 

```c
a |= b, 'a' implica 'b'
```

A `inferência lógica` acontece sempre que podemos derivar uma afirmação verdadeira da base de conhecimento, preservando a verdade (*soundness*) e a completude (derivar qualquer frase que esteja vinculada ao conhecimento). Dois conhecimentos dizem-se **logicamente equivalentes** se um implicar outro e vice-versa. <br>
As provas podem ser de dois tipos:
- Backward chaining;
- Forward chaining;

## First Order Logic



## Incerteza

Maximizar o nível de performance do agente e não a probabilidade de sucesso, com base na Teoria da Utilidade.

1. Probabilidade condicionada:

```note
P(gripe|febre) = P(gripe && febre) / P(febre)
```

2. Teorema de Bayes

```note
P(b|a) = ( P(a|b) * P(b) ) / P(a)
```