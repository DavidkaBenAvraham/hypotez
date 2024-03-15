

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Create project directory (in <user profile>'documents' directory by default)
```bash
cd %USERPROFILE%\documents
mkdir 'hypotez'
cd hypotez
```

3. Clone this repository into project directory
```bash
git clone https://github.com/DavidkaBenAvraham/hypotez
```

4. Create new virtual environment
```bash
py -m venv venv
```

5. Activate new virtual environment
bash

```bash
$ . venv/bin/activate
    """!

    """
```

powershell
```bash
venv/Scripts/Activate.ps1
Set-ExecutionPolicy RemoteSigned
```

6. Install the requirements
```bash
py -m pip install --upgrade pip
pip install -r requirements.txt
```


7. Make a copy of the example environment variables file
```bash
cp secrets_file_example.py venv/secrets_file.py
```


8. Init git
```bash
$ git init
```

9. Change LF to CRLF
```bash
$ git config --global core.autocrlf true
```


10. add all files to created repository 
(without exluded in .gitignore)
```bash
$ git add .
```

11. First commit
```bash
$ git commit -m "First commit"
```

12. Remote repository
```bash
git remote add origin <URL репозитория>
```


13. Push
```bash
git push -u origin master
```

Rem:
*The core.autocrlf option in the git config command allows you to configure automatic conversion of line endings during Git operations. The following values are possible for this option:

true: Automatically convert line endings during add and commit operations. Git will convert line endings to CRLF (for Windows) during add and commit operations, and then back to LF (for UNIX-like systems) during checkout operations.

false: Do not perform automatic line ending conversion. Files will be saved with the line endings as they were in their original state.

input: Automatically convert line endings during add operations. Git will convert line endings to LF (regardless of the operating system) during add operations, but it will not change line endings during commits or when checking out the source code.

In general, if you are working on Windows, it is recommended to use the value true to have Git automatically convert line endings to CRLF during add and commit operations. This helps ensure compatibility with other tools and platforms that expect the use of CRLF on Windows.

The core.autocrlf option can also be set at the repository level or locally for a specific project using the git config command without the --global flag.*

8. Change LF to CRLF
```bash
$ git config --global core.autocrlf true
```

<!-- 7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   ```bash
   $ flask run
   ``` -->

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).


GLOBAL SETTINGS 
files:
- settinglobal_settings.json
- secrets_file.py
- gs.py

Файл secrets.py находится в Database.kdbx - Базы данных менеджера паролей keypass
