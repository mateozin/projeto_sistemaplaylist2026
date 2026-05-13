from biblioteca import *
from musica import *
from fila import *
from faker import Faker
import os
import random
fake = Faker("pt_BR")
biblioteca = Biblioteca()
fila = Fila()
historico = Fila()
gerenciador = GerenciadorFila()
def adicionar_al(biblioteca, quantidade):
    generos =["Rock", "Pop", "Jazz", "Samba", "Forró", "MPB", "Metal", "Funk"]
    for _ in range(quantidade):
        titulo = fake.sentence(nb_words=3).rstrip(".")
        artista = fake.name()
        genero= random.choice(generos)
        bpm = random.randint(60,180)
        biblioteca.adicionar(titulo, artista, genero, bpm)
    print("Dados falsos criados com sucesso")

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
filas_criadas = False
menu="MENU PRINCIPAL \n1- Adicionar música a biblioteca\n2- Remover música da biblioteca\n3- Listar todas músicas na biblioteca\n4- Buscar música por ID\n5- Criar as filas de reprodução baseada no humor\n6- Reproduzir próxima música da fila\n7- Exibir fila de reprodução por humor\n8- Exibir histórico de reprodução\n9- Mostrar as estatísicas\n10- Gerar dados de músicas aleatórias com Faker\n0- Sair"
while True:
    print(menu)
    try:
        escolha=int(input("Escolha uma opção: "))
    except ValueError: 
        print("Isso não é um número válido")
        escolha=-1
    if escolha==1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("OK! Comece digitando o título da música e siga concedendo as informações necessitadas.")
        titulo=input("Título: ")
        artista=input("Artista: ")
        genero=input("Gênero: ")
        bpm = ver_bpm()
        m = biblioteca.adicionar(titulo, artista, genero, bpm)
    elif escolha==2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("OK! Digite o ID da musica que deseja remover da biblioteca")
        if biblioteca.vazia():
            print("Biblioteca vazia. Cancelando operação")
        else:
            verid=ver_id()
            if biblioteca.remover(verid):
                print(f"Música com o ID {verid} removida com sucesso.")
            else:
                print(f"Música com ID {verid} não encontrada.")
    elif escolha==3:
        os.system('cls' if os.name == 'nt' else 'clear')
        musicas = biblioteca.listar()
        if biblioteca.vazia():
            print("Biblioteca vazia")
        else:
            for m in musicas:
                print(f"{m}")
    elif escolha==4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("OK! Digite o id da música que deseja encontrar na biblioteca")
        verid=ver_id()
        ms = biblioteca.buscar_id(verid)
        if ms:
            print(f"Música encontrada: {ms}")
        else:
            print(f"Música com ID {verid} não encontrada")
    elif escolha==5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("OK! Montando filas de reprodução baseadas no humor")
        if biblioteca.vazia():
            print("Nenhuma fila criada, cancelando operação")
        else:
            gerenciador.montar(biblioteca)
            for humor in gerenciador.humores():
                fila = gerenciador.def_fila(humor)
                if fila:
                    print(f"Playlist {humor} com {fila.tamanho()} músicas")
            filas_criadas = True
            print("Playlist criada com sucesso.")
    elif escolha==6:
        os.system('cls' if os.name == 'nt' else 'clear')
        if filas_criadas == False:
            print("Nenhuma fila criada, cancelando operação")
        else:
            print("OK! Escolha qual fila deseja reproduzir")
            print(f"Humores: {gerenciador.humores()}")
            humor= input("Qual humor: ")
            fila = gerenciador.def_fila(humor)
            if fila is None:
                print("Humor inválido")
            elif fila.vazia():
                print("Fila vazia")
            else:
                m = fila.dequeue()
                if m:
                    historico.enqueue(m)
                    print(f"Reproduzindo {m}")
                    print(f"Histórico: {historico.tamanho()} faixas executadas")
    elif escolha==7:
        os.system('cls' if os.name == 'nt' else 'clear')
        if filas_criadas == False:
            print("Nenhuma fila criada, cancelando operação")
        else:
            print("OK! Apenas cite qual humor")
            print(f"Humores: {gerenciador.humores()}")
            humor = input("Qual humor: ")
            fila = gerenciador.def_fila(humor)
            if fila is None:
                print("Humor inválido")
            elif fila.vazia():
                print(f"Fila {humor} vazia.")
            else:
                musicas= fila.listar()
                print(f"Fila {humor} com {len(musicas)} músicas.")
                for i, m in enumerate(musicas,1):
                    print(f'Ordem {i} - ID {m}')
    elif escolha==8:
        os.system('cls' if os.name == "nt" else 'clear')     
        if historico.vazia():
            print("Histórico vazio, nenhuma musica reproduzida. Cancelando operação.")
        else:
            musicas = historico.listar()
            print(f"{len(musicas)} músicas reproduzidas:")
            for i, m in enumerate(musicas, 1):
                print(f"Executada em {i} - ID {m}")
    elif escolha==9:
        os.system('cls' if os.name == "nt" else 'clear')
        print("OK! Mostrando as estatísticas do usuário:")
        if biblioteca.vazia():
            print("Biblioteca vazia! Cancelando operação.")
        else:
            total = len(biblioteca.listar())
            if filas_criadas == False:
                print("Nenhuma fila criada, cancelando operação")
            else:
                print(f"Biblioteca tem no total {total} músicas.")
                for humor in gerenciador.humores():
                    fila_humor = gerenciador.def_fila(humor)
                    print(f"Fila {humor} está com {fila_humor.tamanho()} músicas")
            print(f'E já foram reproduzidas {historico.tamanho()} músicas.')
    elif escolha==10:
        os.system('cls' if os.name == "nt" else 'clear')
        print("OK! Criando 30 músicas aleatórias.")
        adicionar_al(biblioteca, 30)
    elif escolha==0:
        break


