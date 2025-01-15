# Financial Time-Series Forecasting Archive

This repository contains a collection of financial time-series forecasting models. It produces esting a benchmark for prac

## Create Virtual Environment
The virtual environment is created using conda. It is used to manage the dependencies of the package.

The following steps are used to create the virtual environment.

Inside your terminal, write:
```bash
conda create -n ftsf python=3.12.6
```

Activate virtual environment:
```bash
conda activate ftsf
```

Install packages:
```bash
pip install -r requirements-dev.txt
```

Install pre-commit hooks:
```bash
pre-commit install
```

# Migrations
## On macOS/Linux
```bash
export FLASK_APP=run.py
```

```bash
export FLASK_ENV=development
```

```bash
python -m flask db init
```

```bash
python -m flask db migrate -m "Initial migration for Development SQLite"
```

```bash
python -m flask db upgrade
```

```bash
export FLASK_ENV=production
```

```bash
python -m flask db init
```

```bash
python -m flask db migrate -m "Initial migration for Production SQLite"
```

```bash
python -m flask db upgrade
```

## On Windows (Command Prompt)
```bash
set FLASK_APP=run.py
```

```bash
set FLASK_ENV=development
```

```bash
python -m flask db init
```

```bash
python -m flask db migrate -m "Initial migration for Development SQLite"
```

```bash
python -m flask db upgrade
```

```bash
set FLASK_ENV=production
```

```bash
python -m flask db init
```

```bash
python -m flask db migrate -m "Initial migration for Production SQLite"
```

```bash
python -m flask db upgrade
```

## On Windows (PowerShell)
```powershell
$env:FLASK_APP="run.py"
```

```powershell
$env:FLASK_ENV="development"
```

```powershell
python -m flask db init
```

```powershell
python -m flask db migrate -m "Initial migration for Development SQLite"
```

```powershell
python -m flask db upgrade
```

```powershell
$env:FLASK_ENV="production"
```

```powershell
python -m flask db init
```

```powershell
python -m flask db migrate -m "Initial migration for Production SQLite"
```

```powershell
python -m flask db upgrade
```
