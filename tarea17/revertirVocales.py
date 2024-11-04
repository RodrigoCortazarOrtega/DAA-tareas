

def revertirVocales(s: str) -> str:
    v = {"a": "a", "e": "e", "i": "i", "o": "o", "u": "u",
         "A": "A", "E": "E", "I": "I", "O": "O", "U": "U"}
    # Convertimos la cadena en una lista de caracteres(Debido a que los string son inmutables)
    s = list(s)
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] not in v: #Si la llave no esta en el diccionario
            i += 1
        elif s[j] not in v:
            j -= 1
        else:
            # Intercambiamos las vocales
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    # Convertimos la lista de vuelta a cadena
    return ''.join(s)
# Prueba de la función
print(revertirVocales("Lapiz"))
print(revertirVocales("Icecream"))