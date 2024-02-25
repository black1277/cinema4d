## Python

### Как создать клонер в Cinema 4D

Чтобы создать любой объект используемый для сцены нужно воспользоваться таким кодом:
```Python
obj = c4d.BaseObject(ID)
```
где ID - представляет из себя номер идендификатора нужного объекта.
Номерам наиболее часто используемых объектов сопоставлены константы:
- Ocube    5159
- Onull    5140
- Oplane   5168
- Osphere  5160

и т.д. Список этих констант можно найти в [документации][1]. Таким образом мы можем создать, например примитив куба, либо написав так:
```Python
cube = c4d.BaseObject(5159)
```
либо так:
```Python
cube = c4d.BaseObject(c4d.Ocube)
```
Однако, в документации перечислены не все возможные объекты. Как раз клонера там и нету... В таком случае, есть обходной путь. В самой Cinema 4D включаем команду "Протокол скрипта" (находится там же где и менеджер скриптов) - теперь каждое действие в редакторе будет сопровождаться отображением примерно такой команды:
```Python
c4d.CallCommand(300000116) # Протокол скрипта...
```
![изображение протокола скрипта](https://github.com/black1277/cinema4d/blob/main/text/img/protokol.jpg)

Создаем клонер на сцене через меню редактора и наблюдаем в протоколе скрипта:
```Python
c4d.CallCommand(1018544) # Клон
```
Вот эта цифра 1018544 и есть нужный нам номер, который позволит создать клонер в коде:
```Python
cloner = c4d.BaseObject(1018544)
```
Далее созданный объект можно поместить в сцену:
```Python
cloner.SetName('сloner') # дадим своё название в менеджере объектов
doc.InsertObject(cloner) # добавили клонер в документ

# Обновляем сцену после добавления новых объектов
c4d.EventAdd()
```
Важное примечание: таким образом можно создавать только объекты помещаемые в сцену. Другие объекты, например слои в менеджере слоев, нужно создавать по другому, хотя сама команда c4d.CallCommand(ID) может быть использована.

Перед тем как добавить клонер на сцену можно настроить параметры клона:
```Python
# тип клонера - линейный
cloner[c4d.ID_MG_MOTIONGENERATOR_MODE]=c4d.ID_MG_MOTIONGENERATOR_MODE_LINEAR
```
где константа c4d.ID_MG_MOTIONGENERATOR_MODE_LINEAR может быть заменена обычным числом 1 . Названия констант можно смотреть в [документации][3] или просто заменять их числами. Так следущее число 2 сделает тип клона радиальным и т.д.

Чтобы узнать как изменить соответствующий атрибут объекта(клонера) нужно найти его в менеджере атрибутов, выделить название атрибута щелчком левой кнопки мыши, а затем перетащить это название в редактор скриптов или консоль. В том месте куда перетащили название атрибута появится в квадратных скобках имя константы через которую надо обратится к соответвующему параметру объекта. К примеру, у линейного клонера есть атрибут количество, перетащив его в редактор увидим название `cloner[c4d.MG_LINEAR_COUNT]` Используем это:
```Python
cloner[c4d.MG_LINEAR_COUNT]=7 # количество клонов будет 7
```
![изображение атрибутов клонера](https://github.com/black1277/cinema4d/blob/main/text/img/kolvo.jpg)

Перед тем как в коде назначать параметрам свои значения полезно заглянуть в [документацию][2], чтобы не ошибиться с типом значения. Или просто распечатать через print:
```Python
print(cloner[c4d.MG_LINEAR_OBJECT_POSITION])
# Распечатает Vector(0, 50, 0)
```
Зададим смещение каждому следующему объекту в линии. Это можно сделать двумя способами. Первый:
```Python
cloner[c4d.MG_LINEAR_OBJECT_POSITION] = c4d.Vector(50, 0, 0)
# задаем сразу три значения по порядку - x,y,z
```
Второй:
```Python
cloner[c4d.MG_LINEAR_OBJECT_POSITION,c4d.VECTOR_X] = 50 # зададим смещение по x
cloner[c4d.MG_LINEAR_OBJECT_POSITION,c4d.VECTOR_Y] = 0 # лучше явно обнулить на случай если
cloner[c4d.MG_LINEAR_OBJECT_POSITION,c4d.VECTOR_Z] = 0 # там было значение по умолчанию
```
Вот полный код скрипта:
```Python
import c4d

def main():
    cube = c4d.BaseObject(c4d.Ocube)
    # устанавливаем стороны для куба по 45
    cube[c4d.PRIM_CUBE_LEN] = c4d.Vector(45.,45., 45.)
    cloner = c4d.BaseObject(1018544)
    cloner.SetName('сloner')
    cloner[c4d.ID_MG_MOTIONGENERATOR_MODE]=1
    cloner[c4d.MG_LINEAR_COUNT]=7
    cloner[c4d.MG_LINEAR_OBJECT_POSITION] = c4d.Vector(50, 0, 0)
    #cloner[c4d.MG_LINEAR_OBJECT_POSITION,c4d.VECTOR_X] = 50
    #cloner[c4d.MG_LINEAR_OBJECT_POSITION,c4d.VECTOR_Y] = 0
    #cloner[c4d.MG_LINEAR_OBJECT_POSITION,c4d.VECTOR_Z] = 0
    cube.InsertUnder(cloner)# подчиняем куб клонеру
    doc.InsertObject(cloner) # добавили клонер
    # Обновляем сцену после добавления новых объектов
    c4d.EventAdd()

if __name__=='__main__':
    main()
```


[1]: https://developers.maxon.net/docs/py/23_110/types/objects.html
[2]: https://developers.maxon.net/docs/py/23_110/classic_resource/object/mglineararray.html
[3]: https://developers.maxon.net/docs/py/23_110/classic_resource/object/obasemogen.html