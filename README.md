В репозитории АТ на python для ui и api с использованием
- python
- selenium
- requests
- pytest
- allure
После скачивания репозитория необходимо:
1. Установить пакет зависимостей из файла requirements.txt командой pip install -r requirements.txt
2. т.к. для api тестов использовался анонимный юзернейм, то необходимо проверить что auth_token в файле conftest.py рабочий, в противном случае обновить его
3. для запуска автотестов использовать команду:
   pytest test_ui_cart.py --alluredir=./allure-results
   pytest test_ui_cart.py --alluredir=./allure-results
5. Генерация отчета:
   allure serve allure-results
