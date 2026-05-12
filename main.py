from biblioteca import *
from musica import *

def ver_bpm():
    while True:
        try:
            bpm = input("BPM: ")
        except ValueError:
            print("Isso não é um número inteiro válido")
        bpm = int(bpm)
        if bpm <= 0:
            print("BPM deve ser maior que zero")
            continue
        return bpm
def ver_id():
    while True:
        try:
            id = input("ID da música: ")
        except ValueError:
            print("Isso não é um ID válido")
            id = -1
        id = int(id)
        return id

menu="MENU PRINCIPAL \n1- Adicionar música a biblioteca\n2- Remover música da biblioteca\n3- Listar todas músicas na biblioteca\n4- Buscar música por ID\n0- Sair"

biblioteca = Biblioteca()
while True:
    print(menu)
    try:
        escolha=int(input("Escolha uma opção: "))
    except ValueError: 
        print("Isso não é um número válido")
        escolha=-1
    if escolha==1:
        print("OK! Comece digitando o título da música e siga concedendo as informações necessitadas.")
        titulo=input("Título: ")
        artista=input("Artista: ")
        genero=input("Gênero: ")
        bpm = ver_bpm()
        m = biblioteca.adicionar(titulo, artista, genero, bpm)
    elif escolha==2:
        print("OK! Digite o ID da musica que deseja remover da biblioteca")
        if biblioteca.vazia():
            print("Biblioteca vazia")
        else:
            verid=ver_id()
            if biblioteca.remover(verid):
                print(f"Música com o ID {verid} removida com sucesso.")
            else:
                print(f"Música com ID {verid} não encontrada.")
    elif escolha==3:
        musicas = biblioteca.listar()
        if biblioteca.vazia():
            print("Biblioteca vazia")
        else:
            for m in musicas:
                print(f"{m}")
    elif escolha==4:
        print("OK! Digite o id da música que deseja encontrar na biblioteca")
        verid=ver_id()
        ms = biblioteca.buscar_id(verid)
        if ms:
            print(f"Música encontrada: {ms}")
        else:
            print(f"Música com ID {verid} não encontrada")
    elif escolha==0:
        break


