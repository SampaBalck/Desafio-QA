# pytest api_tests/test_api_flow.py -s
import pytest
import random
import uuid

# Gera um usuário e senha únicos para toda a sessão de testes
USERNAME = f"test_user_{uuid.uuid4().hex[:8]}"
PASSWORD = "Test@12345!"

def test_01_criar_usuario(client):
    """Verifica o Passo 1: Criação de um usuário único."""
    print(f"\n--- Etapa 1: Criar o usuário: {USERNAME} ---")
    response = client.create_user(USERNAME, PASSWORD)
    
    assert response.status_code == 201, f"Esperado 201, mas recebido {response.status_code}. Mensagem: {response.text}"
    
    data = response.json()
    assert "userID" in data
    print(f"✅ Usuário criado com sucesso (Status {response.status_code}).")

def test_02_gerar_token(client):
    """Verifica o Passo 2: Geração de token."""
    print("--- Etapa 2: Gerar um token de acesso ---")
    response = client.generate_token()

    assert response.status_code == 200
    
    data = response.json()
    assert data.get("status") == "Success"
    assert "token" in data
    print(f"✅ Token gerado com sucesso (Status {response.status_code}).")

def test_03_confirmar_autorizacao(client):
    """Verifica o Passo 3: Confirmação de autorização."""
    print("--- Etapa 3: Confirmar se o usuário está autorizado ---")
    response = client.is_authorized()

    assert response.status_code == 200
    
    assert response.json() is True
    print(f"✅ Usuário está autorizado (Status {response.status_code}).")

def test_04_listar_livros(client):
    """Verifica o Passo 4: Listagem de livros."""
    print("--- Etapa 4: Listar os livros disponíveis ---")
    response = client.list_books()

    assert response.status_code == 200
    
    books = response.json()["books"]
    assert isinstance(books, list) and len(books) > 0
    client.books_list = books  # Salva para o próximo passo
    print(f"✅ {len(books)} livros listados (Status {response.status_code}).")

def test_05_alugar_livros(client):
    """Verifica o Passo 5: Aluguel de dois livros."""
    print("--- Etapa 5: Alugar dois livros de livre escolha ---")
    
    books_to_rent = random.sample([book["isbn"] for book in client.books_list], 2)
    response = client.add_books(books_to_rent)

    assert response.status_code == 201
    
    data = response.json()
    assert "books" in data
    client.rented_books = books_to_rent
    print(f"✅ Livros alugados com sucesso (Status {response.status_code}).")

def test_06_listar_detalhes_usuario(client):
    """Verifica o Passo 6: Detalhes do usuário com livros alugados."""
    print("--- Etapa 6: Listar detalhes do usuário com os livros escolhidos ---")
    response = client.get_user_details()

    assert response.status_code == 200

    details = response.json()
    reserved_isbns = [book["isbn"] for book in details["books"]]
    for isbn in client.rented_books:
        assert isbn in reserved_isbns
    print("✅ Detalhes do usuário validados com os livros corretos.")