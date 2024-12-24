import pyfiglet

def crear_banner(titulo, subtitulo):
    banner = pyfiglet.figlet_format(titulo)
    print(banner)
    print(f"{subtitulo.center(len(banner.splitlines()[0]))}")

def presentacion():
    # Llamar a la función con el texto deseado
    crear_banner("MEDINAS S.A.", ">> echo La mejor tienda online")