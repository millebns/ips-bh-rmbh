# Metodologia

## Fonte dos dados

[IPS Brasil](https://ipsbrasil.org.br): tabelas de dados das edições 2024, 2025 e 2026, com os 5.570 municípios brasileiros. Os arquivos originais estão em [`data/raw/`](../data/raw), apenas com os nomes padronizados:

| Arquivo no repositório | Arquivo original |
| --- | --- |
| `ips_brasil_2024.csv` | IPS Brasil 2024 - Tabela de Dados_Brasil.csv |
| `ips_brasil_2025.csv` | IPS Brasil 2025 - Tabela de Dados_Brasil.csv |
| `ips_brasil_2026.csv` | IPS Brasil 2026 - Tabela de Dados_Brasil.csv |

Antes do IPS, a primeira opção foi usar dados da Prefeitura de Belo Horizonte. A documentação mostrou que essa base ia só até 2016, e por isso o projeto buscou uma fonte mais recente.

## O que é o IPS

O Índice de Progresso Social mede **resultados sociais e ambientais**, e não renda. Ele tem notas de 0 a 100 (maior é melhor) e é formado por:

- **3 dimensões:** Necessidades Humanas Básicas, Fundamentos do Bem-estar e Oportunidades;
- **12 componentes**, quatro em cada dimensão;
- **57 indicadores** de fontes públicas.

O PIB per capita vem na base como informação complementar e **não entra no cálculo do índice**. Isso é o que permite perguntar se riqueza e progresso social andam juntos. A estrutura completa está no [dicionário de dados](dicionario_de_dados.md).

## Recorte

- **Edição:** apenas 2026 (ver [comparabilidade das edições](comparabilidade_edicoes.md)).
- **Estado:** Minas Gerais, 853 municípios, filtrados com SQL (DuckDB).
- **Região:** os 34 municípios da Região Metropolitana de Belo Horizonte (RMBH).

### Municípios da RMBH

Baldim, Belo Horizonte, Betim, Brumadinho, Caeté, Capim Branco, Confins, Contagem, Esmeraldas, Florestal, Ibirité, Igarapé, Itaguara, Itatiaiuçu, Jaboticatubas, Juatuba, Lagoa Santa, Mário Campos, Mateus Leme, Matozinhos, Nova Lima, Nova União, Pedro Leopoldo, Raposos, Ribeirão das Neves, Rio Acima, Rio Manso, Sabará, Santa Luzia, São Joaquim de Bicas, São José da Lapa, Sarzedo, Taquaraçu de Minas e Vespasiano.

A lista fica em [`src/ips_rmbh/config.py`](../src/ips_rmbh/config.py), e o notebook 02 confere que os 34 nomes estão na base.

## Checagens de qualidade

- Linhas duplicadas em cada edição.
- Município repetido dentro de Minas Gerais (`assert` em cada edição).
- Presença dos 34 municípios da RMBH na base de 2026.
- Valores faltantes: na RMBH, só *Violência Contra Indígenas* tem lacunas (16 municípios sem dado).

## Como as comparações são feitas

- **Posição de BH:** ranking entre os 34 municípios, em que 1 é o melhor. Empates dividem a mesma posição. Para indicadores de eventos negativos, como homicídios, a ordem é invertida (menor é melhor).
- **Referência regional:** mediana da RMBH, e não a média, para reduzir o peso de municípios muito diferentes.
- **IPS x PIB:** regressão linear simples do IPS no log10 do PIB per capita. A diferença entre o IPS observado e o esperado mostra quem tem progresso social acima ou abaixo do que a riqueza sugeriria.

## Limitações

- Municípios pequenos têm taxas mais instáveis, o que afeta a leitura de posições próximas no ranking.
- A relação entre IPS e PIB é uma associação entre 34 municípios, não uma relação de causa.
- As notas não são comparáveis entre edições, então o projeto não fala em evolução no tempo.
