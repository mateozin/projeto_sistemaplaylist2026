from musica import *
class noFila:
    def __init__(self, musica):
        self.musica= musica
        self.proximo = None
class Fila:
    def __init__(self):
        self._frente= None
        self._tras = None
        self._tamanho = 0
    def enqueue(self,musica):
        novo = noFila(musica)
        if self._tras is None:
            self._frente = novo
            self._tras = novo
        else:
            self._tras.proximo = novo
            self._tras = novo
        self._tamanho += 1
    def vazia(self):
        return self._frente is None
    def dequeue(self):
        if self.vazia():
            return None
        musica = self._frente.musica
        self._frente = self._frente.proximo
        if self._frente is None:
            self._tras = None
        self._tamanho -= 1
        return musica
    def tamanho(self) -> int:
        return self._tamanho
    def listar(self):
        musicas = []
        atual = self._frente
        while atual:
            musicas.append(atual.musica)
            atual = atual.proximo
        return musicas
def hum_intenso(bpm):
    return bpm > 160
def hum_agitado(bpm):
    return 120 < bpm <= 160
def hum_concentracao(bpm):
    return 80 < bpm <= 120
def hum_tranquilo(bpm):
    return bpm <= 80
humores={"Relaxar": hum_tranquilo,"Focar": hum_concentracao,"Animar": hum_agitado, "Treinar": hum_intenso,}

class GerenciadorFila:
    def __init__(self):
        self.fila_intenso = Fila()
        self.fila_agitado = Fila()
        self.fila_concentracao = Fila()
        self.fila_tranquilo = Fila()
    def montar(self, biblioteca):
        self.fila_intenso = Fila()
        self.fila_agitado = Fila()
        self.fila_concentracao = Fila()
        self.fila_tranquilo = Fila()
        for musica in biblioteca.listar():
            if hum_intenso(musica.bpm):
                self.fila_intenso.enqueue(musica)
            elif hum_agitado(musica.bpm):
                self.fila_agitado.enqueue(musica)
            elif hum_concentracao(musica.bpm):
                self.fila_concentracao.enqueue(musica)
            elif hum_tranquilo(musica.bpm):
                self.fila_tranquilo.enqueue(musica)
    def def_fila(self, humor):
        if humor == "Treinar":
            return self.fila_intenso
        if humor == "Animar":
            return self.fila_agitado
        if humor == "Focar":
            return self.fila_concentracao
        if humor == "Relaxar":
            return self.fila_tranquilo
    def humores(self):
        return "Treinar", "Animar", "Focar", "Relaxar"