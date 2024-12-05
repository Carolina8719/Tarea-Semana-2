
#TAREA SEMANA 2
#EJERCICIO 

import random

# juego de "Adivina el Número"
class AdivinaElNumero:

    # rango de números y el número de intentos
    def __init__(self, rango_minimo=1, rango_maximo=15, intentos_maximos=3):
        self.rango_minimo = rango_minimo  # mínimo del rango
        self.rango_maximo = rango_maximo  # máximo del rango
        self.intentos_maximos = intentos_maximos  # Número máximo de intentos permitidos
        self.numero_secreto = random.randint(self.rango_minimo, self.rango_maximo)  # Número secreto aleatorio
        self.intentos_restantes = self.intentos_maximos  # intentos restantes

    # comienza el juego
    def jugar(self):
        print("¡Bienvenido al juego de Adivina el Número!")
        print(f"Estoy pensando en un número entre {self.rango_minimo} y {self.rango_maximo}. Tienes {self.intentos_maximos} intentos para adivinarlo.")
        
        while self.intentos_restantes > 0:
            try:
                # jugador debe ingresar un número
                intento = int(input(f"\nTienes {self.intentos_restantes} intentos restantes. Ingresa un número: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            # Revisando si el número es correcto
            if intento == self.numero_secreto:
                print(f"¡Felicidades! Has adivinado el número secreto {self.numero_secreto} correctamente.")
                break
            elif intento < self.numero_secreto:
                print("El número secreto es mayor. Intenta de nuevo.")
            else:
                print("El número secreto es menor. Intenta de nuevo.")
            
            # Indicar los intentos restantes
            self.intentos_restantes -= 1
        
        # Si se han agotado los intentos, el jugador ha perdido
        if self.intentos_restantes == 0:
            print(f"\n¡Se acabaron los intentos! El número secreto era {self.numero_secreto}. ¡Mejor suerte la próxima vez!")

# estadísticas del jugador
class Jugador:
    
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del jugador
        self.puntuacion = 0    # Puntuación inicial del jugador
    
    # Método para mostrar el puntaje del jugador
    def mostrar_puntuacion(self):
        print(f"\nPuntuación de {self.nombre}: {self.puntuacion} puntos.")
    
    # Método para actualizar la puntuación del jugador
    def actualizar_puntuacion(self, puntos):
        self.puntuacion += puntos


# Función principal que ejecuta el juego
def iniciar_juego():
    # Pide el nombre del jugador
    nombre = input("Ingresa tu nombre: ")
    
    # Crea una instancia del jugador
    jugador = Jugador(nombre)

    # Inicia el juego de adivinar el número
    juego = AdivinaElNumero(rango_minimo=1, rango_maximo=100, intentos_maximos=10)
    
    # Ejecuta el juego
    juego.jugar()
    
    # Si el jugador adivina el número, se le otorgan puntos
    if juego.intentos_restantes > 0:
        jugador.actualizar_puntuacion(10)  # Otorga 10 puntos por adivinar el número
    
    # Muestra la puntuación final del jugador
    jugador.mostrar_puntuacion()

# Ejecuta el juego
if __name__ == "__main__":
    iniciar_juego()
