from machine import Pin, PWM, ADC
import dht
import time

# Configuración del sensor de temperatura DHT11
SENSOR_PIN = 15
sensor = dht.DHT11(Pin(SENSOR_PIN))

# Configuración del buzzer usando PWM
BUZZER_PIN = 2


buzzer = PWM(Pin(BUZZER_PIN))

# Configuración del sensor de humedad de suelo
SOIL_SENSOR_PIN = 32
soil_sensor = ADC(Pin(SOIL_SENSOR_PIN))
soil_sensor.atten(ADC.ATTN_11DB)
soil_sensor.width(ADC.WIDTH_12BIT)  # Resolución de 12 bits (0-4095)

# Temperatura umbral (°C) por debajo de la cual se activa la alarma
TEMP_UMBRAL = 12

# Frecuencias para la alarma
FREQ_ALTA = 2500   # Frecuencia alta (2.5kHz)
FREQ_MEDIA = 1800  # Frecuencia media
FREQ_BAJA = 800    # Frecuencia baja

# Volúmenes
VOL_MAX = 512
VOL_MEDIO = 400

# Variable para controlar si la alarma está activa
alarma_activa = False

# Inicializar el buzzer apagado
buzzer.duty(0)

def set_buzzer(freq, volumen):
    """Configura el buzzer con frecuencia y volumen específicos"""
    if freq == 0:  # Apagar el buzzer
        buzzer.duty(0)
    else:
        buzzer.freq(freq)
        buzzer.duty(volumen)

def reproducir_patron_alarma():
    """Reproduce un patrón de alarma una vez"""
    # Patrón 1: Tres tonos rápidos ascendentes
    for _ in range(3):
        set_buzzer(FREQ_BAJA, VOL_MAX)
        time.sleep(0.07)
        set_buzzer(FREQ_MEDIA, VOL_MAX)
        time.sleep(0.07)
        set_buzzer(FREQ_ALTA, VOL_MAX)
        time.sleep(0.07)
        set_buzzer(0, 0)  # Apagar brevemente
        time.sleep(0.05)
    
    # Patrón 2: Tono de sirena alternante
    for _ in range(4):
        set_buzzer(FREQ_ALTA, VOL_MAX)
        time.sleep(0.15)
        set_buzzer(FREQ_BAJA, VOL_MAX)
        time.sleep(0.15)

def leer_humedad_suelo():
    """Lee la humedad del suelo y devuelve el porcentaje"""
    valor = soil_sensor.read()  # Lee valor entre 0 y 4095
    # Convertir a porcentaje (0% = completamente seco, 100% = completamente húmedo)
    # Nota: Los valores ADC son inversamente proporcionales a la humedad
    porcentaje = 100 - int((valor / 4095) * 100)
    return porcentaje

# Bucle principal
print("Sistema de monitoreo de temperatura y humedad de suelo iniciado")
print("Umbral de alerta de temperatura: {}°C".format(TEMP_UMBRAL))

# Inicialización del sensor
time.sleep(2)  # Tiempo de estabilización del sensor antes de comenzar

while True:
    try:
        # 1. Medir temperatura y humedad ambiental
        sensor.measure()
        time.sleep(0.5)  # Pequeña pausa para estabilizar la lectura
        
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        # 2. Medir humedad del suelo
        humedad_suelo = leer_humedad_suelo()
        
        # Mostrar todas las lecturas
        print("Temperatura: {}°C, Humedad ambiente: {}%, Humedad suelo: {}%".format(
            temp, hum, humedad_suelo))
        
        # Verificar si la temperatura está por debajo del umbral
        if temp < TEMP_UMBRAL:
            if not alarma_activa:
                print("¡ALERTA! Temperatura por debajo de {}°C".format(TEMP_UMBRAL))
                alarma_activa = True
            
            # Mientras la temperatura esté por debajo del umbral, seguir reproduciendo el patrón de alarma
            reproducir_patron_alarma()
            # Nota: La función reproducir_patron_alarma no apaga el buzzer al final
            
        else:
            if alarma_activa:
                print("Temperatura normal restaurada: {}°C".format(temp))
                alarma_activa = False
            
            # Asegurar que el buzzer esté apagado cuando la temperatura es normal
            set_buzzer(0, 0)
            
    except OSError as e:
        print("Error al leer el sensor:", e)
        # Esperar un poco más en caso de error antes de reintentar
        time.sleep(2)
        # No activar el buzzer en caso de error para evitar falsos positivos
        set_buzzer(0, 0)
    
    # Si la temperatura es normal, añadimos una pausa
    if not alarma_activa:
        time.sleep(2)