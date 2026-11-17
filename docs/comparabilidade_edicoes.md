# Por que as edições 2024, 2025 e 2026 não são comparadas

O plano original do projeto era acompanhar a evolução de Belo Horizonte no IPS entre as edições 2024, 2025 e 2026. Ao colocar as três bases lado a lado (notebook [`01_exploracao_edicoes`](../notebooks/01_exploracao_edicoes.ipynb)), ficou claro que a mesma coluna, com o mesmo nome, não mede exatamente a mesma coisa em todas as edições. O próprio IPS Brasil avisa que as bases publicadas nesses anos não são estritamente comparáveis.

## O que muda entre as edições

| Edição | Nº de colunas | População de referência |
| --- | --- | --- |
| 2024 | 74 | 2022 |
| 2025 | 78 | 2024 |
| 2026 | 78 | 2025 |

### De 2024 para 2025: o conjunto de indicadores mudou

- **Saiu:** Trabalho Infantil.
- **Entraram:** Famílias em Situação de Rua, IVCAD (Índice de Vulnerabilidade das Famílias do CadÚnico), Consumo de Ultraprocessados, Resposta a Processos Previdenciários e Resposta a Processos Familiares.
- **Enem:** passou de **nota média** para **nota mediana**, que é outra estatística.

### De 2025 para 2026: mesmos indicadores, tratamento diferente

- Os indicadores são os mesmos, mas vários nomes de coluna mudaram de grafia (maiúsculas, plural, espaço no fim). Por isso a comparação foi feita com os nomes **normalizados**: minúsculas, sem acentos e sem espaços nas pontas (função `normalizar` em [`src/ips_rmbh/dados.py`](../src/ips_rmbh/dados.py)).
- Mesmo assim, o tratamento dos dados mudou: *Violência Contra Indígenas* passou de 745 para 4.078 valores faltantes no Brasil.

## Consequência

O IPS, as dimensões e os componentes são calculados a partir desses indicadores. Por isso, comparar a nota de BH em 2024 com a de 2026 mostraria uma "evolução" que, em parte, seria só uma mudança na forma de medir.

**Decisão:** as análises usam somente a **edição 2026**, a mais recente e completa. As edições 2024 e 2025 ficam no repositório como contexto e para quem quiser reproduzir a comparação.
