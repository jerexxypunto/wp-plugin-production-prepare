import argparse
import os

import shutil

## Función que clona un directorio y su contenido en un folder llamado temp
def clonar_directorio(ruta, dest):
    shutil.copytree(ruta, dest)


## Función que busca en ruta un folder llamado node_modules y lo elimina del folder que fue proporcionado por el parametro.
def delete_in_folder(ruta, subcjet):
    for root, dirs, files in os.walk(ruta):
        if subcjet in dirs:
            shutil.rmtree(os.path.join(root, subcjet))




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ruta", help="Imprime la ruta proporcionada")
    parser.add_argument("--destino", help="Nombre del folder de destino")
    args = parser.parse_args()

    destino = args.destino

    print("Clonando proyecto...")

    clonar_directorio(args.ruta, destino)

    print("Proyecto cloando...")

    print("Eliminado .git...")
    delete_in_folder(destino, '.git/')
    
    print("Eliminado node_modules...")
    delete_in_folder(destino, 'node_modules')

    print("Eliminado js/src ...")
    delete_in_folder(f"{destino}/js/" , "src")


    print(f"Comprimiendo {destino}")
    shutil.make_archive(destino, 'zip', destino)

    print("Eliminando el folder destino...")
    shutil.rmtree(destino)
    
    print("Exito")

if __name__ == "__main__":
    main()
