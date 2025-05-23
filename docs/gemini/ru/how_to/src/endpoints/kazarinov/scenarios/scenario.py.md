## Как использовать этот блок кода
=========================================================================================

### Описание
-------------------------

Этот блок кода представляет собой сценарий сбора информации о товарах, 
обработки их с помощью ИИ и генерации отчетов в различных языковых версиях.
Он включает в себя следующие этапы:
 - Сбор товаров
 - Обработка товаров с помощью ИИ
 - Генерация отчетов

### Шаги выполнения
-------------------------

1. **Сбор товаров:** 
    - Извлекает список URL товаров.
    - Создает грабер (Graber) для каждого URL, используя функцию `get_graber_by_supplier_url`.
    - Использует грабер для извлечения полей товара (ProductFields) с помощью `graber.grab_page_async`.
    - Конвертирует данные о товарах в нужный формат с помощью `convert_product_fields`.
    - Сохраняет полученные данные с помощью `save_product_data`. 
    - Добавдяет данные в список `products_list`.
2. **Обработка товаров с помощью ИИ:**
    - Проходит по списку языков (`langs_list`).
    - Для каждого языка отправляет список товаров в модель (`gemini`) с помощью `process_llm_async`.
    - Извлекает обработанные данные от модели.
3. **Генерация отчетов:**
    - Создает отчет для каждого языка с помощью `ReportGenerator`.
    - Записывает обработанные данные в json-файлы с помощью `j_dumps`.

### Пример использования
-------------------------

```python
    urls_list:list[str] = [
        'https://www.morlevi.co.il/product/21039',
        'https://www.morlevi.co.il/product/21018',
        'https://www.ivory.co.il/catalog.php?id=85473',
        'https://grandadvance.co.il/eng/?go=products&action=view&ties_ids=801&product_id=28457--SAMSUNG-SSD-1TB-990-EVO-PCle-4.0-x4--5.0-x2-NVMe',
        'https://www.ivory.co.il/catalog.php?id=85473',
        'https://www.morlevi.co.il/product/21018'
    ]

    s = Scenario(window_mode = 'normal')
    asyncio.run(s.run_scenario_async(urls = urls_list, mexiron_name = 'test price quotation', ))
```

Этот код запускает сценарий с использованием списка URL товаров, 
заданным в `urls_list`.
В `mexiron_name` задается имя для отчета.