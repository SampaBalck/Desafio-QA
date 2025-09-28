import time
import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.bases_page import BasePage


class AcessoPage(BasePage):
    """
    Esta classe contém os localizadores e métodos para interações
    com o menu Forms e a página Practice Form.
    """

    def __init__(self):
        super().__init__()
        self.driver = conftest.driver

        # --- Localizadores Gerais ---
        self.titulo_field = (By.XPATH, "//*[@id='app']/header/a/img")

        # --- Localizadores para o menu "Forms" ---
        self.forms_menu = (By.XPATH, "//h5[text()='Forms']")
        self.submenu_practice_form = (By.XPATH, "//span[text()='Practice Form']")

        # --- Campos do formulário ---
        self.first_name_field = (By.ID, "firstName")
        self.last_name_field = (By.ID, "lastName")
        self.userEmail_field = (By.ID, "userEmail")
        self.gender_male_radio = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
        self.userNumber_field = (By.ID, "userNumber")
        self.date_of_birth_input = (By.ID, "dateOfBirthInput")

        # --- Localizadores para o campo "Subjects" ---
        self.subjects_container = (By.XPATH, '//*[@id="subjectsContainer"]/div/div[1]')
        self.subjects_input = (By.CSS_SELECTOR, "input[id^='react-select-'][id$='-input']")
        self.subjects_selected_label = (By.XPATH, "//*[@id='subjectsContainer']")

        # --- Outros campos ---
        self.uploadPicture_field = (By.ID, "uploadPicture")
        self.currentAddress_field = (By.ID, "currentAddress")
        self.state_dropdown = (By.ID, "state")
        self.city_dropdown = (By.ID, "city")
        self.submit_button = (By.ID, "submit")

    # --- MÉTODO GERAL ---
    def Dado_que_como_usuario_devo_acessar_a_pagina_demoqa(self):
        """Verifica se o título da página está visível, confirmando o carregamento."""
        self.verificar_se_elemento_esta_visivel(self.titulo_field)
        print("✅ Página do DemoQA acessada com sucesso. Título verificado.")

    # --- MÉTODOS PARA O TESTE DE "Practice Form" ---
    def Quando_navegar_para_a_pagina_de_practice_form(self):
        """Navega pelo menu até a página do formulário de prática."""
        print("\n--- Navegando para a página Practice Form ---")
        self.rolar_para_o_elemento(self.forms_menu)
        self.clicar(self.forms_menu)
        print("Clicou em 'Forms'.")
        time.sleep(1)

        self.clicar(self.submenu_practice_form)
        print("Clicou no submenu 'Practice Form'.")
        time.sleep(2)

    def E_preencher_o_formulario_da_pagina_de_practice_form(
        self,
        first_name,
        last_name,
        email,
        gender,
        phone,
        date_of_birth,
        subjects=None,
        hobbies=None,
        picture_path=None,
        address=None,
        state=None,
        city=None
    ):
        """Preenche o formulário da página Practice Form."""
        self.escrever(self.first_name_field, first_name)
        self.escrever(self.last_name_field, last_name)
        self.escrever(self.userEmail_field, email)

        # Corrigido: clique no gênero usando JS para evitar overlay de anúncios
        if gender and gender.lower() == "male":
            element = self.driver.find_element(*self.gender_male_radio)
            self.driver.execute_script("arguments[0].click();", element)

        self.escrever(self.userNumber_field, phone)
        self.escrever(self.date_of_birth_input, date_of_birth)
