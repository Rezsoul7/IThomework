import aiohttp
import asyncio

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def fetch(self, endpoint: str, params: dict = None):
        """Виконує GET-запит до API."""
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f"{self.base_url}{endpoint}", params=params) as response:
                    response.raise_for_status()
                    data = await response.json()
                    return data
            except aiohttp.ClientError as e:
                print(f"Помилка клієнта: {e}")
            except Exception as e:
                print(f"Невідома помилка: {e}")

    async def post(self, endpoint: str, payload: dict):
        """Виконує POST-запит до API."""
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(f"{self.base_url}{endpoint}", json=payload) as response:
                    response.raise_for_status()
                    data = await response.json()
                    return data
            except aiohttp.ClientError as e:
                print(f"Помилка клієнта: {e}")
            except Exception as e:
                print(f"Невідома помилка: {e}")

# Приклад використання:
async def main():
    base_url = "https://jsonplaceholder.typicode.com"
    client = APIClient(base_url)

    # GET-запит
    posts = await client.fetch("/posts", params={"userId": 1})
    print("GET-запит:", posts)

    # POST-запит
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    created_post = await client.post("/posts", payload=new_post)
    print("POST-запит:", created_post)

# Запуск головної функції
if __name__ == "__main__":
    asyncio.run(main())
