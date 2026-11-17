# Diário de bordo

Registro das etapas do projeto e das decisões tomadas em cada uma.

## Sprint 1 · Escolha da base, escopo e limpeza

O Sprint 1 era para ser "só" a limpeza dos dados. Virou uma lição sobre não assumir que dois números com o mesmo nome medem a mesma coisa.

**Escolha da base.** A primeira opção foram os dados da Prefeitura de Belo Horizonte, mas a documentação mostrou que eles iam só até 2016. A alternativa foi o IPS Brasil, uma base atual com indicadores de acesso à cultura e lazer, segurança e PIB per capita, cobrindo os 853 municípios de Minas Gerais.

**Escopo.** Uma única base pode gerar várias análises diferentes, então o primeiro passo foi definir as perguntas do projeto e montar a lista da Região Metropolitana de BH, para facilitar os filtros.

**A virada.** O plano original era comparar a evolução de Belo Horizonte no IPS entre as edições 2024, 2025 e 2026. Ao colocar as três bases lado a lado, apareceu o aviso do próprio IPS Brasil: essas edições não são estritamente comparáveis. E os dados mostraram por quê:

- o Enem deixou de usar a nota média e passou a usar a nota mediana;
- o indicador Trabalho Infantil saiu, e entraram cinco novos, como Famílias em Situação de Rua e Consumo de Ultraprocessados;
- a população de referência muda a cada edição (2022, 2024 e 2025).

Comparar 2024 com 2026 mostraria uma evolução que seria, em parte, só uma mudança de régua.

**Decisão:** usar somente a edição 2026. As edições 2024 e 2025 ficam como contexto. Detalhes em [comparabilidade das edições](comparabilidade_edicoes.md).

**Resto da limpeza:**

- filtro de Minas Gerais com SQL (DuckDB);
- conferência de duplicados e de município repetido;
- lista dos 34 municípios da RMBH, todos encontrados na base.

**Notebooks:** [`01_exploracao_edicoes`](../notebooks/01_exploracao_edicoes.ipynb) e [`02_limpeza_mg_rmbh`](../notebooks/02_limpeza_mg_rmbh.ipynb).

## Sprint 2 · Primeiras respostas

Onde BH fica no ranking da Grande BH, como BH se compara aos vizinhos nos componentes do índice, no PIB per capita e em segurança, e se renda mais alta significa mais segurança.

**Notebooks:** [`03_ranking_ips_rmbh`](../notebooks/03_ranking_ips_rmbh.ipynb) a [`06_seguranca`](../notebooks/06_seguranca.ipynb).
