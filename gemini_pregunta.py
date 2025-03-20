import google.generativeai as genai
import api_key
import sys

genai.configure(api_key=api_key.API_KEY)  # Usa la API_KEY

model = genai.GenerativeModel('gemini-1.5-flash-late')

# Obtiene la pregunta desde la línea de comandos
if len(sys.argv) > 1:
    pregunta = sys.argv[1]
else:
    pregunta = "No se ha ingresado ninguna pregunta en la línea de comandos. Por favor, proporciona una pregunta como argumento."



# Combinamos contexto, instrucciones y pregunta
prompt = f"{pregunta}"

# Configuramos las opciones de generación
generation_config = genai.GenerationConfig(
    temperature=0.7,
    top_p=1,
    top_k=32,
    max_output_tokens=256,
)

# Generamos la respuesta
respuesta = model.generate_content(prompt, generation_config=generation_config)

print(respuesta.text)
