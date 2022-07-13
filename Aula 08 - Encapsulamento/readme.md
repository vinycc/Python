# Encapsulamento

- O encapsulamento restringe o acesso aos atributos e métodos de uma classe
- Evita que atributos específicos de uma classe possam ser acessado diretamente
- Em Python, ao aplicar o conceito de encapsulamento, os atributos e métodos da classe podem ser:
  - **Públicos:** Podem ser acessados diretamente 
  - **Privados:** Não podem ser acessados diretamente

## Sintaxe em Python

- Atributos e métodos privados devem ter seus nomes iniciados por dois sublinhados 

```
class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        # atributos publicos
            self.nome = nome
            self.idade = idade
        # atributos privados
            self.__cpf = cpf
            self.__rg = rg
```

- Os atributos e métodos privados não podem ser acessados fora da classe.

```
class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        # atributos publicos
            self.nome = nome
            self.idade = idade
        # atributos privados
            self.__cpf = cpf
            self.__rg = rg
            
pessoa1 = Pessoa("João", 25, "11111111111", "3333333")
pessoa1.idade = 26                      # Altera a idade
pessoa1.__cpf = "22222222"              # ERRO
print(pessoa1.__rg)                     # ERRO
```


