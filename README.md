# parsing-vessel-database

Проверяет ссылки на наличие судов. Если судов нет или больше одного, то данные не берём.\
Если судно одно, то берёт у него следующие данные: Название, IMO, MMSI и тип, и записывает их в Excel таблицу result.xlsx

## Библиотеки

Установка необходимых библиотек:

	pip install -r requirements.txt

После установки запустите скрипт:

	python main.py
