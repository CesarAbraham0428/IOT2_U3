from machine import ADC, Pin
from time import sleep
import network
from umqtt.simple import MQTTClient

# Configura tu WiFi
ssid = 'TP-Link_084A'
password = '85435230'

# Conexión WiFi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

# Esperar conexión
while not sta_if.isconnected():
    pass
print('✅ Conectado a WiFi:', sta_if.ifconfig())

# Configura MQTT con broker.emqx.io
broker = 'broker.emqx.io'
client_id = 'sensor_esp32'
topic_nivel = b'sensor/nivel_agua'     # Topic para el sensor de nivel
topic_humedad = b'sensor/humedad'      # Topic para el sensor de humedad

# Crear cliente MQTT
client = MQTTClient(client_id, broker)
client.connect()
print("Conectado al broker MQTT:", broker)

# Configurar sensor ADC (nivel de agua)
sensor_nivel = ADC(Pin(34))  # Pin para el sensor de nivel
sensor_nivel.atten(ADC.ATTN_11DB)
sensor_nivel.width(ADC.WIDTH_12BIT)

# Configurar sensor ADC (humedad del suelo)
sensor_humedad = ADC(Pin(32))  # Pin para el sensor de humedad (elige otro disponible)
sensor_humedad.atten(ADC.ATTN_11DB)
sensor_humedad.width(ADC.WIDTH_12BIT)

# Bucle principal: leer y enviar ambos sensores cada 5 segundos
while True:
    valor_nivel = sensor_nivel.read()
    valor_humedad = sensor_humedad.read()

    print("Nivel de agua:", valor_nivel)
    print("Humedad del suelo:", valor_humedad)

    client.publish(topic_nivel, str(valor_nivel))      # Publicar nivel de agua
    client.publish(topic_humedad, str(valor_humedad))  # Publicar humedad del suelo

    sleep(5)

