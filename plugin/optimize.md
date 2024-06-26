## Оптимизация кеша для Object Data Plugin
При каждом вызове метода Python должен управлять множеством вещей, чтобы метод можно было исполнить.
Метод ```ObjectData.GetVirtualObjects()``` вызывается при каждом выполнении сцены (один или несколько раз за кадр).
Вызванный однажды метод ```ObjectData.GetVirtualObjects()``` возвращает каждый раз кеш установленный в объекте.
Обычно для оптимизации вместо повторной генерации всего при каждом выполнении сцены рекомендуется вернуть ранее возвращенный объект: тот, который присутствует в кеше.
Пример реализации такого GetVirtualObjects:
```python
def GetVirtualObjects(self, op, hh):

    # dirty = True если кэш изменен или данные (любые параметры) объекта изменились.
    dirty = op.CheckCache(hh) or op.IsDirty(c4d.DIRTY_DATA)

    # Если ничего не изменилось и кеш присутствует, верните кеш
    if not dirty:
        return op.GetCache(hh)

    # создаем куб
    return c4d.BaseObject(c4d.Ocube)
```
Это обычный способ возврата кэшированного объекта, поэтому Cinema 4D и Python не нужно создавать весь объект при каждом выполнении сцены.
Это экономит много времени. Но как было написано ранее, просто вызов метода требует некоторого времени, поскольку Python должен зарегистрировать этот вызов во внутренней системе управления.

В качестве обходного пути предыдущей проблемы можно вызвать ```self.SetOptimizeCache(True)```, чтобы вернуть кеш вашего уже созданного объекта на уровне, который намного ближе к внутренней системе, чем Python.
Внутри он будет выполнять тот же код, что и предыдущий код, но на C++.
Это означает, что если кеш доступен и параметры не изменены, он вернет ранее сохраненный объект в кеше без необходимости вызывать и готовить какие-либо элементы Python, поскольку все будет обрабатываться на C++.
Внутренний тест с использованием первого кода Python дает около 89 кадров в секунду, а использование ```SetOptimizeCache``` дает около 278 кадров в секунду.


Примечание ```self.SetOptimizeCache``` необходимо вызывать из метода ```__init__``` вашего класса, поскольку он проверяется сразу после него.

Пример реализации такого GetVirtualObjects:
```python
class CacheTest(plugins.ObjectData):
"""CacheTest Generator"""

    def __init__(self):
        self.SetOptimizeCache(True)

    def GetVirtualObjects(self, op, hh):
        """
        Поскольку SetOptimizeCache имеет значение True в методах __init__, следующие строки больше не нужны.
        Внутренние проверки по-прежнему будут выполняться, но на C++, а не на Python, что приведет к увеличению производительности.

        dirty = op.CheckCache(hh) or op.IsDirty(c4d.DIRTY_DATA)

        if not dirty:
            return op.GetCache(hh)
        """

        # Creates a cube
        return c4d.BaseObject(c4d.Ocube)
```
[Оригинальная документация][1]

[1]: https://developers.maxon.net/docs/py/23_110/manuals/plugins/object_data.html