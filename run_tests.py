# pytest run_tests.py

import pytest
from datetime import datetime
from pathlib import Path
import webbrowser # <-- 1. ADICIONE ESTA LINHA NO TOPO

if __name__ == "__main__":
    # 1. Pega a data e hora atuais para usar no nome da pasta
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # 2. Define o caminho da pasta de relatórios
    # Ex: reports/run_2025-09-06_22-15-30
    run_dir = Path("reports") / f"run_{now}"
    
    # 3. Cria a pasta (e a pasta 'reports' se ela não existir)
    run_dir.mkdir(parents=True, exist_ok=True)
    print(f"Diretório de relatórios criado em: {run_dir.resolve()}")

    # 4. Define os caminhos completos para cada relatório
    html_report_path = run_dir / "report.html"
    
    # Este é outro tipo de relatório (JUnit XML), muito usado por
    # ferramentas de integração contínua como Jenkins, GitLab CI, etc.
    xml_report_path = run_dir / "results.xml"

    # 5. Monta a lista de argumentos para o pytest
    pytest_args = [
        # Adiciona os testes que você quer rodar (opcional, se não especificar roda todos)
        "api_tests/", 
        
        # Argumento para o relatório HTML
        f"--html={html_report_path}",
        "--self-contained-html",
        
        # Argumento para o relatório JUnit XML
        f"--junitxml={xml_report_path}",

        # Para ver os prints no terminal
        "-s" 
    ]
    
    # 6. Executa o pytest com os argumentos definidos
    print(f"Executando testes...")
    pytest.main(pytest_args)
    print(f"Testes finalizados. Relatórios salvos em: {run_dir.resolve()}")


    # 2. ADICIONE ESTAS DUAS LINHAS NO FINAL DO ARQUIVO:
    print("Abrindo relatório no navegador...")
    webbrowser.open(f"file://{html_report_path.resolve()}")