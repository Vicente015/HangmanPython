import random
import string
from palabras import listapalabras
from diagramas import vidas_visual

def palabra_valida():
  palabra = random.choice(listapalabras)
  
  while '_' in palabra or ' ' in palabra:
    palabra = random.choice(listapalabras)

  return palabra.upper()

def ahorcado():
  print("=========================")
  print("   Juego del ahorcado    ")
  print("=========================")

  palabra = palabra_valida()
  por_adivinar  = set(palabra)
  adivinadas    = set()
  abecedario    = set(string.ascii_uppercase)

  vidas = 7

  while len(por_adivinar) > 0 and vidas > 0:
    print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(adivinadas)}")

    lista = [letra if letra in adivinadas else '_' for letra in palabra]
    print(vidas_visual[vidas])
    print(f"Palabra: {' '.join(lista)}")
    
    letra = input("Introduce una letra: ")
   
    # Si la letra está en el abecedario y no está en el conjunto de letras que ha usado
    # Se añade al conjunto de letras usadas
    if letra in abecedario - adivinadas:
      adivinadas.add(letra)

      # Si la letra está en la palabra a adivinar
      if letra in por_adivinar:
        por_adivinar.remove(letra)
        print('')
      else:
        vidas = vidas - 1
        print(f"\nLa letra {letra} no está en la palabra.")
    elif letra in adivinadas:
      print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
    else:
      print("\nLetra no válida.")

  if vidas == 0:
    print(vidas_visual[vidas])
    print(f"¡Ahorcado! Perdiste jaja. La palabra era: {palabra}")
  else:
    print(f"¡Excelente! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Advinaste la palabra {palabra}")

ahorcado()