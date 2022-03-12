# MODULO DE CADASTRO DE LOGIN
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso
# Created Date: Mar-2022
# version ='1.0'
# ---------------------------------------------------------------------------
from cores import Cores as cor
import time
import pandas as pd
from IPython.display import display


class LoginExcel:
    # INICIAR O DATAFRAME
    def __init__(self):
        self.i9ti = pd.read_excel("i9ti.xlsx")
        self.dt_original = pd.DataFrame(self.i9ti)  # DA PLANILHA ELE CRIA UM DATAFRAME
        self.nome_login = self.dt_original["LOGIN"]  # LISTA DE USUARIOS
        self.senha_login = self.dt_original["SENHA"]  # LISTA DE SENHAS

    def localizar_login(self, usuario):
        self.encontrado = 0
        self.usuario = usuario
        # VARRE LISTA DE LOGIN
        for i, nome in enumerate(self.nome_login):
            if nome == self.usuario:
                print(f"{cor.vermelho}JA EXISTE ESTE LOGIN CADASTRADO.{cor.normal}")
                self.encontrado = 1
                break
        return self.encontrado

    def valida_telefone(self):
        validado = False
        while validado == False:
            while True:
                tel = input(f"{cor.azul}Digite o telefone do cliente. EX 1699998888: {cor.normal}")
                try:
                    tel = int(tel)
                    break
                except:
                    print(f"{cor.vermelho}Digite apenas telefone numeros EX. 16999998888.{cor.normal} ")
                    continue
            telefone = str(tel)
            telefone = (f"({telefone[0:2]}){telefone[2:7]}-{telefone[7:11]}")
            print(f"{cor.azul}Confirma o telefone {telefone}{cor.normal} ?")
            telefone_verifica = input(f"{cor.azul}SIM OU NÃO? -> S/N: {cor.normal}").lower()
            if telefone_verifica[0] == "s":
                validado = True
            else:
                continue
        return telefone

    def cadastra_login(self):
        # PREENCHE OS CAMPOS DE LOGIN
        nome = input(f"{cor.azul}Digite o nome do cliente: {cor.normal}").upper()
        email = input(f"{cor.azul}Digite o email do cliente: {cor.normal}").lower()
        # TRECHO DO TELEFONE
        telefone = self.valida_telefone()
        # FIM DA VALIDAÇÃO
        login = self.usuario.lower()
        print(f"{cor.vermelho}ATENÇÃO DIGITE AGORA A SENHA DO LOGIN {cor.azul}{login}{cor.normal}.")
        time.sleep(2)
        senha = input(f"{cor.azul}Digite a senha do login: {cor.normal}").lower()
        # CRIA O DICIONARIO SEMPRE COM COLCHETES
        self.dt = {"NOME": [nome], "EMAIL": [email], "TELEFONE": [telefone], "LOGIN": [login], "SENHA": [senha]}
        self.dt_concatenar = pd.DataFrame(self.dt)  # CRIA NOVO DATAFRAME
        #######################################################
        print(f"{cor.azul}CADASTRANDO O USUARIO ABAIXO:{cor.normal}")
        display(self.dt_concatenar)
        time.sleep(3)

        # CONCATENA OS DOIS DATAFREAMES COM COLCHETES
        self.dt_concatenado = pd.concat([self.dt_original, self.dt_concatenar])
        ########################################################

        # display(self.dt_concatenado) #VERIFICAÇÃO DO DT COMPLETO

        # CRIA A PLANILHA EXCEL DO DATAFRAME CONCATENADO, INDICE FALSO
        self.dt_concatenado.to_excel("i9ti.xlsx", index=False)
        print(cor.azul + "CADASTRO FINALIZADO COM SUCESSO." + cor.normal)

    def fazer_login(self, user, senha):
        tamanho_usuario = len(self.nome_login)
        tamanho_senha = len(self.senha_login)
        status = "VERIFICANDO"
        if tamanho_senha == tamanho_usuario:
            for i in range(0, (tamanho_senha - 1)):
                if self.nome_login[i] == user and self.senha_login[i] == senha:
                    print(50*f"{cor.azul}-")
                    print(f"{cor.azul}BEM VINDO {self.dt_original['NOME'][i]}")
                    print(50 * "-")
                    status = "LOGADO NO SISTEMA"
                    break
                status = f"{cor.vermelho}ERRO DE LOGIN."
        else:
            print("OCOREEU ERRO NO SISTEMA....")
        return status


if __name__ == "__main__":
    usuario1 = LoginExcel()
    print(30 * f"{cor.verde}-")
    print("MENU DE SELEÇÃO DO SISTEMA")
    print(" 1 - CADASTRO DE LOGIN.")
    print(" 2 - ACESSAR O SISTEMA.")
    print(" 3 - SAIR DO SISTEMA.")
    print(30 * f"-{cor.normal}")
    sistema = int(input("DIGITE A OPÇÃO VALIDA: "))

    if sistema == 1:
        print(50 * f"{cor.azul}-")
        print("CADASTRAR LOGIN")
        print(50*"-")
        while True:
            nome_login = input(f"{cor.azul}Digite o nome para login: {cor.normal}").lower()
            verifica = usuario1.localizar_login(nome_login)
            if verifica == 0:
                break
            else:
                print(f"{cor.azul}Digite outro usuario de login...{cor.normal}")
                time.sleep(3)
                continue
        usuario1.cadastra_login()

    if sistema == 2:
        print(50 * f"{cor   .verde}-")
        print("SISTEMA DE LOGIN")
        print(50 * "-")
        while True:
            n_user = input("DIGITE O USUARIO PARA LOGIN: ").lower()
            s_senha = input("DIGITE A SENHA PARA LOGIN: ").lower()
            print(f"Usuario {n_user} e Senha {s_senha} digitados.")
            valida = input("CONFIRMA S/N: ").lower()
            if valida[0] == "s":
                break
            else:
                print("REDIGITE USUARIO E SENHA")
                continue
        print(usuario1.fazer_login(n_user, s_senha))
    if sistema == 3:
        print("FINALIZADO")
