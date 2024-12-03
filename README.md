# Sistema de Cadastro de Animais

## Descrição
Um sistema de cadastro de animais utilizando Python e Tkinter. O projeto permite cadastrar animais (cachorros e gatos) com atributos como nome, idade, porte (para cachorros) e raça (para gatos), e listar todos os animais cadastrados em uma interface gráfica.

## Instalação
1. Certifique-se de ter o Python instalado em seu sistema. Você pode baixar o Python [aqui](https://www.python.org/downloads/).
2. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```
3. Instale os pacotes necessários:
    ```bash
    pip install tk
    ```

## Uso
Para iniciar o sistema de cadastro de animais, execute o arquivo `main.py`:
```bash
python main.py

Cadastro de Animais
Vá para a aba "Cadastro".

Preencha os campos "Nome", "Idade", selecione o "Tipo" (Cachorro ou Gato) e preencha o campo "Porte (para Cachorro) ou Raça (para Gato)".

Clique no botão "Cadastrar".

Uma mensagem de sucesso será exibida se o cadastro for bem-sucedido.

Lista de Animais
Vá para a aba "Lista de Animais".

Verifique os animais cadastrados com os detalhes corretos.

```

## Estrutura do Projeto


├── animal.py          # Classe abstrata Animal

├── cachorro.py        # Classe Cachorro que herda de Animal

├── gato.py            # Classe Gato que herda de Animal

├── main.py            # Interface gráfica com Tkinter

└── README.md          # Documentação do projeto

## Autores

>Lucas Rocha - LucasRocha-CMD
