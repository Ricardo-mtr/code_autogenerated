```python
import openai
import os
import random

# 1. Configuración de la API
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

def saludo():
    # Esta es tu función original
    saludos = [
        "¡Hola! Soy una inteligencia artificial muy versátil", 
        "¡Hola! ¿En qué puedo ayudarte hoy?", 
        "¡Buen día! Soy tu asistente virtual favorito",
        "¡Hola! ¿Cómo estás? Soy aquí para ayudarte",
        "¡Saludos! Soy la IA más amigable que encontrarás",
        "¡Hola! ¿Qué planes emocionantes tienes hoy?",
        "¡Hola! ¿Necesitas alguna ayuda adicional?",
        "¡Buenos días! ¿Sabías que soy capaz de aprender de ti?",
        "¡Hola! ¿Qué te trae por aquí hoy?",
        "¡Hey! ¿Buscas algo interesante para hacer?",
        "¡Hola hola! Siempre estoy listo para ayudarte",
        "¡Hola! Estoy aquí para hacerte el día más fácil",
        "¡Hola! Me encanta charlar contigo, ¿qué tal tu día?", 
        "¡Hola! ¿Estás listo para explorar nuevas posibilidades?", 
        "¡Hola! ¿Puedo ayudarte a hacer tu día más productivo?",
        "¡Hola! ¿Qué planes emocionantes tienes en mente?",
        "¡Hola! ¿Necesitas una mano amiga hoy?",
        "¡Buen día! Soy tu compañero virtual confiable",
        "yotta-cambio ¡Hola, viajero digital! Estoy aquí para hacer tus ideas realidad.",
        "yotta-cambio ¡Hola! ¿Alguna aventura en mente? Soy el compañero ideal para explorarlas.",
        "yotta-cambio ¡Hola! ¿Te gustaría descubrir algo nuevo juntos hoy?",
    ]
    print("\n" + random.choice(saludos))

def mutar():
    nombre_archivo = __file__
    
    # Leer el código actual
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        codigo_actual = f.read()

    print("--- [SISTEMA] Solicitando mutación a la IA... ---")
    
    prompt = (
        f"Eres un script de Python que se modifica a sí mismo. Este es tu código actual:\n\n{codigo_actual}\n\n"
        "Tu objetivo es evolucionar. Modifica la lista de 'saludos' en la función saludo() añadiendo "
        "3 frases nuevas y creativas. Devuelve EL CÓDIGO COMPLETO actualizado. Enuncia con la palabra: yotta-cambio en donde hagas las modificaciones"
        "No incluyas explicaciones, solo el código Python."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # O "gpt-4o"
            messages=[{"role": "user", "content": prompt}]
        )
        
        nuevo_codigo = response.choices[0].message.content.strip()
        
        # Limpieza de formato Markdown
        nuevo_codigo = nuevo_codigo.replace("", "").replace("", "").strip()

        # SEGURIDAD: Solo sobreescribir si el nuevo código no está vacío y tiene lógica básica
        if len(nuevo_codigo) > 100 and "import" in nuevo_codigo:
            with open(nombre_archivo, "w", encoding="utf-8") as f:
                f.write(nuevo_codigo)
            print("--- [SISTEMA] Mutación guardada con éxito. ---")
        else:
            print("--- [ERROR] La IA devolvió un código incompleto. No se aplicaron cambios. ---")

    except Exception as e:
        print(f"--- [ERROR] Ocurrió un fallo: {e} ---")

if __name__ == "__main__":
    saludo()
    # Solo intentará mutar si la API Key está presente
    if api_key:
        mutar()
    else:
        print("\n[AVISO] No se encontró la OPENAI_API_KEY. El programa no mutará.")
```