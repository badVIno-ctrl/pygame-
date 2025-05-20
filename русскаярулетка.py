import requests
import json

API_KEY = "DlWJGSjUANbZ5tRjXI3nHhA8AC6S44OX"
API_URL = "https://api.mistral.ai/v1/chat/completions"
MODEL_NAME = "mistral-large-latest"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}


def send_query_to_mistral(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()  
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"[Ошибка] Не удалось получить ответ от Mistral AI:\n{e}"


def main():
    print("=== Chat  ===")
    print("Введите 'выход' или 'exit', чтобы завершить работу.")

    while True:
        user_input = input("\nВы: ")
        if user_input.lower() in ['выход', 'exit', 'quit']:
            print("Завершение работы...")
            break

        print("\nMistral думает... 🤔")
        answer = send_query_to_mistral(user_input)
        print(f"\nMistral:")
        print(answer)


if __name__ == "__main__":
    main()
