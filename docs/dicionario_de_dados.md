# Dicionário de dados — IPS Brasil 2026

Base usada nas análises: `data/raw/ips_brasil_2026.csv` (5.570 municípios × 78 colunas). Na base tratada da RMBH (`data/processed/ips_2026_rmbh.csv`) ficam os 34 municípios, com as mesmas colunas.

**Como ler:**
- O índice geral, as 3 dimensões e os 12 componentes são notas de 0 a 100; quanto maior, melhor.
- Os 57 indicadores estão na unidade original de cada fonte (taxas, percentuais, índices). Para taxas de eventos negativos, como homicídios ou mortes no trânsito, **menor é melhor**.
- A coluna “Nulos” mostra os valores faltantes no Brasil e na RMBH.
- O agrupamento dos indicadores por componente segue a ordem das colunas na base e o [relatório metodológico do IPS Brasil 2026](https://ipsbrasil.org.br/relatorios/download/IPSBrasil2026-Metodol%C3%B3gico.pdf), que traz também as fontes e as definições de cada indicador.
- Alguns nomes de coluna têm espaço no final (ex.: `Expectativa de Vida `). Isso vem da base original.

## Identificação e informações complementares

| Coluna | Descrição | Nulos (Brasil / RMBH) |
| --- | --- | --- |
| `Município` | Nome do município | 0 / 0 |
| `UF` | Sigla do estado | 0 / 0 |
| `ÁREA km²` | Área do município em km² | 0 / 0 |
| `POPULAÇÃO 2025` | População de referência usada nesta edição (2025) | 0 / 0 |
| `PIB PER CAPITA` | PIB per capita em R$. **Não entra no cálculo do IPS**; é informação complementar | 0 / 0 |
| `Índice de Progresso Social` | Índice geral (0 a 100), média das três dimensões | 0 / 0 |

## Dimensões (0 a 100)

| Coluna | Componentes que a formam |
| --- | --- |
| `Necessidades Humanas Básicas` | Nutrição e Cuidados Médicos Básicos, Água e Saneamento, Moradia, Segurança Pessoal |
| `Fundamentos do Bem-estar` | Acesso ao Conhecimento Básico, Acesso à Informação e Comunicação, Saúde e Bem-estar, Qualidade do Meio Ambiente |
| `Oportunidades` | Direitos Individuais, Liberdades Individuais e de Escolha, Inclusão Social, Acesso à Educação Superior |

## Nutrição e Cuidados Médicos Básicos

Dimensão: Necessidades Humanas Básicas. Nota do componente: coluna `Nutrição e Cuidados Médicos Básicos` (0 a 100).

| Indicador | Nulos (Brasil / RMBH) |
| --- | --- |
| `Cobertura Vacinal (poliomielite)` | 0 / 0 |
| `Hospitalizações por Condições Sensíveis à Atenção Primária` | 0 / 0 |
| `Mortalidade Ajustada por Condições Sensíveis à Atenção Primária` | 0 / 0 |
| `Mortalidade Infantil até 5 anos` | 0 / 0 |
| `Subnutrição` | 0 / 0 |

## Água e Saneamento

Dimensão: Necessidades Humanas Básicas. Nota do componente: coluna `Água e Saneamento` (0 a 100).

| Indicador | Nulos (Brasil / RMBH) |
| --- | --- |
| `Abastecimento de Água Via Rede de Distribuição` | 0 / 0 |
| `Esgotamento Sanitário Adequado` | 0 / 0 |
| `Índice de Abastecimento de Água` | 0 / 0 |
| `Índice de Perdas de Água na Distribuição` | 0 / 0 |

## Moradia

Dimensão: Necessidades Humanas Básicas. Nota do componente: coluna `Moradia` (0 a 100).

| Indicador | Nulos (Brasil / RMBH) |
| --- | --- |
| `Domicílios com Coleta de Resíduos Adequada` | 0 / 0 |
| `Domicílios com Iluminação Elétrica Adequada` | 0 / 0 |
| `Domicílios com Paredes Adequadas` | 0 / 0 |
| `Domicílios com Pisos Adequados` | 0 / 0 |

## Segurança Pessoal

Dimensão: Necessidades Humanas Básicas. Nota do componente: coluna `Segurança Pessoal` (0 a 100).

| Indicador | Nulos (Brasil / RMBH) |
| --- | --- |
| `Assassinatos de Jovens` | 0 / 0 |
| `Assassinatos de Mulheres` | 0 / 0 |
| `Homicídios` | 0 / 0 |
| `Mortes por Acidentes de Transporte` | 0 / 0 |

## Acesso ao Conhecimento Básico

Dimensão: Fundamentos do Bem-estar. Nota do componente: coluna `Acesso ao Conhecimento Básico` (0 a 100).

| Indicador | Nulos (Brasil / RMBH) |
| --- | --- |
| `Abandono no Ensino Fundamental` | 0 / 0 |
| `Abandono no Ensino Médio` | 0 / 0 |
| `Distorção Idade-Série no Ensino Médio` | 0 / 0 |
| `Evasão no Ensino Médio` | 0 / 0 |
| `Ideb Ensino Fundamental` | 0 / 0 |
| `Reprovação Escolar no Ensino Médio` | 0 / 0 |

## Acesso à Informação e Comunicação

Dimensão: Fundamentos do Bem-estar. Nota do componente: coluna `Acesso à Informação e Comunicação` (0 a 100).

| Indicador | Nulos (Brasil / RMBH) |
| --- | --- |
| `Cobertura de Internet Móvel (4G/5G)` | 0 / 0 |
| `Densidade de Internet Banda Larga Fixa` | 0 / 0 |
| `Densidade Telefonia Móvel` | 0 / 0 |
| `Qualidade de Internet Móvel` | 0 / 0 |

## Saúde e Bem-estar

Dimensão: Fundamentos do Bem-estar. Nota do componente: coluna `Saúde e Bem-estar` (0 a 100).

| Indicador | Nulos (Brasil / RMBH) |
| --- | --- |
| `Consumo de ultraprocessados` | 0 / 0 |
| `Expectativa de Vida ` | 0 / 0 |
| `Mortalidade entre 15 e 50 anos` | 0 / 0 |
| `Mortalidades por Doenças Crônicas Não Transmissíveis ` | 0 / 0 |
| `Obesidade` | 0 / 0 |
| `Suicídios` | 0 / 0 |

## Qualidade do Meio Ambiente

Dimensão: Fundamentos do Bem-estar. Nota do componente: coluna `Qualidade do Meio Ambiente` (0 a 100).

| Indicador | Nulos (Brasil / RMBH) |
| --- | --- |
| `Áreas Verdes Urbanas` | 0 / 0 |
| `Emissões de CO₂e por Habitante` | 0 / 0 |
| `Focos de Calor` | 0 / 0 |
| `Índice de Vulnerabilidade Climática dos Municípios (IVCM)` | 0 / 0 |
| `Supressão da Vegetação Primária e Secundária` | 0 / 0 |

## Direitos Individuais

Dimensão: Oportunidades. Nota do componente: coluna `Direitos Individuais` (0 a 100).

| Indicador | Nulos (Brasil / RMBH) |
| --- | --- |
| `Acesso a Programas de Direitos Humanos` | 0 / 0 |
| `Existência de Ações para Direitos de Minorias` | 0 / 0 |
| `Índice de Atendimento à Demanda de Justiça` | 0 / 0 |
| `Resposta a Processos Previdenciários` | 0 / 0 |
| `Resposta a Processos Familiares` | 0 / 0 |
| `Taxa de Congestionamento Líquida de Processos` | 0 / 0 |

## Liberdades Individuais e de Escolha

Dimensão: Oportunidades. Nota do componente: coluna `Liberdades Individuais e de Escolha` (0 a 100).

| Indicador | Nulos (Brasil / RMBH) |
| --- | --- |
| `Acesso à Cultura, Lazer e Esporte` | 0 / 0 |
| `Gravidez na Adolescência (<19)` | 0 / 0 |
| `Índice de Vulnerabilidade das Famílias do CadÚnico (IVCAD)` | 0 / 0 |
| `Praças e Parques em Áreas Urbanas` | 0 / 0 |

## Inclusão Social

Dimensão: Oportunidades. Nota do componente: coluna `Inclusão Social` (0 a 100).

| Indicador | Nulos (Brasil / RMBH) |
| --- | --- |
| `Famílias em Situação de Rua` | 0 / 0 |
| `Paridade de Gênero na Câmara Municipal` | 0 / 0 |
| `Paridade de Negros na Câmara Municipal` | 0 / 0 |
| `Violência Contra Indígenas` | 4078 / 16 |
| `Violência Contra Mulheres` | 0 / 0 |
| `Violência Contra Negros` | 0 / 0 |

## Acesso à Educação Superior

Dimensão: Oportunidades. Nota do componente: coluna `Acesso à Educação Superior` (0 a 100).

| Indicador | Nulos (Brasil / RMBH) |
| --- | --- |
| `Empregados com Ensino Superior` | 0 / 0 |
| `Mulheres Empregadas com Ensino Superior` | 0 / 0 |
| `Nota Mediana no Enem` | 0 / 0 |
