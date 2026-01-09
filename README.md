# API Testing Project

Proyecto de pruebas automatizadas para APIs REST utilizando Python, pytest y jsonschema.

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git 

## 🚀 Instalación

### 1. Clonar el repositorio 

```bash
git clone https://github.com/AnderGGomez96/Test-backend
cd Test-backend
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```


## 🧪 Ejecución de Tests

### Ejecutar todos los tests

```bash
pytest
```

### Ejecutar tests por markers

**Tests positivos:**
```bash
pytest -m positive
```

**Tests negativos:**
```bash
pytest -m negative
```

## 📊 Reportes

Los tests están configurados con las siguientes opciones en `pytest.ini`:

- `-v`: Modo verbose (muestra detalles de cada test)
- `-ra`: Muestra resumen de todos los resultados
- `--tb=short`: Traceback corto en caso de errores
- `--strict-markers`: Error si se usa un marker no declarado

## 🏷️ Markers Disponibles

- `@pytest.mark.positive`: Tests de casos exitosos
- `@pytest.mark.negative`: Tests de casos de error

## 📦 Dependencias Principales

- **pytest** (9.0.2): Framework de testing
- **requests** (2.32.5): Cliente HTTP para consumir APIs
- **jsonschema** (4.26.0): Validación de schemas JSON

