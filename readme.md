## Для запуска нужно:
1. git clone https://github.com/aaalis/autotests-python
2. cd autotests-python
3. pip install -r requirements.txt
3. pytest -v --lang=en --reruns 1 --tb=line test_main_page.py
+ lang - язык, может быть ru/en
+ rerun - плагин для повторного запуска тестов при ошибке 