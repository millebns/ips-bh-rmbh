"""Leitura das bases e funções de apoio à limpeza."""

import unicodedata

import pandas as pd

from .config import CAMINHO_RMBH_2026, CAMINHOS_BRUTOS


def carregar_edicao(ano):
    """Lê a tabela de dados original de uma edição do IPS Brasil ('2024', '2025' ou '2026')."""
    return pd.read_csv(CAMINHOS_BRUTOS[str(ano)])


def carregar_rmbh():
    """Lê a base tratada da RMBH (edição 2026), gerada pelo notebook 02."""
    if not CAMINHO_RMBH_2026.exists():
        raise FileNotFoundError(
            f'{CAMINHO_RMBH_2026} não encontrado. Rode antes o notebook 02_limpeza_mg_rmbh.ipynb.'
        )
    return pd.read_csv(CAMINHO_RMBH_2026)


def normalizar(nome):
    """Padroniza o nome de uma coluna: minúsculas, sem acentos e sem espaços nas pontas."""
    nome = unicodedata.normalize('NFKD', nome.strip().lower())
    return ''.join(c for c in nome if not unicodedata.combining(c))
