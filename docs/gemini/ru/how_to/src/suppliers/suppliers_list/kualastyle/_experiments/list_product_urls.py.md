## Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Блок кода представляет собой список URL-адресов страниц с продуктами на сайте Kualastyle.

Шаги выполнения
-------------------------
1. **Определение списка:** Создается список `product_urls` с URL-адресами, которые хранят ссылки на товары.
2. **Заполнение списка:** Список заполняется ссылками на страницы товаров.

Пример использования
-------------------------

```python
from src.suppliers.kualastyle._experiments.list_product_urls import product_urls

# Получение URL-адреса первого товара
first_product_url = product_urls[0]
print(f"Первый товар: {first_product_url}")

# Перебор всех URL-адресов товаров
for url in product_urls:
    print(f"Ссылка на товар: {url}")
```

**Важно:** Данный список URL-адресов является статическим и может быть неактуальным в будущем. Рекомендуется использовать более динамический подход для получения списка URL-адресов товаров, например, парсинг сайта с помощью веб-драйвера.