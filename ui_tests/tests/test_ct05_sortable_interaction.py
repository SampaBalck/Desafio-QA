# pytest -v .\ui_tests\tests\test_ct06_sortable_interaction.py

import pytest
# CORREÇÃO: O nome da classe foi ajustado de AcessoPagina para AcessoPage
from ui_tests.pages.acesso_pagina_sortable import AcessoPage 
import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_01_Acesso_Pagina_demoga_com_metodos_de_drag_and_drop(self):
        # Instancia os objectos a serem usados no teste
        # CORREÇÃO: Usando o nome correto da classe
        acesso_pagina = AcessoPage()
        
        # Chama o método da página
        acesso_pagina.Dado_que_como_usuario_devo_acessar_a_pagina_demoga()
        acesso_pagina.Quando_escolher_opcao_Interactions_e_clicar_no_submenu_Sortable()
        acesso_pagina.Entao_devo_ordenar_a_lista_movendo_um_elemento()

# pytest -v ui_tests/tests/test_ct01_sortable_interaction.py