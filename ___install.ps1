# Устанавливаю политику выполнения
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Клонирую репозиторий `docs`
git clone https://github.com/DavidkaBenAvraham/docs

# Клонируею репозитории `presta_python_api_v1`, `presta_python_api_v2` и `presta_python_api_v3`
#git clone https://github.com/DavidkaBenAvraham/presta_python_api_v1 src\prestashop\presta_apis
#git clone https://github.com/DavidkaBenAvraham/presta_python_api_v2 src\prestashop\presta_apis
#git clone https://github.com/DavidkaBenAvraham/presta_python_api_v3 src\prestashop\presta_apis


Write-Output " ######################### Создано виртуальное окружение ######################"
# Создаю виртуальное окружение `venv`. Это название окружения прописано в коде. 
# Желательно не менять его
python -m venv venv

# Активирую виртуальное окружение
venv\Scripts\Activate.ps1

# Обновляю `pip`
python -m pip install --upgrade pip

# Устанавливаю зависимости из requirements.txt. Флаг `--ignore-installed` позволяет продолжить установку других зависимостей,
# даже если одна из них вызывает ошибку.
pip install -r requirements.txt --ignore-installed


# Запускаю Jupyter Lab
#jupyter-lab '..\..\docs\notepads\intro.ipnyb'

# так делается delete
# Remove-Item -Path "hypotez" -Recurse -Force
