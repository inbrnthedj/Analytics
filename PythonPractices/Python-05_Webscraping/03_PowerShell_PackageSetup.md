# PowerShell Commands & Troubleshooting Guide for Python Web Scraping

Reference guide for installing, updating, and managing Python packages (`pandas`, `beautifulsoup4`, `requests`, `lxml`) in Windows PowerShell / VS Code terminal.

## Quick Cheat Sheet

| Goal | PowerShell Command | Description |
| :--- | :--- | :--- |
| **Check Python Version** | `python --version` | Displays installed Python version. |
| **Check Installed Packages** | `python -m pip list` | Lists all packages installed in active environment. |
| **Upgrade `pip`** | `python -m pip install --upgrade pip` | Updates the Python package installer. |
| **Install Pandas** | `python -m pip install pandas lxml html5lib` | Installs `pandas` and HTML parsing engines. |
| **Install BeautifulSoup** | `python -m pip install beautifulsoup4 requests` | Installs `beautifulsoup4` (`bs4`) and `requests`. |
| **Install / Update All** | `python -m pip install --upgrade pandas lxml html5lib beautifulsoup4 requests` | Single command to install or upgrade all scraping libraries. |
| **Install Python via Winget** | `winget install --id Python.Python.3.12 --exact` | Installs Python 3.12 on Windows using `winget`. |

---

## Detailed Commands & Package Names

### 1. Upgrade `pip`
Always upgrade `pip` before installing new packages:
```powershell
python -m pip install --upgrade pip
```

### 2. Install Pandas & Table Parsers
`pandas` requires `lxml` or `html5lib` under the hood to parse HTML tables with `pd.read_html()`:
```powershell
python -m pip install pandas lxml html5lib
```

### 3. Install Beautiful Soup & Requests
Beautiful Soup is distributed under the PyPI package name `beautifulsoup4` (imported in Python as `from bs4 import BeautifulSoup`):
```powershell
python -m pip install beautifulsoup4 requests
```

---

## Common Errors & Troubleshooting

### Error 1: `Pylance(reportMissingModuleSource)`
- **Cause**: VS Code is pointing to a broken `.venv` or wrong Python interpreter where the package is missing.
- **Fix**: Press `Ctrl + Shift + P` in VS Code -> Select `Python: Select Interpreter` -> Choose your active Global Python environment.

### Error 2: `ModuleNotFoundError: No module named 'bs4'`
- **Cause**: Package `beautifulsoup4` has not been installed in your active Python environment.
- **Fix**: Run `python -m pip install beautifulsoup4` in terminal.

### Error 3: `Python non è stato trovato...` (Python not found)
- **Cause**: Python executable is missing or not registered in your Windows `PATH` environment variable.
- **Fix**: Download Python installer from [python.org](https://www.python.org/downloads/) and check **"Add python.exe to PATH"** during setup.
