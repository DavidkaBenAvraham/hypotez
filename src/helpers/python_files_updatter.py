import ast
import os

def count_lines_and_functions(file_path):
    """
    @brief Считает количество строк и функций в файле Python.
    
    @param file_path Путь к файлу Python.
    @return Словарь с информацией о файле.
    """
    result = {"file_type": "py", "strings": 0, "functions": 0}
    
    with open(file_path, "r") as file:
        content = file.read()

    # Считаем количество строк
    result["strings"] = content.count('\n') + 1
    
    try:
        # Создаем абстрактное синтаксическое дерево
        tree = ast.parse(content)
        
        # Считаем количество функций
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                result["functions"] += 1
    except SyntaxError:
        # Обработка случаев, когда файл содержит синтаксические ошибки
        result["functions"] = "SyntaxError"
    
    return result

def save_to_json(data, file_path):
    """
    @brief Сохраняет данные в формате JSON в указанный файл.
    
    @param data Данные для сохранения.
    @param file_path Путь к файлу.
    """
    import json
    
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

def add_namespaces_to_files(directory):
    """
    @brief Рекурсивно проходит по коду и добавляет первой строкой в каждый файл 
    аннотации пространств имен в формате Doxygen, если их там нет.
    
    @param directory Каталог, в котором нужно выполнить поиск файлов.
    """
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".py"):
                file_path = os.path.join(root, file_name)
                with open(file_path, "r") as file:
                    content = file.read()

                tree = ast.parse(content)
                namespaces = find_namespaces(tree)
                namespaces_str = "\n".join(namespaces)

                with open(file_path, "r+") as file:
                    file_content = file.read()

                    # Проверка наличия строки в файле
                    if namespaces_str not in file_content:
                        file.seek(0, 0)
                        file.write(f"{namespaces_str}\n{file_content}")

def find_namespaces(node, current_namespace=""):
    """
    @brief Рекурсивно проходит по абстрактному синтаксическому дереву 
    и возвращает список аннотаций пространств имен в формате Doxygen.
    
    @param node Узел абстрактного синтаксического дерева.
    @param current_namespace Текущее пространство имен.
    @return Список аннотаций пространств имен.
    """
    namespaces = []

    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            docstring = ast.get_docstring(item)
            if docstring and docstring.startswith("@namespace"):
                namespaces.append(docstring.strip())

        if isinstance(item, ast.ClassDef):
            class_name = item.name
            new_namespace = f"{current_namespace}.{class_name}" if current_namespace else class_name
            docstring = ast.get_docstring(item)
            if docstring and docstring.startswith("@namespace"):
                namespaces.append(docstring.strip())

            namespaces += find_namespaces(item, new_namespace)

    return namespaces

def find_functions(tree):
    """
    @brief Находит и возвращает список имен функций в абстрактном синтаксическом дереве.
    
    @param tree Абстрактное синтаксическое дерево.
    @return Список имен функций.
    """
    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)
    return functions

def find_classes(tree):
    """
    @brief Находит и возвращает список имен классов в абстрактном синтаксическом дереве.
    
    @param tree Абстрактное синтаксическое дерево.
    @return Список имен классов.
    """
    classes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            classes.append(node.name)
    return classes

def find_variables(tree):
    """
    @brief Находит и возвращает список имен переменных в абстрактном синтаксическом дереве.
    
    @param tree Абстрактное синтаксическое дерево.
    @return Список имен переменных.
    """
    variables = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            variables.append(node.id)
    return variables

def add_comment(node, comment):
    """
    @brief Добавляет комментарий к узлу абстрактного синтаксического дерева.
    
    @param node Узел абстрактного синтаксического дерева.
    @param comment Комментарий для добавления.
    """
    if hasattr(node, 'body') and isinstance(node.body, list) and node.body:
        first_statement = node.body[0]
        if isinstance(first_statement, ast.Expr) and isinstance(first_statement.value, ast.Str):
            # Если узел уже имеет комментарий, добавим новый комментарий на новую строку
            first_statement.value.s += f"\n{comment}"
        else:
            # Если узел не имеет комментария, добавим новый комментарий перед первым выражением
            node.body.insert(0, ast.Expr(value=ast.Str(s=comment)))

def add_function_parameter(node, parameter):
    """
    @brief Добавляет параметр к узлу функции в абстрактном синтаксическом дереве.
    
    @param node Узел функции абстрактного синтаксического дерева.
    @param parameter Параметр для добавления.
    """
    if isinstance(node, ast.FunctionDef):
        node.args.args.append(ast.arg(arg=parameter, annotation=None))

def add_class_attribute(node, attribute):
    """
    @brief Добавляет атрибут к узлу класса в абстрактном синтаксическом дереве.
    
    @param node Узел класса абстрактного синтаксического дерева.
    @param attribute Атрибут для добавления.
    """
    if isinstance(node, ast.ClassDef):
        node.body.append(ast.Assign(targets=[ast.Attribute(value=ast.Name(id='self', ctx=ast.Load()), attr=attribute, ctx=ast.Store())], value=None))

def add_line_to_file_start(file_path, line):
    """
    @brief Добавляет строку в начало файла.
    
    @param file_path Путь к файлу.
    @param line Строка для добавления.
    """
    with open(file_path, "r") as file:
        content = file.read()

    with open(file_path, "w") as file:
        file.write(f"{line}\n{content}")

def process_directory_recursively(directory, function):
    """
    @brief Рекурсивно обрабатывает все файлы в указанном каталоге с помощью заданной функции.
    
    @param directory Каталог для обработки.
    @param function Функция, которая будет применена к каждому файлу.
    """
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            function(file_path)

# Пример использования
def process_python_file(file_path):
    """
    @brief Обрабатывает файл Python: добавляет строку и выводит информацию о функциях, классах и переменных.
    
    @param file_path Путь к файлу Python.
    """
    print(f"Processing file: {file_path}")

    # Добавление строки в начало файла
    add_line_to_file_start(file_path, "# This is a new line added to the beginning of the file")

    # Открытие файла и создание абстрактного синтаксического дерева
    with open(file_path, "r") as file:
        content = file.read()

    tree = ast.parse(content)

    # Примеры вызова функций
    functions_list = find_functions(tree)
    classes_list = find_classes(tree)
    variables_list = find_variables(tree)

    print("Functions:", functions_list)
    print("Classes:", classes_list)
    print("Variables:", variables_list)

    # Пример добавления комментария и параметра к функции
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            add_comment(node, "@brief This is a new comment for the function.")
            add_function_parameter(node, "new_parameter")

    # Пример добавления атрибута к классу
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            add_class_attribute(node, "new_attribute")

    # Запись измененного дерева обратно в файл
    with open(file_path, "w") as file:
        file.write(ast.unparse(tree))

# Процесс обработки всех файлов в указанном каталоге и подкаталогах
process_directory_recursively("/путь/к/вашему/каталогу", process_python_file)

# Пример использования
add_namespaces_to_files("/путь/к/вашему/каталогу")
