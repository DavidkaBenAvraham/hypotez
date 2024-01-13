"""! @ru_brief Модуль работы с OpenAI 
@ru_todo было бы неплохо сделать поиск на основе нескльких данных, похожих на характеристики и/или название товара, 
например `мп25, кт316` ии определял категорию и делал пoисковый запрос. Это есть у BING
"""
from src.settings import gs
import openai



def translate (input: str, lang_in: str, lang_out: str, prompt: str = None) -> str:
    """! @ru_brief Функция перевода через openAI
    @ru_todo на реализована. Сморти `openai_translator.py`
    
    """

    openai.api = gs.api_openai
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Translate from English to Russian: Hello, world!",
        temperature=0.5,
        max_tokens=50,
    )

    translation = response.choices[0].text.strip()
    return translation