from musica import Musica
class noLista:
    def __init__(self, musica: Musica):
        self.musica = musica
        self.proximo = None
class Biblioteca:
    def __init__(self):
        self._cabeca = None
        self._proximo_id = 1
    def adicionar(self, titulo: str, artista: str, genero: str, bpm:int):
        musica = Musica(self._proximo_id, titulo, artista, genero, bpm)
        self._proximo_id += 1
        novo = noLista(musica)
        if self._cabeca is None:
            self._cabeca = novo
        else:
            atual = self._cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo
        return musica
    def remover(self, id: int):
        atual = self._cabeca
        anterior = None
        while atual:
            if atual.musica.id == id:
                if anterior is None:
                    self._cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False
    def listar(self):
        musicas = []
        atual = self._cabeca
        while atual:
            musicas.append(atual.musica)
            atual = atual.proximo
        return musicas
    def buscar_id(self,id):
        atual = self._cabeca
        while atual:
            if atual.musica.id == id:
                return atual.musica
            atual = atual.proximo
        return None
    def vazia(self):
        return self._cabeca is None
    