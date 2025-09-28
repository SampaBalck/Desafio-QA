# api_tests/pages/client.py
import requests

BASE_URL = "https://demoqa.com"

class BookStoreClient:
    def __init__(self):
        self.session = requests.Session()
        self.user_id = None
        self.token = None
        self.username = None
        self.password = None

    def create_user(self, username, password):
        """Cria um usuário e guarda username e password."""
        self.username = username
        self.password = password
        url = f"{BASE_URL}/Account/v1/User"
        payload = {"userName": username, "password": password}
        resp = self.session.post(url, json=payload)
        # Salva o user_id se a chamada for bem sucedida (código 201)
        if resp.status_code == 201:
            self.user_id = resp.json().get("userID")
        return resp

    def generate_token(self, username=None, password=None):
        """Gera token de acesso."""
        username = username or self.username
        password = password or self.password
        url = f"{BASE_URL}/Account/v1/GenerateToken"
        payload = {"userName": username, "password": password}
        resp = self.session.post(url, json=payload)
        # Atualiza o token na sessão se a chamada for bem sucedida
        if resp.status_code == 200:
            data = resp.json()
            if "token" in data and data.get("status") == "Success":
                self.token = data["token"]
                self.session.headers.update({"Authorization": f"Bearer {self.token}"})
        return resp

    def is_authorized(self, username=None, password=None):
        """Confirma se o usuário está autorizado."""
        username = username or self.username
        password = password or self.password
        url = f"{BASE_URL}/Account/v1/Authorized"
        payload = {"userName": username, "password": password}
        return self.session.post(url, json=payload)

    def list_books(self):
        """Lista todos os livros disponíveis."""
        url = f"{BASE_URL}/BookStore/v1/Books"
        return self.session.get(url)

    def add_books(self, isbn_list):
        """Aluga livros para o usuário."""
        url = f"{BASE_URL}/BookStore/v1/Books"
        payload = {
            "userId": self.user_id,
            "collectionOfIsbns": [{"isbn": isbn} for isbn in isbn_list]
        }
        return self.session.post(url, json=payload)

    def get_user_details(self):
        """Retorna detalhes do usuário com livros alugados."""
        if not self.user_id:
            raise ValueError("UserID não definido. Crie um usuário primeiro.")
        url = f"{BASE_URL}/Account/v1/User/{self.user_id}"
        return self.session.get(url)