import random, os

def read():
    list_palabras = []
    with open("./archivos/data1.txt", "r", encoding="utf-8") as f:
        for line in f:
            list_palabras.append(line)
        palabra = random.choice(list_palabras)
        doclines = palabra.splitlines()
        doc_rejoined = ''.join(doclines)
    return doc_rejoined

def dividir_palabra(palabra):
    palabra_dividia = {}
    for i, palabra in (enumerate(palabra)):
        if palabra != "\n":
            palabra_dividia[i] = palabra
    return palabra_dividia

def nueva_letra():
    letra = input("\nEscribe una letra: ")
    try:
        if len(letra) >= 2:
            raise ValueError("Sólo números naturales")
    except ValueError as e:
        print(e)
        return False
    return letra

def acomodar(palabra):
    hecho2 = {}
    for i in range(len(palabra)):
            hecho2[i] = "-"
    return hecho2

def run():

    palabra = read()
    acomodar_palabra = acomodar(palabra)

    while acomodar_palabra != dividir_palabra(palabra):

        print("Adivina la palabra\n")

        print(acomodar_palabra)

        letra = nueva_letra()

        for value in dividir_palabra(palabra):
            if dividir_palabra(palabra).get(value) == letra:
                acomodar_palabra[value] = letra

        # os.system("cls")

    print("Correcto, la palabra es", palabra)


if __name__ == "__main__":
    run()