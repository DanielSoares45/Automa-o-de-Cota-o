# 🤖 Assistente de Cotação Diária (RPA)

Um projeto de Automação Robótica de Processos (RPA) desenvolvido em Python para eliminar o trabalho manual de busca e registro de cotações de moedas. Este é um projeto focado em demonstrar a resolução de problemas reais de negócios através da programação.

## 🎯 Objetivo do Projeto

Demonstrar a capacidade de integrar o consumo de APIs RESTful com automação de interface gráfica (GUI) para otimizar rotinas operacionais. O script busca as cotações atuais do Dólar e do Euro em tempo real e digita automaticamente um relatório padronizado diretamente no Bloco de Notas do Windows.

## 🛠️ Tecnologias Utilizadas

* **Python 3**

* **Requests:** Utilizado para o consumo da API pública de cotações de moedas (AwesomeAPI).

* **PyAutoGUI:** Utilizado para a automação dos movimentos do mouse e simulação do teclado no sistema operacional.

## ⚙️ Como a Automação Funciona

1. O script realiza uma requisição HTTP `GET` para a API de moedas.

2. Os dados em formato JSON são filtrados para extrair os valores exatos de compra (bid) do Dólar e do Euro.

3. O código formata dinamicamente um relatório em texto.

4. A biblioteca assume o controle do sistema, abre o Bloco de Notas via menu Iniciar e digita o relatório caractere por caractere.

## 🚀 Como executar o projeto na sua máquina

1. Clone este repositório:

```
git clone https://github.com/DanielSoares45/automacao-cotacao.git

```

2. Acesse a pasta do projeto:

```
cd automacao-cotacao

```

3. Crie e ative um ambiente virtual:

```
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

```

4. Instale as dependências necessárias:

```
pip install requests pyautogui

```

5. Execute a automação (Atenção: solte o mouse e o teclado após pressionar Enter!):

```
python main.py

```

*Desenvolvido por **\[Daniel Soares\]** - Estudante de tecnologia em busca da primeira oportunidade como Estagiário em Desenvolvimento.*