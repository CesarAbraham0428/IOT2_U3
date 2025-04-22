from machine import Pin
from time import sleep
import urequests
import network

# Configuración del sensor KY-022
sensor_ir = Pin(34, Pin.IN)  # Ajusta el pin según tu conexión

# Función para leer el estado del sensor IR
def leer_sensor_ir():
    estado = sensor_ir.value()  # 0 si detecta señal IR, 1 si no detecta
    return estado

# Conectar a WiFi
def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('TP-Link_084A', '85435230')  # Agrega contraseña si es necesario

    timeout = 10  # Tiempo máximo de espera en segundos
    while not sta_if.isconnected() and timeout > 0:
        print(".", end="")
        sleep(1)
        timeout -= 1

    if sta_if.isconnected():
        print("\nWiFi Conectado, IP:", sta_if.ifconfig()[0])
        return True
    else:
        print("\nError: No se pudo conectar a WiFi.")
        return False

# URL del WebApp de Google
WEBAPP_URL = "https://script.google.com/macros/s/AKfycbwpiobbHKq6gAQy677qWwW4RkOUZKrM1Qflt41sXCBL-fHFGZmm35XRWP6gJDXk1SG16w/exec"

# Enviar datos a Google Sheets
def send_to_sheets(estado):
    try:
        print(f"Enviando estado del sensor IR: {estado} a Google Sheets...")
        response = urequests.post(WEBAPP_URL, json={"sensor_ir": estado})  # Enviar JSON
        print("Respuesta del servidor:", response.text)  # Ver la respuesta del WebApp
        response.close()
    except Exception as e:
        print("Error enviando datos:", e)

# Conectar a WiFi antes de iniciar el loop
estado_anterior = None

if connect_wifi():
    while True:
        try:
            estado_actual = leer_sensor_ir()
            print(f"Estado del sensor IR: {estado_actual}")

            if estado_actual != estado_anterior:
                send_to_sheets(estado_actual)
                estado_anterior = estado_actual

        except Exception as e:
            print("Error al leer sensor o enviar datos:", e)

        sleep(1)