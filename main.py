from gtts import gTTS
import time

texto = """¡Claro! El CHIKI es un vehículo eléctrico muy interesante. Aquí te dejo algunos detalles clave:

Modelo: CHIKI-L (110KM) LITIO
Autonomía: 110 km, ideal para desplazamientos urbanos.
Batería: Litio NCM de 4,5 KWh con 2000 ciclos de vida.
Tiempo de carga: Aproximadamente 7 horas, admite cargas parciales.
Potencia: 2 KW.
Dimensiones: 2500x1200x1630 mm.
Velocidad máxima: 45 km/h.
Características de seguridad y confort: Tablero digital, faros LED, frenos a disco, calefacción, vidrios eléctricos, sistema de carga inteligente, Bluetooth y radio.

Además, su diseño lo hace perfecto para la movilidad urbana. ¡Es el primer vehículo eléctrico de San Luis!

El precio del CHIKI es de USD 9.900,00 y está disponible con entrega a 60 días.

Si estás interesado en adquirirlo o tenés más preguntas, ¡contame! 😊"""

start_time = time.time()

tts = gTTS(text=texto, lang='es', slow=False)
tts.save("voz_chatbot.mp3")

end_time = time.time()

tiempo_total = end_time - start_time
print(f"🕒 Tiempo de generación: {tiempo_total:.2f} segundos")
