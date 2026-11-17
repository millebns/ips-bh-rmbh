"""Funções para comparar um município (por padrão, BH) com os demais da RMBH."""

import pandas as pd

from .config import BH


def posicao(df, coluna, maior_melhor=True, municipio=BH):
    """Posição do município entre os da base (1 = melhor; empates dividem a posição)."""
    r = df[coluna].rank(ascending=not maior_melhor, method='min')
    return int(r[df['Município'] == municipio].iloc[0])


def valor(df, coluna, municipio=BH):
    """Valor de uma coluna para o município."""
    return df.loc[df['Município'] == municipio, coluna].iloc[0]


def perfil(df, colunas, municipio=BH):
    """Tabela com o valor do município, a mediana da base, a diferença e a posição em cada coluna."""
    linhas = []
    for c in colunas:
        v = valor(df, c, municipio)
        linhas.append({
            'item': c,
            'BH': round(v, 2),
            'mediana_RMBH': round(df[c].median(), 2),
            'diferenca': round(v - df[c].median(), 2),
            'posicao_BH': posicao(df, c, municipio=municipio),
        })
    return pd.DataFrame(linhas).sort_values('diferenca', ascending=False).reset_index(drop=True)
