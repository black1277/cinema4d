## Создание точек отката UNDOTYPE

В Cinema 4D Python API, методы `StartUndo`, `AddUndo`, и `EndUndo` используются для создания точек отката (undo points) при изменении документа сцены. Это позволяет пользователям отменять и повторять изменения, сделанные скриптом.

Смотреть в документации [StartUndo][1]

Вот как эти методы и типы можно использовать в скрипте:

### Пример: Изменение позиции объекта с точками отката
```Python
import c4d

def main():
    doc.StartUndo()  # Начало записи отката

    obj = doc.GetActiveObject()  # Получаем активный объект
    if obj is None:
        return

    # Добавляем точку отката для изменения объекта
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

    # Изменяем позицию объекта
    new_position = c4d.Vector(100, 200, 300)
    obj.SetAbsPos(new_position)

    doc.EndUndo()  # Завершаем запись отката
    c4d.EventAdd()  # Обновляем сцену, чтобы изменения были видны

# Вызов основной функции
if __name__ == '__main__':
    main()
```

### Пример: Удаление объекта с точками отката
```Python
import c4d

def main():
    doc.StartUndo()  # Начало записи отката

    obj = doc.GetActiveObject()  # Получаем активный объект
    if obj is None:
        return

    # Добавляем точку отката для удаления объекта
    doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, obj)

    # Удаляем объект
    doc.AddUndo(c4d.UNDOTYPE_DELETE, obj)
    obj.Remove()

    doc.EndUndo()  # Завершаем запись отката
    c4d.EventAdd()  # Обновляем сцену, чтобы изменения были видны

# Вызов основной функции
if __name__ == '__main__':
    main()
```

### Пример: Изменение выбора объекта с точками отката
```Python
import c4d

def main():
    doc.StartUndo()  # Начало записи отката

    # Предполагаем, что у нас есть массив объектов, которые мы хотим выбрать
    objects_to_select = [obj for obj in doc.GetObjects() if obj.GetName() == 'Cube']

    # Изменяем выбор объектов
    for obj in objects_to_select:
        doc.AddUndo(c4d.UNDOTYPE_BITS, obj)  # Точка отката для изменения битов объекта
        obj.SetBit(c4d.BIT_ACTIVE)  # Устанавливаем бит активности

    doc.EndUndo()  # Завершаем запись отката
    c4d.EventAdd()  # Обновляем сцену, чтобы изменения были видны

# Вызов основной функции
if __name__ == '__main__':
    main()

```

### Пример: Изменение иерархии и PSR объекта с точками отката
```Python
import c4d

def main():
    doc.StartUndo()  # Начинаем запись отката

    # Получаем ссылки на объекты
    parent_obj = doc.SearchObject('ParentObject')  # Родительский объект
    child_obj = doc.SearchObject('ChildObject')  # Дочерний объект

    if parent_obj is None or child_obj is None:
        return

    # Добавляем точку отката для изменения иерархии и PSR
    doc.AddUndo(c4d.UNDOTYPE_HIERARCHY_PSR, child_obj)

    # Перемещаем ребенка под нового родителя
    child_obj.InsertUnder(parent_obj)

    # Меняем положение (Position), вращение (Rotation) и масштаб (Scale) ребенка
    child_obj.SetRelPos(c4d.Vector(50, 0, 0))
    child_obj.SetRelScale(c4d.Vector(1.5, 1.5, 1.5))
    rotation = c4d.Vector(0, c4d.utils.Rad(90), 0)
    child_obj.SetRelRot(rotation)

    doc.EndUndo()  # Заканчиваем запись отката
    c4d.EventAdd()  # Обновляем сцену, чтобы отобразить изменения

# Вызов основной функции
if __name__ == '__main__':
    main()

```
Ниже перечислены [типы][2] которые можно использовать для фиксации точек отката:

**UNDOTYPE_CHANGE**  Любое изменение объекта, включая модификации иерархии;  изменение позиционирования (объект был перемещен из A в B), подструктур и т. д. (Необходимо вызвать перед изменением.)

**UNDOTYPE_CHANGE_NOCHILDREN**  То же, что UNDOTYPE_CHANGE, но без дочерних изменений.  (Необходимо вызвать перед изменением.)

**UNDOTYPE_CHANGE_SMALL**  Изменяете только локальные данные (например, контейнер данных), без подструктур (например, без тегов на объекте) и без дочерних элементов.  (Необходимо вызвать перед изменением.)

**UNDOTYPE_CHANGE_SELECTION**  Измените выбор только на точку/полигон/ребро.  (Необходимо вызвать перед изменением.)

**UNDOTYPE_NEWOBJ**  Был создан новый объект/узел/тег и т. д.  (Необходимо вызвать после изменения.)

**UNDOTYPE_DELETEOBJ**  Объект/узел/тег и т. д., подлежащий удалению.  (Необходимо вызвать перед изменением.)

**UNDOTYPE_ACTIVATE**  Автоматически управляется с помощью BaseDocument.SetActiveObject()/SetActiveTag()/SetActiveMaterial() и т. д. Нет необходимости использовать вручную.

**UNDOTYPE_DEACTIVATE**  Автоматически управляется с помощью BaseDocument.SetActiveObject()/SetActiveTag()/SetActiveMaterial() и т. д. Нет необходимости использовать вручную.

**UNDOTYPE_BITS**  Изменение битов объекта, например, статуса выбора.  (Необходимо вызвать перед изменением.)

**UNDOTYPE_HIERARCHY_PSR**  Изменение иерархического размещения и значений PSR.  (Необходимо вызвать перед изменением.)

[1]: https://developers.maxon.net/docs/py/23_110/modules/c4d.documents/BaseDocument/index.html?highlight=startundo#BaseDocument.StartUndo "StartUndo"
[2]: https://developers.maxon.net/docs/py/23_110/consts/UNDOTYPE.html "Types and Symbols List » UNDOTYPE"