# pytest -v .\ui_tests\tests\test_ct03_elements_interaction.py

import pytest
# CORREÇÃO: O nome da classe foi ajustado de AcessoPagina para AcessoPage
from pages.acesso_pagina_elements import AcessoPage  
import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_01_Acesso_Pagina_demoga_com_metodos_de_elements(self):
        acesso = AcessoPage()
        acesso.Dado_que_como_usuario_devo_acessar_a_pagina_demoga()
        acesso.Quando_navegar_para_a_pagina_de_elements()  
        
        acesso.E_criar_um_novo_registro(
            firstName="Joao",
            lastName="Silva",
            userEmail="joao.silva@test.com",
            age=30,
            salary=9000,
            department="QA")           # método existente no Page Object
        
        acesso.E_clicar_no_botao_editar(
            firstName="Joao Batista"
        )
        acesso.Entao_será_possivel_exclui_ao_clicar_no_botao_excluir()


        # acesso.Entao_devo_parar_a_barra_em_100_porcento_e_validar() 
