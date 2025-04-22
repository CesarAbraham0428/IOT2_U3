import network
from umqtt.simple import MQTTClient
from machine import Pin
from time import sleep
import time

# Configuración del broker MQTT
MQTT_BROKER = "broker.emqx.io"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = "placa1"
MQTT_PORT = 1883

# Topics
MQTT_RELAY_TOPIC = "sistema_de_riego_inteligente/placa_1_rele"
MQTT_FLOW_TOPIC = "sistema_de_riego_inteligente/placa_1_agua"
MQTT_MANUAL_RELAY_TOPIC = "sistema_de_riego_inteligente/placa_1_rele/set"
MQTT_LED_ROJO_TOPIC = "sistema_de_riego_inteligente/placa_1_led_rojo"
MQTT_LED_AZUL_TOPIC = "sistema_de_riego_inteligente/placa_1_led_azul"
MQTT_AUTO_RELAY_TOPIC = "sistema_de_riego_inteligente/placa_1_rele/auto"

# Pines
rele = Pin(13, Pin.OUT)
led_rojo = Pin(14, Pin.OUT)
led_azul = Pin(27, Pin.OUT)
flow_sensor = Pin(4, Pin.IN)

# Estado
flow_counter = 0
estado_rele_manual = False
estado_rele_auto = False

# Contador de pulsos
def contar_pulsos(pin):
    global flow_counter
    flow_counter += 1

flow_sensor.irq(trigger=Pin.IRQ_FALLING, handler=contar_pulsos)

# WiFi
def conectar_wifi():
    print("Conectando WiFi...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('TP-Link_084A', '85435230')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print(" ¡Conectado!")

# Callbacks MQTT
def mqtt_callback(topic, msg):
    global estado_rele_manual, estado_rele_auto
    topic_str = topic.decode()
    msg_str = msg.decode().lower()
    print(f"[DEBUG] Mensaje recibido - Topic: {topic_str}, Mensaje: {msg_str}")
    

    if topic_str == MQTT_MANUAL_RELAY_TOPIC:
        if msg_str == "true":
            estado_rele_manual = True
        elif msg_str == "false":
            estado_rele_manual = False
        print("Relevador manual:", estado_rele_manual)
    elif topic_str == MQTT_AUTO_RELAY_TOPIC:
        if msg_str == "true":
            estado_rele_auto = True
        elif msg_str == "false":
            estado_rele_auto = False
        print("Relevador auto:", msg.decode())

# MQTT
def subscribir():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT,
                        user=MQTT_USER, password=MQTT_PASSWORD, keepalive=60)
    client.set_callback(mqtt_callback)
    client.connect()
    client.subscribe(MQTT_MANUAL_RELAY_TOPIC)
    client.subscribe(MQTT_AUTO_RELAY_TOPIC)
    print(f"Conectado a {MQTT_BROKER}, {MQTT_MANUAL_RELAY_TOPIC}, {MQTT_AUTO_RELAY_TOPIC}")
    return client

# Conexión
conectar_wifi()
client = subscribir()

# Función para actualizar LEDs y mandar estados
def actualizar_leds_y_mandar_estado(encendido):
    if encendido:
        led_azul.on()
        led_rojo.off()
        client.publish(MQTT_LED_AZUL_TOPIC, "Encendido")
        client.publish(MQTT_LED_ROJO_TOPIC, "Apagado")
    else:
        led_azul.off()
        led_rojo.on()
        client.publish(MQTT_LED_AZUL_TOPIC, "Apagado")
        client.publish(MQTT_LED_ROJO_TOPIC, "Encendido")

# Loop principal
while True:
    # Escuchar mensajes MQTT
    client.check_msg()

    # Medición del flujo
    start_time = time.time()
    flow_counter = 0
    for _ in range(10):
        client.check_msg()
        sleep(0.1)  # 10 * 0.1 = 1 segundo

    elapsed_time = time.time() - start_time
    flow_rate = (flow_counter / elapsed_time) / 7.5
    client.publish(MQTT_FLOW_TOPIC, f"{flow_rate:.2f} L/min")
    print(f"Flujo: {flow_rate:.2f} L/min")

    # Control del relé y LEDs
    if estado_rele_manual:
        rele.off()
        client.publish(MQTT_RELAY_TOPIC, "Encendido")
        actualizar_leds_y_mandar_estado(True)
    else:
        if estado_rele_auto:
            rele.off()
            client.publish(MQTT_RELAY_TOPIC, "Encendido")
            actualizar_leds_y_mandar_estado(True)
        else:
            rele.on()
            client.publish(MQTT_RELAY_TOPIC, "Apagado")
            actualizar_leds_y_mandar_estado(False)
        

    # Permitir tiempo para recibir nuevos mensajes
    for _ in range(20):
        client.check_msg()
        sleep(0.1)  # 2 segundos
