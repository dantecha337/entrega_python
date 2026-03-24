import random

categorias= {
    "programacion": ["python", "variable","funcion","programa","bucle","lista","entero","cadena"],
    "futbolistas argentinos": ["messi","maradona","batistuta","riquelme","di maria", "tevez", "kempes", "redondo"],
    "bandas argentinas": ["soda estereo","patricio rey", "los piojos", "la renga", "babasonicos", "los abuelos de la nada", "rata blanca", "viejas locas"]
}

lista_categorias= list(categorias.keys())

#Imprime cada categoria con un numero para seleccionar
for i in range(len(lista_categorias)):
    print(f"{i+1} - {lista_categorias[i]}")

#Valida que el numero elegido sea una opcion valida
while True:
    numero=int(input("Seleccione una opcion: "))
    if numero<1 or numero>len(lista_categorias):
        print("Opcion invalida, eliga de nuevo")
    else:  
        break

eleccion= lista_categorias[numero-1]

word = random.choice(categorias[eleccion])
guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!")
print()

puntaje=0

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:

        #Agregue esta validacion ya que algunas palabras que puse tenian espacios
        if letter == " ":
            progress+= "  "
        elif letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        puntaje+=6
        break
    
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    
    #Agrego el lower para que se puedan poner mayusculas
    letter = input("Ingresá una letra: ").lower()
    
    #Verifica que sea una letra y que no haya mas de una
    if len(letter)!=1 or not letter.isalpha():    
        print("Entrada no valida")
        print()
        continue
    
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje-=1
        print("Esa letra no está en la palabra.")
    
    print()

else:
    print(f"¡Perdiste! La palabra era: {word}")
    puntaje=0

print(f"Puntaje conseguido: {puntaje}")