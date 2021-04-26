import os
import pathlib
import os.path

print("*************************\n")
print("Churrascaria PYTHON CODE\n")
print("*************************\n")

def cadastro():
    
    nome = input('Insira o nome do cliente: ')
    cpf = input('CPF: ')
    credito = 0

    if(validaCadastro(cpf)):
        with open('.\cadastros\\' + cpf + '.txt', 'w') as arquivo:
            arquivo.write(nome.upper() + '\n')
            arquivo.write(cpf + '\n')
            arquivo.write(str(credito))
            print("Cadastro realizado com sucesso!")
    else:
        print("CPF INVALIDO OU JA CADASTRADO!")

def validaCadastro(cpf):

    if(len(cpf) == 11):
        try:
            with open("./cadastros/"+cpf+".txt", 'r') as f:
                return False
        except IOError:
            return True
    
def procuraCadastro():

    cpf = input("CPF: ")
    try:
        if(len(cpf) == 11):
            with open("./cadastros/"+cpf+".txt", 'r') as f:

                dados = f.readlines()
                print(f"Nome: {dados[0]}\nCPF:{dados[1]}\nCréditos:{dados[2]}")
                return True
        print("CPF INVALIDO")
        return False
    except IOError:
        print('Cadastro não encontrado')
        return False

def alteracaoCadastro():

    print("[1] Editar Cadastro\n[2] Excluir Cadastro")
    op = int(input())
    if(op == 1):
        
        cpf = procuraCadastro()
        if(cpf):

            print("[1] Alterar Nome\n[2] Alterar Crédito")
            op = int(input())
            if(op == 1):

                #Busca as informações de cpf e credito do cadastro
                with open("./cadastros/"+cpf+".txt", 'r') as f:
                    lines = f.readlines()
                    cpf_cadastro = lines[1]
                    credito = lines[2]
                #altera o nome e insere as informaçõe salvas anteriormente.
                with open("./cadastros/"+cpf+".txt", 'w') as f:
                    nome = input('Altere o nome: ')
                    f.write(nome.upper() + '\n')
                    f.write(cpf_cadastro)
                    f.write(credito)

            elif(op == 2):
                #Busca as informações de nome e cpf do cadastro
                with open("./cadastros/"+cpf+".txt", 'r') as f:
                    lines = f.readlines()
                    nome_cadastro = lines[0]
                    cpf_cadastro = lines[1]
                #altera o credito e insere as informaçõe salvas anteriormente.
                with open("./cadastros/"+cpf+".txt", 'w') as f:
                    novo_credito = input('Qual o valor do credito: ')
                    f.write(nome_cadastro.upper())
                    f.write(cpf_cadastro)
                    f.write(novo_credito)
            else:
                print("Opção Invalida!")
    elif(op==2):

        cpf_remove = input("Digite o CPF cadastrado para exclusão: ")
        try:
            os.remove("./cadastros/"+cpf_remove+'.txt')
            print("Removido com Sucesso")
            return True
        except IOError:
            print("ERRO! Não existe cadastro com esse CPF")
            return True
        
        
 
