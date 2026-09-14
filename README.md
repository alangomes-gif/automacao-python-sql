# Sistema de Automação de Dados & Integração SQL com Python

Este projeto automatiza a ingestão, tratamento e carga de dados de vendas não estruturados para um banco de dados relacional SQL.

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **Pandas** (Tratamento e limpeza de dados)
- **SQLite3** (Banco de dados relacional)
- **Git & GitHub** (Versionamento de código)

## 🎯 Funcionalidades Principais
1. **Ingestão de Dados:** Leitura de arquivos `.csv` de vendas.
2. **Tratamento & Validação:** Correção de valores nulos e cálculo automático do faturamento por item.
3. **Persistência SQL:** Criação de estrutura de tabela via DDL e gravação otimizada.
4. **Consultas analíticas:** Agrupamento e relatórios de faturamento via SQL puro (`GROUP BY`, `SUM`).

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/automacao-python-sql.git](https://github.com/SEU-USUARIO/automacao-python-sql.git)
   cd automacao-python-sql