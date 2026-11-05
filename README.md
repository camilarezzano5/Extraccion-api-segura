# Extracción y almacenamiento seguro de datos vía API

## Descripción
Este proyecto realiza una petición GET a la API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts), recupera publicaciones, conserva los campos principales y guarda el resultado en un archivo JSON.

Se utiliza un archivo `.env` para configurar la URL de la API. No se necesitan credenciales ni API Key para este ejemplo.

## Estructura del repositorio

```text
extraccion_api_segura/
├── data/
│   └── data_extracted.json
├── .env.example
├── .gitignore
├── extract_data.py
├── README.md
└── requirements.txt
```

## Requisitos
- Python 3.9 o superior.
- Conexión a Internet.

## Instalación y configuración

1. Clonar el repositorio o descargar sus archivos.
2. Crear y activar un entorno virtual (recomendado):

   ```bash
   python -m venv .venv
   ```

   En Windows:

   ```bash
   .venv\Scripts\activate
   ```

   En macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crear el archivo `.env` copiando `.env.example` y conservar esta configuración:

   ```env
   API_URL=https://jsonplaceholder.typicode.com/posts
   ```

   El archivo `.env` está excluido de Git mediante `.gitignore`. No subir credenciales ni tokens al repositorio.

## Ejecución

Desde la carpeta principal del proyecto:

```bash
python extract_data.py
```

Si la petición es exitosa, los datos se guardan en `data/data_extracted.json`.

## Manejo de errores
El script contempla errores HTTP mediante `raise_for_status()` y bloques `except` para errores de conexión, tiempo de espera y otras fallas de la petición. También valida que la respuesta tenga el formato esperado y controla errores al guardar el archivo.

## Fuente de datos
- API: [JSONPlaceholder - Posts](https://jsonplaceholder.typicode.com/posts)
- Método HTTP: `GET`
- Formato de respuesta: JSON
- Archivo de salida: `data/data_extracted.json`

## Seguridad
La configuración se carga desde variables de entorno con `python-dotenv`. El archivo `.env` no debe publicarse. Se incluye `.env.example` como plantilla sin información sensible.
