# pytest -v .\ui_tests\tests\test_ct02_elements_frame_windows.py
# pytest -v

import pytest
# CORREÇÃO: O nome da classe foi ajustado de AcessoPagina para AcessoPage
from pages.acesso_pagina_frame_windows import AcessoPage  
import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_01_Acesso_Pagina_demoga_com_metodos_de_frame_windows(self):
        acesso = AcessoPage()

        acesso.Dado_que_como_usuario_devo_acessar_a_pagina_demoga()             
        acesso.Quando_navegar_para_a_pagina_de_Alerta_frame_windows()  
        acesso.E_selecionar_o_submenu_browser_windows()        
        acesso.Entao_devo_clicar_em_new_window_e_validar_a_frase()
        
        