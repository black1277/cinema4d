## [c4d.BaseList2D][1]
Каждый экземпляр c4d.BaseList2D имеет ссылку на объект класса c4d.BaseContainer.  По сути, это ассоциативный массив, содержащий все значения параметров, которые объект имеет в Менеджере атрибутов.

В Cinema 4D Python API, `c4d.BaseList2D` является базовым классом для всех объектов, которые могут быть упорядочены в иерархическом списке. Это включает материалы, объекты, теги и др. Этот класс обеспечивает методы для получения и установки бит (выделения, фолдинга и др.), получения и установки пользовательских данных (атрибутов) объекта, работа со слоями, треками и ключами. Далее приведены наиболее важные методы, остальные в [документации][1].

### Получение и установка бит:
- `BaseList2D.DelBit(self, mask)` удалить бит
- `BaseList2D.GetAllBits(self)` получить все биты
- `BaseList2D.GetBit(self, mask)` получить конкретный бит
- `BaseList2D.SetAllBits(self, mask)` установить все биты
- `BaseList2D.SetBit(self, mask)` установить конкретный бит
- `BaseList2D.ToggleBit(self, mask)` переключить бит

### Имя и тип объекта:
- `BaseList2D.GetBubbleHelp(self)` получить всплывающее описание объекта
- `BaseList2D.GetName(self)` получить имя
- `BaseList2D.GetTypeName(self)` Имя категории объекта, например Phong, Spline, Bone
- `BaseList2D.SetName(self, name)` задать имя

### Слои:
- `BaseList2D.GetLayerData(self, doc[, rawdata])` возвращает данные слоя для этого объекта в виде словаря `dict{solo: bool, view: bool, render: bool, manager: bool, locked: bool, generators: bool, expressions: bool, animation: bool, color: Vector, xref: bool}`
- `BaseList2D.GetLayerObject(self, doc)` получить слой этого объекта
- `BaseList2D.SetLayerData(self, doc, data)` устанавливает данные слоя для этого объекта. Параметры в виде словаря `dict{solo: bool, view: bool, render: bool, manager: bool, locked: bool, generators: bool, expressions: bool, animation: bool, color: Vector, xref: bool}`
- `BaseList2D.SetLayerObject(self, layer)` установить слой этого объекта

[Пример кода][2] с созданием слоев
### Шейдеры:
- `BaseList2D.GetFirstShader(self)` получить первый шейдер
- `BaseList2D.InsertShader(self, shader[, pred])` вставить шейдер

### Треки:
- `BaseList2D.FindCTrack(self, id)` найти трек по id
- `BaseList2D.GetCTrackRoot(self)` получить корневой трек
- `BaseList2D.GetCTracks(self)` получить треки
- `BaseList2D.GetFirstCTrack(self)` получить первый трек
- `BaseList2D.InsertTrackSorted(self, track)` вставляет трек и автоматически помещает его в нужное место

### Пользовательские данные (атрибуты):
- `BaseList2D.AddUserData(self, datadescription)` Добавляет контейнер пользовательских данных.
- `BaseList2D.GetUserDataContainer(self)` Получает последовательность контейнеров пользовательских данных.
- `BaseList2D.RemoveUserData(self, id)` Удаляет элемент пользовательских данных.
- `BaseList2D.SetUserDataContainer(self, descid, ...)` Вставляет новые данные пользователя с указанным идентификатором.

### Другое:
- `BaseList2D.GetMain(self)` Переходит на уровень вверх, например, от тега к объекту или от узла Xpresso к тегу, от объекта к документу и т. д.
- `BaseList2D.GetInfo(self)` Возвращает информационные флаги для объекта.  Интерпретация зависит от типа объекта.

## Примеры:
```Python
import c4d

def main():
    # Получить активный документ
    doc = c4d.documents.GetActiveDocument()
    if doc is None:
        return

    # Получить все объекты в документе
    objects = doc.GetObjects()

    # Найти сферу и куб
    sphere = None
    cube = None
    for obj in objects:
        if obj.CheckType(c4d.Opolygon):
            if obj.GetName() == "Сфера":
                sphere = obj
            elif obj.GetName() == "Куб":
                cube = obj

    if sphere is not None and cube is not None:
        # Снять выделение с куба
        cube.DelBit(c4d.BIT_ACTIVE)

        # Установить выделение на сферу
        sphere.SetBit(c4d.BIT_ACTIVE)

        # Обновить окно Cinema 4D
        c4d.EventAdd()

# Вызов основной функции
if __name__=='__main__':
    main()
```

```Python
def AddLongDataType(obj):
    if obj is None: return

    bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_LONG) # Create default container
    bc[c4d.DESC_NAME] = "Test"                        # Rename the entry

    element = obj.AddUserData(bc)     # Add userdata container
    obj[element] = 30                 # Assign a value
    c4d.EventAdd()                    # Update
```

```Python
for id, bc in op.GetUserDataContainer():
    print (id, bc)

obj.RemoveUserData(1)  # все варианты равнозначны
obj.RemoveUserData([c4d.ID_USERDATA, 1])
obj.RemoveUserData(c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA), c4d.DescLevel(1)))

if bl2D.GetInfo() & c4d.OBJECT_MODIFIER:
    print " This bl2D is an object modifier"
```


[1]: https://developers.maxon.net/docs/py/23_110/modules/c4d/C4DAtom/GeListNode/BaseList2D/index.html "c4d » c4d.C4DAtom » c4d.GeListNode » c4d.BaseList2D"
[2]: https://github.com/PluginCafe/cinema4d_py_sdk_extended/blob/master/scripts/04_3d_concepts/scene_elements/scene_management/layer_creates_r13.py "layer_creates"