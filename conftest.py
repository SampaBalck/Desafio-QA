import pytest
import os
import uuid
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from api_tests.pages.client import BookStoreClient

# --- Variável global para o driver ---
# É acessada pela BasePage e outras partes do framework
driver = None

# ------------------------------------------------------------------
# Fixtures para Testes de API (sem alteração)
# ------------------------------------------------------------------

@pytest.fixture(scope="session")
def client():
    """Cria uma única instância do cliente para toda a sessão."""
    return BookStoreClient()

@pytest.fixture(scope="session")
def created_user(client):
    """Cria um usuário único para a sessão de testes."""
    username = f"test_user_{uuid.uuid4().hex[:6]}"
    password = "Test@00001"
    response = client.create_user(username, password)
    return {"client": client, "response": response}

@pytest.fixture(scope="session")
def generated_token(client, created_user):
    """Gera um token para o usuário criado na sessão."""
    response = client.generate_token(client.username, client.password)
    return {"client": client, "response": response}

# ------------------------------------------------------------------
# Fixture Unificada para Testes de UI (Selenium)
# ------------------------------------------------------------------

@pytest.fixture(scope="class")
def setup_teardown(request):
    """
    Fixture unificada: abre o navegador antes da classe de teste,
    disponibiliza o driver e o fecha no final.
    """
    global driver
    
    # --- SETUP ---
    logging.info("Iniciando o setup do navegador...")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://demoqa.com/")
    driver.maximize_window()
     # --- LINHA ADICIONADA AQUI ---
    print("Ajustando o zoom para 75%...")
    driver.execute_script("document.body.style.zoom = '75%'")

    driver.implicitly_wait(5) # Boa prática para esperas
    
    # Disponibiliza o driver para a classe de teste
    if request.cls is not None:
        request.cls.driver = driver
    
    # --- EXECUÇÃO DOS TESTES ---
    yield driver # Retorna o driver para que os testes o utilizem
    
    # --- TEARDOWN ---
    logging.info("Finalizando o driver...")
    driver.quit()

# ------------------------------------------------------------------
# Hooks do Pytest (configurações extras)
# ------------------------------------------------------------------

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Cria o diretório de relatórios antes do início dos testes."""
    reports_dir = 'reports'
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    # Configura o arquivo de log
    logging.basicConfig(
        filename=os.path.join(reports_dir, 'test_run.log'),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

#def pytest_html_report_title(report):
#    """Define um título dinâmico para o relatório HTML."""
#    report.title = "Relatório de Automação - " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook para tirar screenshot APENAS SE o teste falhar.
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == 'call' and report.failed:
        if driver:
            reports_dir = 'reports'
            current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # Usa o nome do teste para nomear o screenshot
            screenshot_name = f"FAILURE_{item.name}_{current_datetime}.png"
            screenshot_path = os.path.join(reports_dir, screenshot_name)
            driver.save_screenshot(screenshot_path)
            logging.error(f"Screenshot de falha salvo em: {screenshot_path}")