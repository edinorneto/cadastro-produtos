# cadastro-produtos

Projeto simples feito em Python para cadastrar produtos pelo terminal e salvar tudo em um arquivo JSON.

- Permite cadastrar produtos com nome, descrição, preço, categoria, estoque, etc.
- Cada produto recebe um ID automaticamente.
- Os dados ficam salvos no arquivo `cadastro_produtos.json` na mesma pasta do projeto.

### Estrutura do projeto

- `main.py`: onde roda o programa principal
- `data.py`: funções para ler/gravar o JSON
- `config.py`: só o nome do arquivo de dados
- `interface.py`: onde ficam as perguntas pro usuário


## Talvez seja necessário instalar o pacote `tzdata` no terminal:
```
   pip install tzdata
```
