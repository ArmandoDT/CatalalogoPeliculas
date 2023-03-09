from Dominio.Pelicula import Pelicula
from Servicio.Catalogo_peliculas import CatalogoPeliculas as cp

opcion = None

while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar películas')
        print('2. Listar peliculas')
        print('3. Eliminar catalogo de películas')
        print('4. salir')
        opcion = int(input('Escribe una opcion (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Proporcionar el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_pelicula()
        elif opcion == 3:
            cp.eliminar_pelicula()

    except Exception as e:
        print(f'Ocurrió un error {e}')

    else:
        print('Saliendo del programa...')
