import time
import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.bases_page import BasePage

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

    # --- MÉTODO GERAL ---

    def Dado_que_como_usuario_devo_acessar_a_pagina_demoga(self):
        """Verifica se o título da página está visível, confirmando o carregamento."""
        self.verificar_se_elemento_esta_visivel(self.titulo_field)
        print("Página do DemoQA acessada com sucesso. Título verificado.")

    # --- MÉTODOS PARA O TESTE DE "SORTABLE" (DRAG AND DROP) ---

    def Quando_escolher_opcao_Interactions_e_clicar_no_submenu_Sortable(self):
        """Rola e clica no menu 'Interactions' e depois no submenu 'Sortable'."""
        print("\n--- Navegando para a página Sortable ---")
        self.rolar_para_o_elemento(self.interactions)
        self.clicar(self.interactions)
        print("Clicou em 'Interactions' com sucesso.")
        time.sleep(1)
        self.clicar_com_javascript(self.submenu_sortable)
        print("Clicou no submenu 'Sortable' com sucesso.")

    def Entao_devo_ordenar_a_lista_movendo_um_elemento(self):
        """Demonstra o drag and drop movendo o item 'Six' para a posição do 'One'."""
        try:
            source_element = self.encontrar_elemento(self.item_six)
            target_element = self.encontrar_elemento(self.item_one)
            actions = ActionChains(self.driver)
            print("Iniciando a ação de arrastar e soltar...")
            actions.drag_and_drop(source_element, target_element).perform()
            print("Ação de drag and drop executada com sucesso!")
            time.sleep(3)
        except Exception as e:
            print(f"Ocorreu um erro durante o drag and drop: {e}")
            self.driver.save_screenshot("erro_drag_and_drop.png")
            raise

    # --- MÉTODOS PARA O TESTE DE "PROGRESS BAR" ---

    def Quando_navegar_para_a_pagina_de_progress_bar(self):
        """Navega pelo menu até a página da barra de progresso."""
        print("\n--- Navegando para a página Progress Bar ---")
        self.rolar_para_o_elemento(self.widgets_menu)
        self.clicar(self.widgets_menu)
        print("Clicou em 'Widgets'.")
        time.sleep(1)
        self.rolar_para_o_elemento(self.submenu_progress_bar)
        self.clicar(self.submenu_progress_bar)
        print("Clicou no submenu 'Progress Bar'.")
        time.sleep(1)

    def Entao_devo_parar_a_barra_em_25_porcento_e_validar(self):
        """
        Inicia a barra de progresso, para exatamente em 25% e valida o resultado.
        """
        self.clicar(self.start_stop_button)
        print("\n--- Iniciando o teste da barra de progresso ---")
        print("Clicou em 'Start'. Monitorando para parar em 25%...")

        while True:
            valor_atual = int(self.encontrar_elemento(self.progress_bar).get_attribute("aria-valuenow"))
            if valor_atual >= 25:
                self.clicar(self.start_stop_button)
                print(f"Botão 'Stop' pressionado com o valor de {valor_atual}%.")
                print("Pausando por 3 segundos para visualização...")
                time.sleep(3)
                break
            time.sleep(0.05)

        valor_apos_parada = int(self.encontrar_elemento(self.progress_bar).get_attribute("aria-valuenow"))
        assert valor_apos_parada == 25, f"FALHA: O valor deveria ser 25%, mas parou em {valor_apos_parada}%."
        print(f"✅ SUCESSO: A barra de progresso parou corretamente em {valor_apos_parada}%.")