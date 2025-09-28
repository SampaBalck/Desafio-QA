#  pytest -v .\ui_tests\tests\test_ct05_process_bar_interaction.py

import time
import conftest
from selenium.webdriver.common.by import By
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

        # --- Localizadores para a página "Elements" ---
        self.frame_windows = (By.XPATH, "//h5[text()='Alerts, Frame & Windows']")
        self.browser_windows = (By.XPATH, "//span[text()='Browser Windows']")
        self.new_windows_button = (By.XPATH, "//button[@id='windowButton' and text()='New Window']")

        self.browser_Windows_titulo = (By.XPATH, "//h1[text()='Browser Windows']")

        # Localizador do texto na nova página
        self.sample_page_text = (By.ID, "sampleHeading")

        

        
    def Dado_que_como_usuario_devo_acessar_a_pagina_demoga(self):
        """Verifica se o título da página está visível, confirmando o carregamento."""
        self.verificar_se_elemento_esta_visivel(self.titulo_field)
        print("Página do DemoQA acessada com sucesso. Título verificado.")

    def Quando_navegar_para_a_pagina_de_Alerta_frame_windows(self):
        """Navega pelo menu até a página do frame_windows."""
        print("\n--- Navegando para a página frame_windows ---")
        self.rolar_para_o_elemento(self.frame_windows)
        self.clicar(self.frame_windows)
        print("Clicou em 'Forms'.")
        time.sleep(1)
        
    def E_selecionar_o_submenu_browser_windows(self):    
        # self.rolar_para_o_elemento(self.frame_windows)
        self.clicar(self.browser_windows)
        print("Clicou em 'Forms'.")
        self.rolar_para_o_elemento(self.browser_windows)
        time.sleep(1)

    def Entao_devo_clicar_em_new_window_e_validar_a_frase(self):
        """
        Clica no botão 'New Window', muda o foco para a nova janela,
        valida o texto "This is a sample page" e depois retorna à janela principal.
        """
        print("Iniciando validação da nova janela...")
        
        janela_original = self.driver.current_window_handle
        print(f"Janela original: {janela_original}")

        self.clicar(self.new_windows_button)
        print("Clicou no botão 'New Window'.")

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        for handle in self.driver.window_handles:
            if handle != janela_original:
                self.driver.switch_to.window(handle)
                print(f"Foco mudou para a nova janela: {handle}")
                break
        
        print("Validando texto na nova janela...")
        self.verificar_se_elemento_esta_visivel(self.sample_page_text)
        texto_capturado = self.pegar_texto_elemento(self.sample_page_text)
        
        assert texto_capturado == "This is a sample page", f"ERRO: Texto esperado era 'This is a sample page', mas foi encontrado '{texto_capturado}'"
        print("✅ Frase 'This is a sample page' validada com sucesso!")

        self.driver.close()
        self.driver.switch_to.window(janela_original)
        print("Nova janela fechada e foco retornado para a original.")
   
