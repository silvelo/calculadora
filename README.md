![CI](https://github.com/silvelo/calculadora/actions/workflows/ci.yml/badge.svg)


1. Clonar el proyecto
  
    ```bash
    git clone git@github.com:silvelo/calculadora.git
    cd calculadora
    ```

2. Crear entorno virtual

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # Linux/macOS
    ```

3. Instalar dependencias
    
    ```
    pip install -r requirements.txt
    pre-commit install         # instala los hooks configurados
    ```

4. Ejecuta linters

    ```
    black .
    isort .
    flake8 .
    ```

5. Ejecutar test

   ```
   pytest -v
   ```
