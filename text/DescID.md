## [c4d.DescID][1]


`c4d.DescID` в Cinema 4D Python API используется для идентификации параметров объекта. Он состоит из одного или нескольких уровней, каждый из которых представлен `c4d.DescLevel`. Каждый уровень идентифицирует определенный параметр или подпараметр объекта.

Конструктор `c4d.DescID` принимает один или несколько объектов `c4d.DescLevel` в качестве аргументов. Каждый объект `c4d.DescLevel` создается с идентификатором параметра и, возможно, типом данных и группой.

Вот пример использования `c4d.DescID` для идентификации пользовательских данных:

```python
# Создаем DescLevel для пользовательских данных
level1 = c4d.DescLevel(c4d.ID_USERDATA, c4d.DTYPE_SUBCONTAINER, 0)

# Создаем DescLevel для конкретных пользовательских данных
level2 = c4d.DescLevel(1, c4d.DTYPE_LONG, 0)

# Создаем DescID
desc_id = c4d.DescID(level1, level2)
```

В этом примере мы создаем `c4d.DescID`, который идентифицирует первые пользовательские данные типа Long. Обратите внимание, что `c4d.ID_USERDATA` используется для идентификации пользовательских данных, `c4d.DTYPE_SUBCONTAINER` указывает, что это контейнер для других параметров, и `c4d.DTYPE_LONG` указывает, что параметр является целым числом.

Вы можете использовать `c4d.DescID` для доступа к параметрам объекта с помощью метода `__getitem__()` или `__setitem__()` объекта. Например, если у вас есть объект `obj` и `desc_id`, как определено выше, вы можете получить или установить значение пользовательских данных следующим образом:

```python
# Получить значение пользовательских данных
value = obj[desc_id]

# Установить значение пользовательских данных
obj[desc_id] = 10
```

Обратите внимание, что `c4d.DescID` и `c4d.DescLevel` являются частью системы описаний Cinema 4D, которая используется для идентификации и работы с параметрами объекта. Это включает в себя встроенные параметры, такие как положение и вращение объекта, а также пользовательские данные и параметры, определенные плагинами

Есть пример кода от разработчиков в котором хорошо объясняется какие параметры принимает объект c4d.DescID и их значение:

```python
import c4d

def main():

    if not isinstance(op, c4d.BaseObject):
        raise RuntimeError("Please select an object.")

    # --- Доступ к элементу описания ---

    # Самая простая форма указания положения объекта.
    # Константа(символ) это просто (целое) число.
    print (c4d.ID_BASEOBJECT_REL_POSITION) # выведет число 903

    # Мы можем прочитать параметр узла в Python с помощью синтаксиса скобок.
    # Передавая число или символ.
    print (op[903])
    print (op[c4d.ID_BASEOBJECT_REL_POSITION])

    # Мы также могли бы использовать другие интерфейсы доступа, такие как C4DAtom.Get/SetParameter или BaseContainer,
    # но я собираюсь их здесь игнорировать.

    # Однако мы также можем обернуть это число в DescID следующим образом.
    descId = c4d.DescID(c4d.ID_BASEOBJECT_REL_POSITION)
    # будет делать то же самое, что и предыдущий вызов
    # op[c4d.ID_BASEOBJECT_REL_POSITION]
    print (op[descId])

    # DescID формально создаются из DescLevels, то, что мы сделали выше,
    # было всего лишь сокращением для этого.  DescLevel просто оборачивает число.
    # Итак, мы можем указать c4d.DescID(c4d.ID_BASEOBJECT_REL_POSITION) также следующим образом.
    descLevel = c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION)
    descId = c4d.DescID(descLevel)
    print (op[descId])

    # Однако DescLevels может передавать больше информации, чем просто идентификатор,
    # они также могут хранить тип данных и создателя этого идентификатора.
    # Позиция является вектором, поэтому мы можем это указать.
    # 0 в конце означает отсутствие создателя
    descLevel = c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION,
                              c4d.DTYPE_VECTOR, 0)
    descId = c4d.DescID(descLevel)
    print (op[descId])

    # Итак, подведем итог: эти пять идентификаторов более или менее эквивалентны,
    # они, по крайней мере, будут возвращать одно и то же значение параметра.
    #
    #   903
    #   c4d.ID_BASEOBJECT_REL_POSITION
    #   c4d.DescID(c4d.ID_BASEOBJECT_REL_POSITION)
    #   c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION))
    #   c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION,
    #                            c4d.DTYPE_VECTOR, 0))

    # --- Доступ к компоненту элемента описания ---

    # До сих пор мы имели доступ только к вектору в целом.
    # Но есть некоторые типы данных, которые состоят из подкомпонентов,
    # например BaseContainer или Vector.  Вот почему DescID может состоять из трех идентификаторов,
    # где каждый уровень (DescLevel) дополнительно определяет,
    # к какой части параметра мы хотим получить доступ.

    print (c4d.VECTOR_X) # выведет 1000

    # Чтобы получить доступ к компоненту X вектора положения, мы можем сделать это
    print (op[903, 1000])
    print (op[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X])

    # Как и раньше, это можно сделать более подробно с помощью DescID

    # a.
    dLvlVector = c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION)
    dLvlVectorX = c4d.DescLevel(c4d.VECTOR_X)
    descId = c4d.DescID(dLvlVector, dLvlVectorX)
    print (op[descId])

    # b.
    dLvlVector = c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION,
                               c4d.DTYPE_VECTOR, 0)
    dLvlVectorX = c4d.DescLevel(c4d.VECTOR_X,
                                c4d.DTYPE_REAL, 0)
    descId = c4d.DescID(dLvlVector, dLvlVectorX)
    print (op[descId])

    # Используя числа вместо констант код выглядит короче но менее понятен:
    #
    #   descId = c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA, 5, 0),
    #                       c4d.DescLevel(1, 1, 0))
    #
    # более многословная форма была бы такой::
    #
    #   descId = c4d.DescID(
    #       c4d.DescLevel(c4d.ID_USERDATA, c4d.DTYPE_SUBCONTAINER, 0),
    #       c4d.DescLevel(1, c4d.DTYPE_GROUP, 0))
    #
    # Это просто сложный способ выражения (700, 1) или в символической
    # форме (c4d.ID_USERDATA, 1).  Это просто означает первый элемент
    # в контейнере пользовательских данных.  Однако в некоторых местах,
    # например в описаниях или узлах xpresso, Cinema требуется эта очень
    # подробная форма, поскольку все остальные являются просто сокращенной
    # формой для удобства пользователя.

if __name__ == '__main__':
    main()
```

[1]: https://developers.maxon.net/docs/py/23_110/modules/c4d/DescID/index.html "c4d.DescID"