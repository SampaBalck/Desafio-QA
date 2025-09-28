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

        # --- Localizadores para a página "Elements" ---
        self.elements = (By.XPATH, "//h5[text()='Elements']")
        self.Web_Tables = (By.XPATH, "//span[text()='Web Tables']")
        self.addNew_Record_Button_button = (By.ID, "addNewRecordButton")

        # --- Localizadores do Formulário de Registro ---
        self.modal = (By.CLASS_NAME, "modal-content")
        self.firstName_field = (By.ID, "firstName")
        self.lastName_field = (By.ID, "lastName")
        self.userEmail_field = (By.ID, "userEmail")
        self.age_field = (By.ID, "age")
        self.salary_field = (By.ID, "salary")
        self.department_field = (By.ID, "department")
        self.submit_button = (By.ID, "submit")

        self.edit_button = (By.XPATH, "//*[@id='edit-record-4']")
        self.delete_button = (By.XPATH, "//*[@id='delete-record-4']")

        


    
        

      

        # # --- Localizadores para a página "Progress Bar" ---
        # self.widgets_menu = (By.XPATH, "//h5[text()='Widgets']")
        # self.submenu_progress_bar = (By.XPATH, "//span[text()='Progress Bar']")
        # self.start_stop_button = (By.ID, "startStopButton")
        # self.progress_bar = (By.XPATH, "//div[@role='progressbar']")
        # # self.reset_button = (By.ID, "resetButton")

    # --- MÉTODO GERAL ---
    def Dado_que_como_usuario_devo_acessar_a_pagina_demoga(self):
        """Verifica se o título da página está visível, confirmando o carregamento."""
        time.sleep(3)
        self.verificar_se_elemento_esta_visivel(self.titulo_field)
        print("Página do DemoQA acessada com sucesso. Título verificado.")

    # --- MÉTODOS PARA O TESTE DE "Web Tables" ---
    def Quando_navegar_para_a_pagina_de_elements(self):
    #     """Navega pelo menu até a página da barra de Web Tables."""
        print("\n--- Navegando para a página Web Tables ---")
        self.rolar_para_o_elemento(self.elements)
        self.clicar(self.elements)
        print("Clicou em 'Elements'.")
        time.sleep(1)
        self.rolar_para_o_elemento(self.Web_Tables)
        self.clicar(self.Web_Tables)
        self.clicar(self.addNew_Record_Button_button)
        print("Clicou no submenu 'WebT ables'.")
        time.sleep(1)



    def E_criar_um_novo_registro(self, firstName: str, lastName: str, userEmail: str, age: int, salary: int, department: str):
        # Espera o modal abrir antes de procurar o campo
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.modal)
        )

        # Primeiro nome
        campo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.firstName_field)
        )
        campo.clear()
        campo.send_keys(firstName)
        print(f"✅ Nome '{firstName}' preenchido com sucesso.")

        # Segundo nome
        campo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.lastName_field)
        )
        campo.clear()
        campo.send_keys(lastName)
        print(f"✅ Nome '{lastName}' preenchido com sucesso.")

        # Email
        campo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.userEmail_field)
        )
        campo.clear()
        campo.send_keys(userEmail)
        print(f"✅ Nome '{userEmail}' preenchido com sucesso.")

        # Idade
        campo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.age_field)
        )
        campo.clear()
        campo.send_keys(age)
        print(f"✅ Nome '{age}' preenchido com sucesso.")

        # Salario
        campo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.salary_field)
        )
        campo.clear()
        campo.send_keys(salary)
        print(f"✅ Nome '{salary}' preenchido com sucesso.")

        # Departamento
        campo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.department_field)
        )
        campo.clear()
        campo.send_keys(department)
        print(f"✅ Nome '{department}' preenchido com sucesso.")

        # --- Submissão do Formulário com Espera Explícita ---
        print("Tentando clicar no botão 'Submit'...")
        botao_submit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit_button)
        )
        botao_submit.click()
        print("✅ Botão 'Submit' clicado com sucesso.")

    def E_clicar_no_botao_editar(self, firstName: str):
        time.sleep(1)
        self.rolar_para_o_elemento(self.edit_button)
        self.clicar(self.edit_button)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.modal)
        )

        # Primeiro nome
        campo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.firstName_field)
        )
        campo.clear()
        campo.send_keys(firstName)
        print(f"✅ Nome '{firstName}' preenchido com sucesso.")

        # --- Submissão do Formulário com Espera Explícita ---
        print("Tentando clicar no botão 'Submit'...")
        botao_submit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit_button)
        )
        botao_submit.click()
        print("✅ Botão 'Submit' clicado com sucesso.")

    def Entao_será_possivel_exclui_ao_clicar_no_botao_excluir(self):
        time.sleep(1)
        self.rolar_para_o_elemento(self.delete_button)
        self.clicar(self.delete_button)
        
       
    # def E_criar_um_novo_registro(self, first_name: str, last_name: str, email: str, age: str, salary: str, department: str):
    #     """Preenche o formulário do modal e cria um novo registro"""

    #     # Espera o modal abrir
    #     WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located(self.modal)
    #     )

    #     # Preencher os campos
    #     campos = [
    #         (self.first_name_field, first_name, "first_name"),
    #         (self.last_name_field, last_name, "lastName"),
    #         (self.user_email_field, email, "Email"),
    #         (self.age_field, age, "Idade"),
    #         (self.salary_field, salary, "Salário"),
    #         (self.department_field, department, "Departamento"),
    #     ]

    #     for locator, valor, descricao in campos:
    #         campo = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(locator)
    #         )
    #         campo.clear()
    #         campo.send_keys(valor)
    #         print(f"✅ {descricao} '{valor}' preenchido com sucesso.")
       


    # def _parar_e_validar_barra(self, valor_alvo: int, timeout: int = 60):
    #     """Método auxiliar para parar a barra de progresso e validar."""
    #     self.clicar(self.start_stop_button)
    #     end = time.time() + timeout

    #     while time.time() < end:
    #         elem = self.encontrar_elemento(self.progress_bar)
    #         texto = elem.text.strip()
    #         try:
    #             valor = int(elem.get_attribute("aria-valuenow") or -1)
    #         except (TypeError, ValueError):
    #             valor = -1

    #         if valor >= valor_alvo or texto == str(valor_alvo):
    #             self.clicar(self.start_stop_button)
    #             time.sleep(0.5)
    #             break
    #         time.sleep(0.02)

    #     # validação final (mais tolerante)
    #     elem = self.encontrar_elemento(self.progress_bar)
    #     texto_final = elem.text.strip()
    #     try:
    #         valor_final = int(elem.get_attribute("aria-valuenow") or -1)
    #     except (TypeError, ValueError):
    #         valor_final = -1

    #     assert texto_final == str(valor_alvo) or valor_final >= valor_alvo, (
    #         f"FALHA: esperado {valor_alvo}% (ou >= {valor_alvo}), mas foi texto='{texto_final}', aria-valuenow={valor_final}"
    #     )
    #     print(f"✅ SUCESSO: barra parada — texto='{texto_final}', aria-valuenow={valor_final}")

    #     self.clicar(self.start_stop_button)
    #     time.sleep(3)

    # def E_devo_parar_a_barra_em_25_porcento_e_validar(self):
    #     """Para a barra em 25%."""
    #     self._parar_e_validar_barra(25)

    
    # def Entao_devo_parar_a_barra_em_100_porcento_e_validar(self, timeout: int = 120):
    #     """Para a barra em 100% de forma confiável, continuando após 25%."""

    #     wait = WebDriverWait(self.driver, timeout)
    #     wait.until(EC.visibility_of_element_located(self.progress_bar))

    #     # Inicia a barra
    #     self.clicar(self.start_stop_button)
    #     print("Iniciando a barra de progresso para 100%...")

    #     valor_anterior = -1
    #     inicio = time.time()

    #     while True:
    #         if time.time() - inicio > timeout:
    #             raise TimeoutError("A barra de progresso não completou 100% dentro do timeout.")

    #         elem = self.encontrar_elemento(self.progress_bar)
    #         texto = elem.text.strip().replace("%", "")
    #         try:
    #             valor = int(elem.get_attribute("aria-valuenow") or -1)
    #         except (TypeError, ValueError):
    #             valor = -1

    #         # Se travar antes de 100%, clicar Start novamente
    #         if valor == valor_anterior and valor < 100:
    #             print(f"Barra travou em {valor}%, reiniciando...")
    #             self.clicar(self.start_stop_button)
    #             time.sleep(0.2)

    #         valor_anterior = valor

    #         # Validar que chegou em 100%
    #         if valor >= 100 or texto == "100":
    #             print(f"Barra atingiu 100% (valor={valor}%)")
    #             break

    #         time.sleep(0.1)

    #     # Validação final antes de reset
    #     assert valor >= 100 or texto == "100", (
    #         f"FALHA: esperado 100%, mas foi texto='{texto}', aria-valuenow={valor}"
    #     )
    #     print(f"✅ SUCESSO: barra chegou em 100% — texto='{texto}', aria-valuenow={valor}")

    #     # Encerra o teste clicando Reset
    #     self.clicar(self.reset_button)
    #     print("Barra resetada com sucesso, teste encerrado.")
