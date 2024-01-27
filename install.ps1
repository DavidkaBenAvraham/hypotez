# Устанавливаем политику выполнения
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Клонируем репозиторий `hypotez`
#git clone https://github.com/DavidkaBenAvraham/hypotez

# Переходим в директорию hypotez
#cd hypotez


# Создаем виртуальное окружение `venv`. Название окружения прописано в коде.
# Желательно не менять его
python -m venv venv
Write-Output " ######################### Создано виртуальное окружение ######################"

# Прописываем путь к каталогу с кодом
# Получаем путь к директории, содержащей activate.ps1
$venvDir = Get-Item -LiteralPath (Split-Path $MyInvocation.MyCommand.Path)

# Полный путь к activate.ps1
$activatePath = Join-Path -Path $venvDir -ChildPath "Scripts\Activate.ps1"

Rename-Item -Path Join-Path -Path venvDir -ChildPath "Scripts\Activate.ps1" -NewName "Scripts\___Activate.ps1"
#копия моего файла активации
Copy-Item -Path "src/templates/Activate.ps1" -Destination $activatePath

Write-Output " ######################### Перезаписан скрипт активации ######################"


# Строка, которую мы хотим добавить
$lineToAdd = '$env:PYTHONPATH += ";$PSScriptRoot\src"'

# Добавляем строку в конец файла
Add-Content -Path $activatePath -Value $lineToAdd

# Ссылка `py` на `python`
$venvPythonPath = (Get-Command python.exe).Path
$pyLinkPath = .\venv\Scripts\py.exe

# Проверяем существование символической ссылки
if (-Not (Test-Path $pyLinkPath -PathType Leaf)) {
    # Создаем ссылку, если она не существует
    New-Item -ItemType SymbolicLink -Path $pyLinkPath -Target $venvPythonPath

    Write-Host "Ссылка 'py.exe' успешно создана."
} else {
    Write-Host "Ссылка 'py.exe' уже существует."
}

# Переходим в директорию hypotez
Set-Location hypotez

# Ссылка `ju` на `jupyter-notebook`
$venvJupyterPath = (Get-Command jupyter.exe -notebook).Path
$juLinkPath = .\venv\Scripts\ju.cmd  # .cmd расширение для обеспечения корректной работы на Windows

# Проверяем существование символической ссылки
if (-Not (Test-Path $juLinkPath -PathType Leaf)) {
    # Создаем ссылку, если она не существует
    New-Item -ItemType SymbolicLink -Path $juLinkPath -Target $venvJupyterPath

    Write-Host "Ссылка 'ju' успешно создана."
} else {
    Write-Host "Ссылка 'ju' уже существует."
}

# Добавляем строку в конец файла src\activate.ps1, чтобы настроить окружение для Jupyter
$lineToAddJupyter = 'function ju { Start-Process jupyter-notebook }'
Add-Content -Path .\activate.ps1 -Value $lineToAddJupyter

# Активируем виртуальное окружение
. .\venv\Scripts\Activate.ps1

# Обновляем `pip`
python -m pip install --upgrade pip

# Устанавливаем зависимости из requirements.txt. Флаг `--ignore-installed` позволяет продолжить установку других зависимостей,
# даже если одна из них вызывает ошибку.
pip install -r requirements.txt --ignore-installed

# Создаем папку docs
New-Item -ItemType Directory -Path .\docs
New-Item -ItemType Directory -Path .\export
New-Item -ItemType Directory -Path .\log
New-Item -ItemType Directory -Path .\tmp

# Переходим в директорию docs
#cd .\docs

# Клонируем репозиторий `docs` внутри директории hypotez
git clone https://github.com/DavidkaBenAvraham/docs


# Переходим в директорию doxygen
Set-Location .\docs\doxygen

New-Item -ItemType Directory -Path .\_build
New-Item -ItemType Directory -Path .\_build\ru
New-Item -ItemType Directory -Path .\_build\en


# Запускаем doxyrun
./doxyrun

# Переходим в директорию src
Set-Location .
