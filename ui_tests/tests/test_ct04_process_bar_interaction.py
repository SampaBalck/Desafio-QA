# pytest -v .\ui_tests\tests\test_ct05_sortable_interaction.py

import pytest
# CORREÇÃO: O nome da classe foi ajustado de AcessoPagina para AcessoPage
from pages.acesso_pagina_process_bar import AcessoPage  
import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_01_Acesso_Pagina_demoga_com_metodos_de_progress_bar(self):
        acesso = AcessoPage()
        acesso.Dado_que_como_usuario_devo_acessar_a_pagina_demoga()
        acesso.Quando_navegar_para_a_pagina_de_progress_bar()            # método existente no Page Object
        acesso.E_devo_parar_a_barra_em_25_porcento_e_validar() 
        acesso.Entao_devo_parar_a_barra_em_100_porcento_e_validar() 
