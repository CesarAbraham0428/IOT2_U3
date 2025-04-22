# Importa los módulos necesarios
from machine import Pin, ADC         # Para usar pines y el convertidor analógico-digital (ADC)
from time import sleep               # Para hacer pausas en la ejecución
import urequests                     # Para hacer peticiones HTTP
import network                       # Para manejar la conexión WiFi

# Configura el pin 34 como entrada analógica (ADC) para leer el sensor
sensor = ADC(Pin(34))               
sensor.atten(ADC.ATTN_11DB)         # Establece la atenuación para leer hasta ~3.3V
sensor.width(ADC.WIDTH_12BIT)       # Establece la resolución del ADC a 12 bits (valores de 0 a 4095)

# Función para conectar a la red WiFi
def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)  # Crea la interfaz WiFi en modo estación
    sta_if.active(True)                    # Activa la interfaz WiFi
    sta_if.connect("WF_CANO", "23122024")  # Conecta a la red con SSID y contraseña
    while not sta_if.isconnected():        # Espera hasta que se conecte
        print(".", end="")                 
        sleep(0.5)                         
    print("\nWiFi OK IP:", sta_if.ifconfig()[0])  # Muestra la IP una vez conectado

connect_wifi()  # Llama a la función para conectarse al WiFi

# URL de la WebApp de Google que recibe los datos
WEBAPP_URL = "https://script.google.com/macros/s/AKfycby-GPAII0W711FKTS2q0U0-UzyAwZ72dOQpOgImuiOvEk7jXjIKZd_uLGxDYCNAMWFe/exec"

# Función para enviar el dato leído a Google Sheets vía WebApp
def send_to_sheets(valor):
    data = {
        "nivel_agua": valor  # Enviamos el valor del sensor con la clave "nivel_agua"
    }
    try:
        response = urequests.post(WEBAPP_URL, json=data)  # Envío del dato en formato JSON
        print("Respuesta:", response.text)                # Imprime la respuesta del servidor
        response.close()                                  # Cierra la conexión
    except Exception as e:
        print("Error enviando datos:", e)                 # Muestra error si falla la conexión

# Bucle principal que se ejecuta continuamente
while True:
    try:
        valor = sensor.read()  # Lee el valor del sensor ADC
        print("Nivel de agua (valor ADC):", valor)  # Muestra el valor leído
        print("-"*20)  # Línea separadora visual

        send_to_sheets(valor)  # Llama a la función para enviar el valor a Sheets

    except Exception as e:
        print("Error al leer sensor:", e)  # Captura y muestra cualquier error de lectura
    sleep(2)  # Espera 2 segundos antes de la siguiente lectura
