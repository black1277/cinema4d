Немного про совместимость версий при переходе со 2 на 3 Python

Самые частые ошибки которые мне попадались:
1. во 2-й версии был оператор `xrange` -> в 3-й версии `range`
2. 2-я версия - `print` вызывался без скобок для аргументов -> 3 - скобки обязательны
3. итератор `c4d.__dict__.iteritems()` был заменен на `c4d.__dict__.items()`
4. тип 'long' заменен на тип 'int'
5. в 3 Python убрали Exception Message: вместо `exception.message` -> `exception.args[0]`
***
Подробнее, смотрим в [документации по миграции][1]


[1]: https://developers.maxon.net/docs/py/23_110/manuals/misc/python3_migration.html "python3_migration"