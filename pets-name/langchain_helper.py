import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    # 1. Configuración del modelo
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        huggingfacehub_api_token=os.getenv("TOKEN_LC"),
        temperature=0.7,
        max_new_tokens=100,
        task="text-generation"
    )

    chat_model = ChatHuggingFace(llm=llm)

    # 2. Definición del Prompt
    prompt = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet. I only want the names after a number"
    )

    # 3. Creación de la cadena con el operador PIPE (|)
    chain = prompt | chat_model | StrOutputParser()

    # 4. Ejecución con .invoke y RETORNO de la respuesta
    response = chain.invoke({
        'animal_type': animal_type, 
        'pet_color': pet_color
    })
    
    return response

if __name__ == "__main__":
    print(generate_pet_name("Dog", "Black"))