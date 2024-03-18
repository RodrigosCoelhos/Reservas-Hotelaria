
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print()
print("                               Bem vindo ao                                 ")
print()
print("                          ***** Plaza Hotel *****                          " )
print()
print("                        - Gerenciador de Reservas -                         ")
print()
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print()
print("                      Preencha o formulário de reserva                      ")
print()
print("----------------------------------------------------------------------------")
print()

# Classe Pessoa

class Pessoa:
    def __init__(self, nome: str, idade: int, nacionalidade: str, telefone: str, email: str) -> None:
        self.nome: str = nome
        self.idade: int = idade
        self.nacionalidade: str = nacionalidade
        self.__telefone: str = telefone
        self.__email: str = email
    
    def mostrar_detalhes(self):
        print(f"Nome: {self.nome} \nNacionalidade: {self.nacionalidade} \nE-mail: {self.email} \nTelefone: {self.telefone}")

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    def set_nacionalidade(self, nacionalidade):
        self.nacionalidade = nacionalidade

    def get_nacionalidade(self):
        return self.nacionalidade

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_telefone(self, telefone):
        self.telefone = telefone

    def get_telefone(self):
        return self.telefone
    
# Fim Classe Pessoa


# Classe Cliente

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, nacionalidade: str, telefone: str, email: str) -> None:
        super().__init__(nome, idade, nacionalidade, telefone, email)
        self.__idade: int = idade
        self.__telefone: str = telefone
        self.__email: str = email

    def mostrar_detalhes(self):
        super().mostrar_detalhes()

# Preenchimento dados do cliente - formulário de reserva
nome_do_cliente = input("Nome do cliente: ")
print()
idade_do_cliente = input("Idade: ")
print()
nacionalidade_do_cliente = input("Nacionalidade: ")
print()
email_do_cliente = input("E-mail: ")
print()
telefone_do_cliente = input("Tel.: ")
print()

# Fim Classe Cliente
        

# Preenchimento data de check-in e check-out das reservas
import datetime

while True:
    check_in = input("Check-in data (AAAA-MM-DD):")
    print()
    check_out = input("Check-out data (AAAA-MM-DD): ")
    print()
    try:
        ano_in, mes_in, dia_in = map(int, check_in.split("-"))
        ano_out, mes_out, dia_out = map(int, check_out.split("-"))
        check_in_objeto = datetime.datetime(ano_in, mes_in, dia_in)
        check_out_objeto = datetime.datetime(ano_out, mes_out, dia_out)
        if check_out_objeto < check_in_objeto:
            print("A data de check-out deve ser posterior à data de check-in. Tente novamente.")
            print()
            continue
        break
       
    except ValueError:
        print("Dados incorretos, digite datas válidas.")
        print()

print()

# Fim Preenchimento data de check-in e check-out das reservas


# Classe Quarto  

class Quarto:
    def __init__(self, tipo_quarto, livre=True):
        self.tipo_quarto = tipo_quarto
        self.livre = livre

class Hotel:
    def __init__(self):
        self.quartos = [Quarto('single') for _ in range(5)] + [Quarto('duplo') for _ in range(5)] + [Quarto('suíte') for _ in range(2)]

    def alocacao_quartos(self, tipo_quarto):
        for quarto in self.quartos:
            if quarto.tipo_quarto == tipo_quarto and quarto.livre:
                quarto.livre = False
                print()
                if tipo_quarto == "single":
                    return f"quarto Nº {self.quartos.index(quarto) + 100} reservado"
                if tipo_quarto == "duplo":
                    return f"quarto Nº {self.quartos.index(quarto) + 200} reservado"
                if tipo_quarto == "suíte":
                    return f"quarto Nº {self.quartos.index(quarto) + 300} reservado"
        print()    
        return "Quartos indisponíveis."

hotel = Hotel()

while True:
    tipo_quarto = input("Escolha o tipo de quarto | single | duplo | suíte |: ")
    resultado_alocacao = hotel.alocacao_quartos(tipo_quarto)
    print(resultado_alocacao)
    print()
    if resultado_alocacao == "Todos os quartos estão ocupados.":
        break
    print()
    outro_quarto = input("Deseja outro quarto a mais? (s/n): ")
    print()
    if outro_quarto.lower() == 'n':
        break

# Fim Classe quarto


# Gerador de ID da reserva

import random
id_aleatorio = random.randint(0, 10000)
print("Reserva realizada com sucesso !")
print()

reserva = print(f"Reserva ID: {id_aleatorio} em nome de: {nome_do_cliente} para categoria {tipo_quarto} - {resultado_alocacao}, Check-in: {check_in_objeto}, Check-out: {check_out_objeto}")
print()

def list_variables_info():
    for id_aleatorio, nome_do_cliente, tipo_quarto, resultado_alocacao, check_in_objeto, check_out_objeto in globals().items():
     print(f"Reserva ID: {id_aleatorio} em nome de: {nome_do_cliente} para categoria {tipo_quarto} - {resultado_alocacao}, Check-in: {check_in_objeto}, Check-out: {check_out_objeto}")
print()

# >>>>>>>>>>>>>>>>>>> Looping para realizar outra reserva <<<<<<<<<<<<<<<<<<<<

while True:
    resposta = input("Deseja realizar outra reserva ? (s/n):")
    print()
    if resposta == "s":
        class Cliente(Pessoa):
            def __init__(self, nome: str, idade: int, nacionalidade: str, telefone: str, email: str) -> None:
                super().__init__(nome, idade, nacionalidade, telefone, email)
                self.__idade: int = idade
                self.__telefone: str = telefone
                self.__email: str = email

    

            def mostrar_detalhes(self):
                super().mostrar_detalhes()

        # Preenchimento dados do cliente - formulário de reserva
        nome_do_cliente = input("Nome do cliente: ")
        print()
        idade_do_cliente = input("Idade: ")
        print()
        nacionalidade_do_cliente = input("Nacionalidade: ")
        print()
        email_do_cliente = input("E-mail: ")
        print()
        telefone_do_cliente = input("Tel.: ")
        print()

# Fim Classe Cliente
            

# Preenchimento data de check-in e check-out das reservas
        import datetime

        while True:
            check_in = input("Check-in data (AAAA-MM-DD):")
            print()
            check_out = input("Check-out data (AAAA-MM-DD): ")
            print()
            try:
                ano_in, mes_in, dia_in = map(int, check_in.split("-"))
                ano_out, mes_out, dia_out = map(int, check_out.split("-"))
                check_in_objeto = datetime.datetime(ano_in, mes_in, dia_in)
                check_out_objeto = datetime.datetime(ano_out, mes_out, dia_out)
                if check_out_objeto < check_in_objeto:
                    print("A data de check-out deve ser posterior à data de check-in. Tente novamente.")
                    print()
                    continue
                break
            
            except ValueError:
                print("Dados incorretos, digite datas válidas.")
                print()

        print()

# Fim Preenchimento data de check-in e check-out das reservas


# Classe Quarto  

        class Quarto:
            def __init__(self, tipo_quarto, livre=True):
                self.tipo_quarto = tipo_quarto
                self.livre = livre

        class Hotel:
            def __init__(self):
                self.quartos = [Quarto('single') for _ in range(5)] + [Quarto('duplo') for _ in range(5)] + [Quarto('suíte') for _ in range(2)]

            def alocacao_quartos(self, tipo_quarto):
                for quarto in self.quartos:
                    if quarto.tipo_quarto == tipo_quarto and quarto.livre:
                        quarto.livre = False
                        print()
                        if tipo_quarto == "single":
                            return f"quarto Nº {self.quartos.index(quarto) + 100} reservado"
                        if tipo_quarto == "duplo":
                            return f"quarto Nº {self.quartos.index(quarto) + 200} reservado"
                        if tipo_quarto == "suíte":
                            return f"quarto Nº {self.quartos.index(quarto) + 300} reservado"
                print()    
                return "Quartos indisponíveis."

        hotel = Hotel()

        while True:
            tipo_quarto = input("Escolha o tipo de quarto | single | duplo | suíte |: ")
            resultado_alocacao = hotel.alocacao_quartos(tipo_quarto)
            print(resultado_alocacao)
            print()
            if resultado_alocacao == "Todos os quartos estão ocupados.":
                break
            print()
            outro_quarto = input("Deseja outro quarto a mais? (s/n): ")
            print()
            if outro_quarto.lower() == 'n':
                break

# Fim Classe quarto


# Gerador de ID da reserva

        import random
        id_aleatorio = random.randint(0, 10000)
        print("Reserva realizada com sucesso !")
        print()

        reservas = print(f"Reserva ID: {id_aleatorio} em nome de: {nome_do_cliente} para categoria {tipo_quarto} - {resultado_alocacao}, Check-in: {check_in_objeto}, Check-out: {check_out_objeto}")
        print()

            


    elif resposta == "n":
        print("Obrigado por reservar conosco !")
        break

    else:
        print("Resposta inválida, digite s ou n.")
        print()

# >>>>>>>>>>>>>>>>>>> Fim do Looping para realizar outra reserva <<<<<<<<<<<<<<<<<<<<


# Classe reserva

class Reserva:
    def __init__(self, id_aleatorio):
        self.id_aleatorio = id_aleatorio

    def __init__(self):
        self.reservas = []

    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)

reservas =()
reservas.mostrar_detalhes()
        
# Fim Classe reserva


# Classe Funcionario
class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, ordenado: float,  telefone: str, email: str) -> None:
        super().__init__(nome, idade, ordenado, telefone, email)
        self.ordenado: float = ordenado
        self.telefone: str = telefone
        self.email: str = email


emp1 = Funcionario("Marcos", 35, 3000, "+351 925 431 578", "marcos@hotelplaza.com")
print(f"Nome: {emp1.nome}")
print(f"Idade: {emp1.idade}")
print(f"Ordenado: {emp1.ordenado}")
print(f"Telefone: {emp1.telefone}")
print(f"E-mail: {emp1.email}")
emp1.mostrar_detalhes()

# Fim Classe Funcionario



# Testes

import unittest

class Cliente:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

class TestCliente(unittest.TestCase):
    def test_increment(self):
        obj = Cliente(0)
        obj.increment()
        self.assertEqual(obj.value, 1)

if __name__ == '__main__':
    unittest.main()


class Funcionario:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

class TestFuncionario(unittest.TestCase):
    def test_increment(self):
        obj = Funcionario(0)
        obj.increment()
        self.assertEqual(obj.value, 1)

if __name__ == '__main__':
    unittest.main()

class Quarto:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

class TestQuarto(unittest.TestCase):
    def test_increment(self):
        obj = Quarto(0)
        obj.increment()
        self.assertEqual(obj.value, 1)

if __name__ == '__main__':
    unittest.main()

class Reserva:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

class TestReserva(unittest.TestCase):
    def test_increment(self):
        obj = Reserva(0)
        obj.increment()
        self.assertEqual(obj.value, 1)

if __name__ == '__main__':
    unittest.main()


