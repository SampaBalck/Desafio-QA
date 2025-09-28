import time
import conftest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

class BasePage:
    """
    Esta classe base contém todos os métodos comuns e interações com a página
    que serão reutilizados por outras classes de página (Page Objects).
    """

    def __init__(self):
        self.driver = conftest.driver

    # --- MÉTODOS FUNDAMENTAIS DE LOCALIZAÇÃO ---

    def encontrar_elemento(self, locator, timeout=10):
        """
        Encontra e retorna um único elemento na página usando uma espera explícita.
        Lança uma exceção TimeoutException se o elemento não for encontrado.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"ERRO: O tempo de {timeout}s expirou. Elemento não encontrado com o localizador: {locator}")
            raise

    def encontrar_elementos(self, locator, timeout=10):
        """
        Encontra e retorna uma lista de elementos na página.
        Retorna uma lista vazia se nenhum elemento for encontrado.
        """
        try:
            # Espera pelo menos um elemento estar presente antes de retornar a lista
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return [] # Retorna lista vazia se nada for encontrado

    # --- MÉTODOS DE INTERAÇÃO BÁSICA ---

    def clicar(self, locator):
        """Encontra um elemento e clica nele."""
        self.encontrar_elemento(locator).click()

    def escrever(self, locator, text):
        """Limpa um campo de texto e escreve nele."""
        element = self.encontrar_elemento(locator)
        element.clear()
        element.send_keys(text)

    def pegar_texto_elemento(self, locator):
        """Encontra um elemento e retorna o seu texto."""
        return self.encontrar_elemento(locator).text

    # --- MÉTODOS DE AÇÕES AVANÇADAS (ActionChains e JavaScript) ---

    def clicar_com_javascript(self, locator):
        """
        Clica em um elemento usando JavaScript.
        Útil para contornar elementos sobrepostos (banners, pop-ups, etc.).
        """
        element = self.encontrar_elemento(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def clique_duplo(self, locator):
        """Realiza um clique duplo em um elemento."""
        element = self.encontrar_elemento(locator)
        ActionChains(self.driver).double_click(element).perform()

    def clique_botao_direito(self, locator):
        """Clica com o botão direito do mouse em um elemento."""
        element = self.encontrar_elemento(locator)
        ActionChains(self.driver).context_click(element).perform()

    def pressionar_tecla(self, locator, key):
        """Pressiona uma tecla do teclado em um elemento (ex: Keys.ENTER)."""
        elem = self.encontrar_elemento(locator)
        elem.send_keys(key)

    # --- MÉTODOS DE VERIFICAÇÃO E ASSERTS ---

    def verificar_se_elemento_esta_visivel(self, locator):
        """Verifica se um elemento está visível na tela. Falha o teste se não estiver."""
        element = self.encontrar_elemento(locator)
        assert element.is_displayed(), f"FALHA: O elemento '{locator}' deveria estar visível, mas não está."

    def verificar_se_elemento_nao_existe(self, locator):
        """Verifica se um elemento NÃO existe na tela. Falha o teste se ele for encontrado."""
        elementos = self.encontrar_elementos(locator, timeout=2) # Um timeout menor é ideal aqui
        assert len(elementos) == 0, f"FALHA: O elemento '{locator}' não deveria existir, mas foi encontrado."

    def verificar_se_radio_esta_selecionado_e_clicar(self, locator):
        """Verifica se um botão de rádio está selecionado e clica caso não esteja."""
        elemento_radio = self.encontrar_elemento(locator)
        if not elemento_radio.is_selected():
            elemento_radio.click()

    # --- MÉTODOS DE ROLAGEM (SCROLL) ---

    def rolar_para_o_elemento(self, locator):
        """Rola a página até que um elemento específico esteja visível."""
        element = self.encontrar_elemento(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def rolar_para_o_fim_da_pagina(self):
        """Rola até o final da página."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1) # Pausa para conteúdo dinâmico (lazy loading) carregar

    def verificar_se_radio_selecionado_e_clicar(self, locator):
        try:
            elemento_radio = self.encontrar_elemento(locator)

            # Verifica se o elemento radio está presente na tela
            if elemento_radio.is_displayed():
                # Verifica se o radio está selecionado, se não estiver, clica nele
                elemento_radio.click()
                if not elemento_radio.is_selected():
                    elemento_radio.click()
                    # self.clicar(elemento_radio)
        except:
            # Caso não consiga encontrar o elemento, simplesmente ignore e prossiga
            pass