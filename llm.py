import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

API_URL = (
    "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
)
API_KEY = os.getenv("HF_API_KEY")

HEADERS = {"Authorization": f"Bearer {API_KEY}"}


def generate_sql(user_request: str) -> str:
    """
    Генерирует SQL-запрос на основе текстового запроса пользователя.

    :param user_request: Описание запроса на естественном языке.
    :return: Сгенерированный SQL-запрос или сообщение об ошибке.
    """
    if not API_KEY:
        return "Ошибка: API-ключ не найден. Проверьте файл .env."

    prompt = f"Напиши SQL-запрос для следующей задачи: {user_request}"
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()[0].get("generated_text", "Ошибка генерации SQL")
    else:
        return f"Ошибка API: {response.status_code}, {response.text}"
