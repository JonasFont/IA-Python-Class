#------------------------Exemplo 2-------------------------------

class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}"


# Criar uma instância da classe Carro
meu_carro = Carro("Toyota", "Corolla", "Prata")


# Imprimir o status do carro
print(meu_carro.status())  # Saída: Marca: Toyota, Modelo: Corolla, Cor: Prata, Velocidade: 50 km/h



#--------------------------------Exemplo 2------------------------------
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

    def fazer_aniversario(self):
        self.idade += 1

# Criar uma instância da classe Pessoa
pessoa1 = Pessoa("João", 30)

# Acessar atributos e chamar métodos da instância
print(pessoa1.cumprimentar())  # Saída: Olá, meu nome é João e eu tenho 30 anos.
pessoa1.fazer_aniversario()  # Incrementa a idade em 1
print(pessoa1.idade)  # Saída: 31


