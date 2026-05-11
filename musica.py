class Musica:
    def __init__(self, id: int, titulo: str, artista: str, genero: str, bpm: int):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def __str__(self):
        return f"{self.id} | {self.titulo} - {self.artista} \nGÊNERO: {self.genero} \nBPM: {self.bpm}"