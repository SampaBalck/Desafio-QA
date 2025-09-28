#  pytest -v .\ui_tests\tests\test_ct05_process_bar_interaction.py

import time
import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.bases_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AcessoPage(BasePage):
    """
    Esta classe contém os localizadores e métodos para todas as interações
    da página de demonstração, herdando os métodos da BasePage.
    """

    def __init__(self):
        super().__init__()
        self.driver = conftest.driver

        # --- Localizadores Gerais ---
        self.titulo_field = (By.XPATH, "//*[@id='app']/header/a/img")

        # --- Localizadores para a página "Sortable" ---
        self.interactions = (By.XPATH, "//h5[text()='Interactions']")
        self.submenu_sortable = (By.XPATH, "//span[text()='Sortable']")
        self.item_one = (By.XPATH, "//div[contains(@class, 'vertical-list-container')]//div[text()='One']")
        self.item_six = (By.XPATH, "//div[contains(@class, 'vertical-list-container')]//div[text()='Six']")

        # --- Localizadores para a página "Progress Bar" ---
        self.widgets_menu = (By.XPATH, "//h5[text()='Widgets']")
        self.submenu_progress_bar = (By.XPATH, "//span[text()='Progress Bar']")
        self.start_stop_button = (By.ID, "startStopButton")
        self.progress_bar = (By.XPATH, "//div[@role='progressbar']")
        self.reset_button = (By.ID, "resetButton")

    # --- MÉTODO GERAL ---
    def Dado_que_como_usuario_devo_acessar_a_pagina_demoga(self):
        """Verifica se o título da página está visível, confirmando o carregamento."""
        self.verificar_se_elemento_esta_visivel(self.titulo_field)
        print("Página do DemoQA acessada com sucesso. Título verificado.")

    # --- MÉTODOS PARA O TESTE DE "PROGRESS BAR" ---
    def Quando_navegar_para_a_pagina_de_progress_bar(self):
        """Navega pelo menu até a página da barra de progresso."""
        print("\n--- Navegando para a página widgets ---")
        self.rolar_para_o_elemento(self.widgets_menu)
        self.clicar(self.widgets_menu)
        print("Clicou em 'Widgets'.")
        time.sleep(1)
        self.rolar_para_o_elemento(self.submenu_progress_bar)
        self.clicar(self.submenu_progress_bar)
        print("Clicou no submenu 'Progress Bar'.")
        time.sleep(1)

    def _parar_e_validar_barra(self, valor_alvo: int, timeout: int = 60):
        """Método auxiliar para parar a barra de progresso e validar."""
        self.clicar(self.start_stop_button)
        end = time.time() + timeout

        while time.time() < end:
            elem = self.encontrar_elemento(self.progress_bar)
            texto = elem.text.strip()
            try:
                valor = int(elem.get_attribute("aria-valuenow") or -1)
            except (TypeError, ValueError):
                valor = -1

            if valor >= valor_alvo or texto == str(valor_alvo):
                self.clicar(self.start_stop_button)
                time.sleep(0.5)
                break
            time.sleep(0.02)

        # validação final (mais tolerante)
        elem = self.encontrar_elemento(self.progress_bar)
        texto_final = elem.text.strip()
        try:
            valor_final = int(elem.get_attribute("aria-valuenow") or -1)
        except (TypeError, ValueError):
            valor_final = -1

        assert texto_final == str(valor_alvo) or valor_final >= valor_alvo, (
            f"FALHA: esperado {valor_alvo}% (ou >= {valor_alvo}), mas foi texto='{texto_final}', aria-valuenow={valor_final}"
        )
        print(f"✅ SUCESSO: barra parada — texto='{texto_final}', aria-valuenow={valor_final}")

        

    def E_devo_parar_a_barra_em_25_porcento_e_validar(self, timeout: int = 27):
        """
        Inicia a barra de progresso, a interrompe antes de 25% e valida o valor final.
        """
        # Inicia a barra
        self.rolar_para_o_elemento(self.progress_bar)
        self.clicar(self.start_stop_button)
        #time.sleep(6)

         # Garante que a barra esteja visível antes de começar
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(self.progress_bar))

        inicio = time.time()
        valor_final = 0

        # Loop para monitorar o progresso
        while True:
            # Proteção contra loops infinitos ou falhas
            if time.time() - inicio > timeout:
                raise TimeoutError("A barra de progresso demorou demais para atingir o ponto de parada.")

            # Pega o valor atual da barra
            elem = self.encontrar_elemento(self.progress_bar)
            try:
                valor_atual = int(elem.get_attribute("aria-valuenow"))
            except (TypeError, ValueError):
                valor_atual = -1

            # 2. Parar antes dos 25%
            # Quando o valor for maior ou igual a 20 (uma margem segura), clica para parar
            if valor_atual >= 23:
                self.clicar(self.start_stop_button)
                print(f"Botão de parar clicado quando a barra atingiu {valor_atual}%.")
                
                # Aguarda um instante para o valor se estabilizar após o clique
                time.sleep(0.5)
                
                # Pega o valor final exato em que a barra parou
                valor_final = int(self.encontrar_elemento(self.progress_bar).get_attribute("aria-valuenow"))
                break

            time.sleep(0.05) # Verifica o valor com frequência

        # 3. Validar que o valor da progress Bar é menor ou igual aos 25%
        assert valor_final <= 24, (
            f"FALHA: A barra parou em {valor_final}%, que é maior que os 25% permitidos."
        )
        print(f"✅ SUCESSO: A barra foi parada em {valor_final}%, dentro do limite de 25%.")


        

    
        
    
    def Entao_devo_parar_a_barra_em_100_porcento_e_validar(self, timeout: int = 120):
        """Para a barra em 100% de forma confiável, continuando após 25%."""

        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(self.progress_bar))

        # Inicia a barra
        self.rolar_para_o_elemento(self.progress_bar)
        self.clicar(self.start_stop_button)
        print("Iniciando a barra de progresso para 100%...")

        valor_anterior = -1
        inicio = time.time()

        while True:
            if time.time() - inicio > timeout:
                raise TimeoutError("A barra de progresso não completou 100% dentro do timeout.")

            elem = self.encontrar_elemento(self.progress_bar)
            texto = elem.text.strip().replace("%", "")
            try:
                valor = int(elem.get_attribute("aria-valuenow") or -1)
            except (TypeError, ValueError):
                valor = -1

            # Se travar antes de 100%, clicar Start novamente
            if valor == valor_anterior and valor < 100:
                print(f"Barra travou em {valor}%, reiniciando...")
                self.clicar(self.start_stop_button)
                time.sleep(0.2)

            valor_anterior = valor

            # Validar que chegou em 100%
            if valor >= 100 or texto == "100":
                print(f"Barra atingiu 100% (valor={valor}%)")
                break

            time.sleep(0.1)

        # Validação final antes de reset
        assert valor >= 100 or texto == "100", (
            f"FALHA: esperado 100%, mas foi texto='{texto}', aria-valuenow={valor}"
        )
        print(f"✅ SUCESSO: barra chegou em 100% — texto='{texto}', aria-valuenow={valor}")

        # Encerra o teste clicando Reset
        self.clicar(self.reset_button)
        print("Barra resetada com sucesso, teste encerrado.")
