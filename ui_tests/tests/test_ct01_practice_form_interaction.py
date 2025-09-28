# pytest -v .\ui_tests\tests\test_ct01_practice_form_interaction.py

import pytest
from pages.acesso_pagina_practice_form import AcessoPage
import conftest

@pytest.mark.usefixtures("setup_teardown")
class TestCT01:

    def test_01_Acesso_Pagina_demoqa_com_metodos_de_practice_form_(self):
        acesso = AcessoPage()
        acesso.Dado_que_como_usuario_devo_acessar_a_pagina_demoqa()
        acesso.Quando_navegar_para_a_pagina_de_practice_form()
        acesso.E_preencher_o_formulario_da_pagina_de_practice_form(
            first_name="Joao",
            last_name="Silva",
            email="joao.silva@email.com",
            gender="Male",
            phone="1199999888",
            date_of_birth="10 May 1990",
            subjects="Maths"
            # hobbies="Sports"
        #     picture_path="C:/Users/Public/Pictures/sample.jpg",
        #     address="Rua Exemplo, 123",
        #     state="NCR",
        #     city="Delhi"
        )


        # acesso.Entao_devo_parar_a_barra_em_100_porcento_e_validar() 
