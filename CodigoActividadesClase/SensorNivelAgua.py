from machine import Pin, ADC
from time import sleep
import urequests
import network

sensor = ADC(Pin(34))  
sensor.atten(ADC.ATTN_11DB)  
sensor.width(ADC.WIDTH_12BIT)  

# Configurar WiFi
def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("WF_CANO", "23122024")
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.5)
    print("\nWiFi OK IP:", sta_if.ifconfig()[0])

connect_wifi()

# URL del WebApp de Google
WEBAPP_URL = "https://script.google.com/macros/s/AKfycby-GPAII0W711FKTS2q0U0-UzyAwZ72dOQpOgImuiOvEk7jXjIKZd_uLGxDYCNAMWFe/exec"

def send_to_sheets(valor):
    data = {
        "nivel_agua": valor  # Clave corregida
    }
    try:
        response = urequests.post(WEBAPP_URL, json=data)
        print("Respuesta:", response.text)
        response.close()
    except Exception as e:
        print("Error enviando datos:", e)

while True:
    try:
        # Leer sensor de nivel de agua
        valor = sensor.read()
        print("Nivel de agua (valor ADC):", valor)
        print("-"*20)

        send_to_sheets(valor)

    except Exception as e:
        print("Error al leer sensor:", e)
    sleep(2)

