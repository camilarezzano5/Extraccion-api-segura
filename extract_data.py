"""
Extrae publicaciones desde JSONPlaceholder y las guarda en data/data_extracted.json.
La URL de la API se configura mediante la variable de entorno API_URL.
"""

import json
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

# Carga las variables definidas en el archivo .env
load_dotenv()

API_URL = os.getenv("API_URL")
OUTPUT_FILE = Path(__file__).parent / "data" / "data_extracted.json"


def extract_data():
    """Consulta la API, valida la respuesta y devuelve datos simplificados."""
    if not API_URL:
        raise ValueError(
            "No se encontró API_URL. Creá un archivo .env a partir de .env.example."
        )

    try:
        response = requests.get(API_URL, timeout=15)
        response.raise_for_status()  # Detecta respuestas HTTP 4xx y 5xx
        payload = response.json()

        if not isinstance(payload, list):
            raise ValueError("La respuesta de la API no tiene el formato de lista esperado.")

        # Conserva solo los campos necesarios para el análisis
        cleaned_data = [
            {
                "id": item.get("id"),
                "user_id": item.get("userId"),
                "title": item.get("title"),
                "body": item.get("body"),
            }
            for item in payload
            if isinstance(item, dict)
        ]

        return cleaned_data

    except requests.exceptions.HTTPError as error:
        print(f"Error HTTP al consultar la API: {error}")
    except requests.exceptions.ConnectionError:
        print("Error de conexión: no se pudo contactar con la API.")
    except requests.exceptions.Timeout:
        print("La solicitud excedió el tiempo de espera.")
    except requests.exceptions.RequestException as error:
        print(f"Error durante la petición: {error}")
    except ValueError as error:
        print(f"Error en la configuración o en los datos recibidos: {error}")

    return None


def save_data(data):
    """Guarda los datos en formato JSON dentro del repositorio."""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Extracción finalizada: {len(data)} registros guardados en {OUTPUT_FILE}")


if __name__ == "__main__":
    extracted_data = extract_data()

    if extracted_data is not None:
        try:
            save_data(extracted_data)
        except OSError as error:
            print(f"No se pudo guardar el archivo: {error}")
            sys.exit(1)
    else:
        sys.exit(1)
