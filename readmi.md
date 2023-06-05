##PYTHON 
-> PIP

# Creación: ubicarnos en la carpeta donde va estar el project
```python
                           //Nombre del entor
=> Comando: python -m venv venv
```

# Activar el entorno virtual: 
```python
#  Windows (powerShell) 
cd venv
cd Scripts
activate.bat or activate.ps1
cd ..
source venv/Scripts/activate
cd ..
#  windows (GitBash)
source venv/Scripts/activate

#  linux or ManCOS
source venv/bin/activate

```
# Desactivar el entorno virtual: 
```python
#  Windows (powerShell) 
cd venv
cd Scripts
deactivate.bat or deactivate.ps1
cd ..
cd ..
#  windows (GitBash)
deactivate

#  linux or ManCOS
deactivate

```
## PIP 
```python
    pip list
```
## Instalar libreria
```python
pip install nombre_libreria

```
# Crear archivo de instalacion de paquetes (requirements.txt)
```python
pip freeze > requirements.txt
```

# Instalar librerias desde requirements.txt
```python
pip install -r requirements.txt
```