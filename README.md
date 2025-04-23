# Proyecto de Sistema de Riego automatizado.

## Herramientas utilizadas. 
|**Sensores**|**Actuadores**|
|--|--|
|1. Sensor de Humedad.|1. Leds|
|2. Sensor de Flujo de Agua.|2. Relevador|
|3. Sensor de Temperatura DHT11.|3. Buzzer Activo|
|4. Sensor de Lluvia.|4. Bomba de Agua|

## Actividades de clase.

### Carcasa

[Link Carcasa](https://www.tinkercad.com/things/ejPxAvtqroV-frantic-jofo/edit?returnTo=https%3A%2F%2Fwww.tinkercad.com%2Fdashboard)

### Sensores Hojas de Cálculo.
|**Nombre**|**Sensor**|**Codigo**|
|--|--|--|
|Cesar Abraham|[Sensor DHT11](https://drive.google.com/file/d/1WExeR7v4lGsBS89xV08NBe9lGUByHLjx/view?usp=sharing)|[`Codigo.py`](/CodigoActividadesClase/TemperaturaHojaDeCalculo.py)|
|Isaac|[Sensor Nivel de Agua](https://drive.google.com/file/d/1llpEefqhAhDUOVI9CU5XQdxaRRH--hib/view?usp=drive_link)|[`Codigo.py`](/CodigoActividadesClase/SensorNivelAgua.py)|
|Luis Manuel|[Sensor KY022](https://drive.google.com/file/d/1a6sqMONPzCDYV34vSWFHVOsdguAs4AYM/view?usp=sharing)|[`Codigo.py`](/CodigoActividadesClase/SensorKY_022.py)|

## Codigos de sensores sistema de Riego.
|**Codigo**|
|--|
|[`Codigo Sensor de Humedad Suelo, DHT11 y Buzzer.py`](/CodigoSistemaRiego/CodigoFinalDHT11_Humedad_Buzzer.py)|
|[`Codigo Sensor de Nivel de Agua  y Humedad Suelo.py`](/CodigoSistemaRiego/SensorHumedadYNivelAgua.py)|
|[`Codigo Sensor de flujo de agua  y Control de relevador.py`](/CodigoMicroPythonSistemaRiego/Codigo_control_de_relevador_y_flujo_de_agua.py)|

## Diagramas de conexión del Sistema de Riego.

![Diagrama de la Alarma y el sensor de Humedad](/assets/AlarmaYHumedad.png)
[Link del diagrama de la Alarma y Sensor de Humedad](https://app.cirkitdesigner.com/project/a1cc3629-8e77-4b2b-bfe8-43f7c3ae7f4d)

![Diagrama de la Alarma y el sensor de Humedad](/assets/BombaYFlujoAgua.png)
[Link del diagrama de la Bomba de Agua y Flujo de Agua](https://app.cirkitdesigner.com/project/e0a767a8-0c34-4e84-8ac1-d186211fcbc0)

### Codigo del Flujo de Node Red.

[Flujo de Node-Red](/CodigoFlujoNodeRed/flujo)

## Coevaluación.

### César Abraham López Aguilar.

Mi Compañero Luis Manuel realizó un gran trabajo ya que a él le toco una parte fundamental del proyecto (bomba de agua y sensor de flujo de agua) y a mi parecer lo hizo de forma excelente, el codigo y los sensores funcionan de forma correcta, además el puso el flujo de Node-Red en la nube y aporto ideas para la realización del proyecto. Sin embargo lo que no me gusto es que en ocasiones llego tarde y muchas veces se enojo proque no funcionaba el codigo eso me disgusto y no me dio confianza hablarle por miedo que me fuera a regañar, además aveces me decia "lanzate por una caguama" sabiendo él que por la realización del proyecto me quede sin dinero y que aún no ha caido la beca, osea para que antoja si sabe que no tengo dinero eso si me molesto bastante. Lo que puede mejorar es su puntualidad y ser más comprensivo con migo.

Mi compañero Isaac Cano realizó un buen trabajo consiguiendo un lugar en donde poder montar y realizar el sistema de riego, además que  que se avento la base de datos en la nube y la parte que el le toco (sensor de humedad y sensor de lluvia) a mi parecer la realizo de forma correcta. Lo que no me gusto es que en ocasiones el ya había terminado y sus tareas correspondientes y no nos ayudo a los demás a terminar sus tareas, además que en una ocasión no nos dejo poner musica hasta las 3 ni idea de porque fue la razón, además un dia se tardo mucho en abrirme la puerta hasta tal punto que gracias a otro indivioduo quen vivia aqui tuve que pasar solo. Lo que puede mejorar es su disposición a ayudar a los demás y dejarnos escuchar musica.

### Isaac Cano Hernández

Mi compañero Cesar Abraham, tuvo un buen desempeño en el proyecto del sistema de riego. Siempre se mostró dispuesto a colaborar, participó activamente en varias partes del trabajo y nos ayudó a conseguir materiales cuando lo necesitábamos, lo cual fue muy útil. Sin embargo, en algunas ocasiones llegó tarde, se frustraba con facilidad cuando algo no funcionaba y hubo un momento en el que dejó parte de su tarea al resto del equipo. A pesar de esos detalles, su aporte fue valioso, aunque creo que podría mejorar en temas como la puntualidad, asumir completamente su parte del trabajo y manejar mejor la presión.

Mi compañero Luis Manuel, tuvo un buen desempeño general en el proyecto. Siempre estuvo dispuesto a ayudar y fue ingenioso para encontrar soluciones rápidas cuando surgían errores, lo cual ayudó a avanzar en varios momentos. Sin embargo, tuvo problemas con la puntualidad y, cuando las cosas no salían como esperaba, se desesperaba y a veces reaccionaba con molestia, lo que afectaba un poco el ambiente del equipo. Aunque su participación fue útil, debe mejorar en el manejo de la frustración y en su compromiso con los tiempos del equipo.

### Luis Manuel Ramirez Ramirez

Isaac demostró ser un miembro valioso del equipo y aportó de manera significativa al proyecto. Su compromiso general con las tareas asignadas fue evidente y su trabajo contribuyó positivamente al avance y la finalización del sistema de riego. Realizó sus responsabilidades de forma competente y mostró una buena disposición para colaborar. Como área de oportunidad, noté que en algunas ocasiones durante las sesiones de trabajo, Isaac tendía a distraerse con su teléfono celular por periodos prolongados. Si bien esto no impidió que completara sus tareas asignadas y su desempeño general fue bueno, considero que una mayor concentración y gestión de las distracciones en esos momentos podría haber optimizado aún más su eficiencia y la dinámica de trabajo del equipo. 

Cesar mostró un buen desempeño en las tareas que se le encomendaron y participó activamente en muchas de las fases del desarrollo del sistema. Por otro lado, identifiqué dos áreas donde podría mejorar su colaboración en futuros proyectos. Primero, hubo momentos específicos durante el tiempo de trabajo conjunto en los que observé una falta de actividad o participación directa en las tareas que se estaban realizando, lo cual a veces requería que otros miembros asumieran una carga adicional temporalmente. Segundo, en algunas ocasiones, Cesar solicitó ayuda para completar tareas que le habían sido asignadas específicamente, incluso cuando los demás miembros del equipo estábamos ocupados gestionando nuestras propias responsabilidades pendientes. Si bien la colaboración y el apoyo mutuo son esenciales, creo que sería beneficioso fomentar una mayor autonomía en la resolución de problemas iniciales y una mejor evaluación de la carga de trabajo del resto del equipo antes de solicitar asistencia. Esto ayudaría a mantener un flujo de trabajo más equilibrado para todos. A pesar de estos puntos, su contribución general al proyecto fue valiosa.
