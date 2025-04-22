import time
import urequests
import network
from machine import Pin
import dht

# ========== CONFIGURACIÓN ==========

# Pines y sensor
sensor = dht.DHT11(Pin(4))  # Usa el pin GPIO 4

# Red WiFi
WIFI_SSID = "INFINITUM5FF7"
WIFI_PASSWORD = "fyf5y2u7ph"

# URL del WebApp de Google Sheets
WEBAPP_URL = "https://script.google.com/macros/s/AKfycbwd3hZaEfrt7mIwgCg5BxT2rNYcvyaB8dpad8PFQ0WphNRtYO29ZGi6hZhr0bTJck_vCA/exec"

# ========== FUNCIONES ==========

# Conexión WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    timeout = 10
    print("Conectando a WiFi", end="")
    while not wlan.isconnected() and timeout > 0:
        print(".", end="")
        time.sleep(1)
        timeout -= 1

    if wlan.isconnected():
        print("\nConectado a WiFi. IP:", wlan.ifconfig()[0])
        return True
    else:
        print("\nError: No se pudo conectar a WiFi.")
        return False

# Enviar solo la temperatura a Google Sheets
def send_to_sheets(temp):
    try:
        print(f"Enviando temperatura: {temp}°C a Google Sheets...")
        response = urequests.post(WEBAPP_URL, json={"temp": temp})
        response.close()
        print("Temperatura enviada correctamente.")
    except Exception as e:
        print("Error enviando temperatura:", e)

# ========== PROGRAMA PRINCIPAL ==========

if connect_wifi():
    while True:
        try:
            sensor.measure()
            temp = sensor.temperature()

            print("Temperatura: {}°C".format(temp))

            if temp > 0:
                send_to_sheets(temp)
            else:
                print("Temperatura inválida, no se enviará.")

        except OSError as e:
            print("Error al leer el sensor:", e)
        except Exception as e:
            print("Error inesperado:", e)

        time.sleep(5)  # Espera 5 segundos entre lecturas
