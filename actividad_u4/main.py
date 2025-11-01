from artista.cantante import Cantante
from artista.banda import Banda
from artista.dj import Dj 

def iniciar_festival(lista_artistas):
    print("\n=====Comienza la fiesta!======= ")
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar() 
        artista.despedirse()
        print("================Fin de la actuación ======================")
    print("Se termino el festival! Gracias por veinr :D")

def main():
    lista_artistas = []
    try:
        num_artistas=int(input("Cuantos artistas se presentarán en el festival?"))
    except ValueError:
        print("Error: Debes ingresar un número")
        return

    for i in range(num_artistas):
        print(f"\n=== Datos del Artista #{i+1} ===")
        print("Que tipo de artista es?")
        print("1: Cantante")
        print("2: DJ")
        print("3: Banda")
        tipo=input("Escoge 1, 2, o 3:")

        if tipo not in ["1", "2", "3"]:
            print("Tipo no válido. Se omitirá este artista.")
            continue 

        nombre=input("Ingresa el nombre del artista:")
        genero=input("Ingresa el género musical: ")
        popularidad=0
        while popularidad<=0 or popularidad>100:
            try:
                popularidad = int(input("Que Popularidad tiene? (1-100): "))
            except ValueError:
                print("Ingresa un número entre el 0 y 100.")
        try:
            if tipo =="1":
                cancion=input("Ingresa la canción más popular del cantante: ")
                nuevo_artista=Cantante(nombre, genero, popularidad, cancion)
            
            elif tipo =="2":
                estilo=input("Ingresa el estilo de mezcla (ejemplo: Techno, house, etc): ")
                nuevo_artista=Dj(nombre, genero, popularidad, estilo) 

            elif tipo == "3":
                integrantes=int(input("Ingresa el número de integrantes de la banda: "))
                nuevo_artista=Banda(nombre, genero, popularidad, integrantes)

            lista_artistas.append(nuevo_artista)
            print(f"{nombre} ha sido añadido al festival!")
        except ValueError:
            print("Error en los datos ingresados se va a omitir este artista")
            continue

    if lista_artistas: 
        iniciar_festival(lista_artistas)
    else:
        print("No hay artistas. El festival queda cancelado")
if __name__=="__main__":
    main()