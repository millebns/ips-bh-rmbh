"""Caminhos, constantes e listas usadas em todos os notebooks."""

from pathlib import Path

# Raiz do repositório (duas pastas acima deste arquivo: src/ips_rmbh/config.py)
RAIZ = Path(__file__).resolve().parents[2]

PASTA_BRUTOS = RAIZ / 'data' / 'raw'
PASTA_TRATADOS = RAIZ / 'data' / 'processed'
PASTA_FIGURAS = RAIZ / 'reports' / 'figures'

CAMINHOS_BRUTOS = {
    '2024': PASTA_BRUTOS / 'ips_brasil_2024.csv',
    '2025': PASTA_BRUTOS / 'ips_brasil_2025.csv',
    '2026': PASTA_BRUTOS / 'ips_brasil_2026.csv',
}

CAMINHO_MG_2026 = PASTA_TRATADOS / 'ips_2026_mg.csv'
CAMINHO_RMBH_2026 = PASTA_TRATADOS / 'ips_2026_rmbh.csv'

# Visualização
BH = 'Belo Horizonte'
COR_BH = '#C0392B'
COR_OUTROS = '#B0B7BF'
COR_DESTAQUE = '#2E86AB'

# Municípios da Região Metropolitana de Belo Horizonte (34)
MUNICIPIOS_RMBH = [
    'Baldim', 'Belo Horizonte', 'Betim', 'Brumadinho', 'Caeté', 'Capim Branco',
    'Confins', 'Contagem', 'Esmeraldas', 'Florestal', 'Ibirité', 'Igarapé',
    'Itaguara', 'Itatiaiuçu', 'Jaboticatubas', 'Juatuba', 'Lagoa Santa',
    'Mário Campos', 'Mateus Leme', 'Matozinhos', 'Nova Lima', 'Nova União',
    'Pedro Leopoldo', 'Raposos', 'Ribeirão das Neves', 'Rio Acima', 'Rio Manso',
    'Sabará', 'Santa Luzia', 'São Joaquim de Bicas', 'São José da Lapa',
    'Sarzedo', 'Taquaraçu de Minas', 'Vespasiano',
]

# Estrutura do IPS: 3 dimensões e 12 componentes
DIMENSOES = ['Necessidades Humanas Básicas', 'Fundamentos do Bem-estar', 'Oportunidades']

COMPONENTES = [
    'Nutrição e Cuidados Médicos Básicos', 'Água e Saneamento', 'Moradia',
    'Segurança Pessoal', 'Acesso ao Conhecimento Básico',
    'Acesso à Informação e Comunicação', 'Saúde e Bem-estar',
    'Qualidade do Meio Ambiente', 'Direitos Individuais',
    'Liberdades Individuais e de Escolha', 'Inclusão Social',
    'Acesso à Educação Superior',
]
