# Ejercicio 2 - Contar palabras en un archivo
def count_words(filename):
    word_counts = {}
    with open(filename, 'r') as file:
        contenido = file.read()
        palabras = contenido.lower().split()
        for palabra in palabras:
            if palabra in word_counts:
                word_counts[palabra] += 1
            else:
                word_counts[palabra] = 1
    return word_counts
