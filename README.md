# Тестовое задание для StafIT.
## Скрипт для обработки csv-файла
### Запуск
Исходные файлы должны лежать в директории ```csv_files/```.
```bash
python main.py --files dataset1.csv dataset2.csv --report average-gdp
```
### Добавление нового отчёта
- Создать файл в директории ```reports/```, например ```unemployment_changed.py```.
- Зарегистрировать функцию через декоратор:
```bash
from reports.loader import register

@register("unemployment-changed")
def unemployment_changed(rows: list[dict]]) -> list[dict]:
    ...
```
Готово, отчёт можно использовать в скрипте.  
Важно! Подразумевается одинаковое именование названия отчёта и соответствующей функции с разницей только в разделителе: для наименования отчёта "-", для функции "_" (см. пример выше).
### Примеры запуска
Два файла  
![CLI example](screenshots/successful_run_both.png)  
Только первый файл  
![CLI example](screenshots/successful_run_only_1.png)  
Только второй файл  
![CLI example](screenshots/successful_run_only_2.png)  
Без аргументов  
![CLI example](screenshots/unsuccessful_run_without_args.png)  
Неправильное название файла  
![CLI example](screenshots/unsuccessful_run_unknown_file.png)  
Неправильное название отчёта  
![CLI example](screenshots/unsuccessful_run_invalid_report.png)  
