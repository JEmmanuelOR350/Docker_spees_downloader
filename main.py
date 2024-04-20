import threading
import time
import requests
import sys

class Descarga(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        inicio = time.time()
        respuesta = requests.get(self.url)
        fin = time.time()
        tiempo_descarga = fin - inicio
        print(f"Descarga de {len(respuesta.content)} bytes completada en {tiempo_descarga:.2f} segundos")

def descarga(url, condicion):
    while not condicion.is_set():
        try:
            print("\n===============================================================")
            print("Revisando enlaces...")
            time.sleep(30) # Espera exactamente 30 segundos desde esta seccion para volver a descargar los datos
            print("Realizando descarga...")
            descarga = Descarga(url)
            descarga.start()
            descarga.join()
            print("Descarga completada. Resultados impresos.")
            print("===============================================================")
        except Exception as e:
            condicion.set()
            print("\nError durante proceso. Cerrando programa. Mensaje de error:\n")
            print(e)
            print("===============================================================")

if __name__ == "__main__":
    # URL de prueba para descarga
    enlace = "https://github.com/JEmmanuelOR350/ID_random_generator/blob/c83176d026fc539e1ebf0027ce441fb33f36e19f/nombres.txt"

    condicion = threading.Event() #Evento para controlar la condición del bucle
    descarga_thread = threading.Thread(target=descarga, args=(enlace, condicion))
    descarga_thread.start()

    #Bucle para capturar una interupccion por teclado, y arrojar el cierre del thread
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        condicion.set()
        print("\nDetención asistida por el usuario. Cerrando el programa.")
        descarga_thread.join()
