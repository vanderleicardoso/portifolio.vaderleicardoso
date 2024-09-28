Aqui está um exemplo de documentação que você pode adicionar ao arquivo `README.md` do seu projeto para guiar outros desenvolvedores (ou você mesmo no futuro) sobre como rodar o projeto:

---

# Marvel Movies Dashboard

Este projeto utiliza **Streamlit** para visualizar dados de filmes da Marvel que estão armazenados em um banco de dados **Supabase**. A aplicação permite a exibição de dados e gráficos interativos, como a receita global dos filmes, pontuações de críticos e audiência, e outras métricas importantes.

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter as seguintes ferramentas instaladas:

- **Python 3.8+**
- **Pip** (gerenciador de pacotes do Python)

Além disso, você precisará instalar as bibliotecas requeridas, conforme descrito abaixo.

## Instalação

1. **Clone o repositório**:

   Abra o terminal e execute:

   ```bash
   git clone https://github.com/seu-usuario/marvel-movies-dashboard.git
   cd marvel-movies-dashboard
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use: venv\Scripts\activate
   ```

3. **Instale as dependências**:

   Com o ambiente virtual ativo, instale as bibliotecas necessárias:

   ```bash
   pip install -r requirements.txt
   ```

   Se não houver um arquivo `requirements.txt`, você pode criar um com as dependências abaixo:

   ```bash
   pip install streamlit pandas supabase
   ```

   Depois de instalar, você pode gerar um `requirements.txt` com:

   ```bash
   pip freeze > requirements.txt
   ```

## Configuração

Certifique-se de que você tem as credenciais corretas do **Supabase**. No arquivo principal (`app.py`, por exemplo), verifique se as seguintes variáveis estão corretas:

```python
SUPABASE_URL = "https://seu-supabase-url.supabase.co"
SUPABASE_KEY = "sua-supabase-key"
```

### Estrutura esperada dos dados

A tabela `vanderlei` no Supabase deve conter uma coluna chamada `data_linha`, onde cada registro tem o seguinte esquema JSON:

```json
{
  "movie": "Ant-Man",
  "category": "Ant-Man",
  "year": 2015,
  "worldwide gross ($m)": 518,
  "% budget recovered": "398%",
  "critics % score": "83%",
  "audience % score": "85%",
  "audience vs critics % deviance": "-2%",
  "budget": 130,
  "domestic gross ($m)": 180,
  "international gross ($m)": 338,
  "opening weekend ($m)": 57,
  "second weekend ($m)": 24,
  "1st vs 2nd weekend drop off": "-58%",
  "% gross from opening weekend": 31.8,
  "% gross from domestic": "34.70%",
  "% gross from international": "65.30%",
  "% budget opening weekend": "43.80%"
}
```

### Ambiente de Desenvolvimento

Para conectar ao Supabase, o projeto já está configurado com o client da API. Apenas configure as variáveis de ambiente necessárias para a conexão.

## Executando o Projeto

Após instalar todas as dependências e configurar as credenciais do Supabase, você pode rodar a aplicação Streamlit com o seguinte comando:

```bash
streamlit run app.py
```

Isso abrirá a aplicação no seu navegador padrão em `http://localhost:8501`.

## Funcionalidades

- **Exibição de Tabela:** Todos os dados do banco de dados são exibidos em uma tabela interativa.
- **Gráfico de Barras:** Exibe a receita global (`worldwide gross ($m)`) dos filmes ao longo dos anos.
- **Comparação de Pontuação:** Compara a pontuação dos críticos e da audiência de cada filme.

## Personalização

Você pode personalizar a aplicação para:

1. **Adicionar novos gráficos**: Modifique a seção de gráficos no código principal para visualizar outras métricas, como `domestic gross ($m)` ou `opening weekend ($m)`.
2. **Filtros Interativos**: Streamlit oferece suporte a widgets como sliders e caixas de seleção, permitindo que você adicione filtros para visualizar os dados de forma mais dinâmica.

## Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit**: Para criar a interface visual interativa.
- **Pandas**: Para manipulação de dados.
- **Supabase**: Para armazenamento e recuperação dos dados.

## Problemas Comuns

1. **Erro de Conexão com o Supabase**: Verifique se a URL e a chave da API estão corretas e se você tem acesso à tabela `vanderlei` no seu projeto do Supabase.
2. **Dados não Carregam**: Certifique-se de que a tabela no Supabase contém dados no formato esperado, especialmente na coluna `data_linha`.

## Contato

Se você tiver alguma dúvida ou problema, entre em contato com [seu-email@exemplo.com].

---

### Exemplo de arquivo `requirements.txt`:

```txt
pandas==1.3.3
streamlit==1.4.0
supabase-py==0.1.3
```

Este arquivo lista todas as dependências necessárias para rodar o projeto.