# Knowledge Representation

Codificação das formas de raciocínio para os programas de computador usando lógica ao mplementar agentes baseados em conhecimento.
A base de dados usada (*Knowledge Base, KB*) é um conjunto de factos sobre o sistema numa determinada linguagem que vai ser importante para a resolução do problema:

- `TELL`, adicionar novos dados ao conjunto;
- `ASK`, pesquisa com base no que se sabe;

Os **mecanismos de inferência** garantem que o raciocínio criado a partir do conjunto de dados é coerente.

<TODO: tudo>

<COISAS>

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