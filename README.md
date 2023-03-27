# demo_qa
Python 3.10.6

## Локальный запуск:

1. Клонировать репозиторий

   `git clone 'https://github.com/Andrewkv11/demo_qa.git'`

2. Создать вирутальное окружение и установить зависимости

3. Запустить тесты командной 
 
   `python -m pytest --alluredir=test_results`
   
4. Посмотреть сгенерированный отчет 

    `allure serve ./test_results`
