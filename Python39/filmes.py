class Filme:
    def init(self,titulo,genero) :
        self.__titulo = titulo
        self.__genero = genero
    
    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero
    
    def set_titulo(self,titulo):
        self.__titulo = titulo
        return titulo

    def set_genero(self,genero):
        self.__genero = genero
        return genero


#programa principal
lista_filmes = []

for i in range(3):
    titulo = input("Titulo-")
    genero = input("Gênero-")
    filme = Filme(genero, titulo)
    lista_filmes.append(filme)

for filme in lista_filmes: 
    print('_' * 30)
    print("Titulo:", filme.get_titulo())
    print("Genero:", filme.get_genero())
