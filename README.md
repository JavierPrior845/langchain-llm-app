# LangChain AI Assistants 🐾📺

Este repositorio contiene dos proyectos prácticos de Inteligencia Artificial desarrollados con **LangChain** y **Streamlit**. Ambos han sido actualizados a las versiones más recientes de la librería (v0.3+) y adaptados para funcionar con el ecosistema de **Hugging Face**.

## 🚀 Proyectos Incluidos

### 1. Pet Name Generator (Generador de Nombres)
Un asistente sencillo que utiliza un modelo de lenguaje para sugerir nombres creativos para mascotas basándose en:
* El tipo de animal (perro, gato, vaca, etc.).
* El color de la mascota.
* Utiliza una estructura de **PromptTemplate** y **LCEL** para generar respuestas rápidas.

### 2. YouTube Assistant (Asistente de Vídeos)
Una herramienta avanzada de RAG (Retrieval Augmented Generation) que:
* Extrae el transcript de vídeos de YouTube.
* Fragmenta el texto y lo vectoriza con **HuggingFaceEmbeddings**.
* Almacena el contenido en una base de datos **FAISS**.
* Permite chatear con el vídeo para obtener información específica sin tener que verlo completo.

---

## 🛠️ Stack Tecnológico

* **Framework:** LangChain (v0.3+)
* **Modelos (LLM):** `mistralai/Mistral-7B-Instruct-v0.2` vía Hugging Face.
* **Embeddings:** `all-MiniLM-L6-v2` (Locales y eficientes).
* **Vector Store:** FAISS.
* **Interfaz:** Streamlit.

---

## 📋 Novedades de esta Versión

He refactorizado el código original (basado en OpenAI) para hacerlo 100% compatible con herramientas Open Source y las últimas prácticas de desarrollo:
* **Sin costes de API:** Cambio de OpenAI a Hugging Face.
* **Código Moderno:** Uso de `ChatHuggingFace` y el motor de cadenas `|` (LCEL).
* **Modularidad:** Separación limpia entre la lógica de LangChain (`langchain_helper.py`) y la interfaz de usuario (`main.py`).

---

## 🔧 Configuración rápida

1. **Clona el proyecto e instala dependencias:**
   ```bash
   git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)
   cd nombre-del-repo
   pip install -r requirements.txt
2. **Variables de entorno**
Crea un archivo .env y añade tu token:
    ```bash
    TOKEN_LC=hf_tu_token_de_huggingface
3. **Ejecucion**
    - Para el generador de nombres: streamlit run pet-name-generator/main.py
    - Para el asistente de YouTube: streamlit run youtube-assistant/main.py