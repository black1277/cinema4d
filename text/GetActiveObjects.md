## [doc.GetActiveObjects][1]

Метод `doc.GetActiveObjects()` возвращает список активных объектов. Аргументом принимает один из флагов:
- ```GETACTIVEOBJECTFLAGS_NONE``` (Добавляется только самый верхний родительский элемент каждой цепочки)
- ```GETACTIVEOBJECTFLAGS_CHILDREN```(Дочерние объекты также добавляются в выделение, если они выбраны)
- ```GETACTIVEOBJECTFLAGS_SELECTIONORDER``` (Массив выбора сортируется в порядке выбора, например, первый выбранный объект является первым элементом массива)

Например, если вы хотите изменить положение активного объекта, вы можете сделать это следующим образом:

```python
import c4d
from c4d import documents

def main():
    # Получаем активный документ
    doc = documents.GetActiveDocument()

    # Получаем активный объект в документе
    obj = doc.GetActiveObjects()[0]

    # Изменяем положение объекта
    obj.SetRelPos(c4d.Vector(100, 0, 0))

    # Обновляем документ
    c4d.EventAdd()

# Выполняем функцию main
if __name__=='__main__':
    main()
```

В этом примере мы получаем первый активный объект и устанавливаем его относительное положение в (100, 0, 0)
см. [GetActiveDocument][2] и [GetActiveObjects][1]

[1]: https://developers.maxon.net/docs/py/23_110/modules/c4d.documents/BaseDocument/index.html?highlight=getactiveobject#BaseDocument.GetActiveObjects "GetActiveObjects"
[2]: https://developers.maxon.net/docs/py/23_110/modules/c4d.documents/index.html?highlight=getactivedocument#c4d.documents.GetActiveDocument "GetActiveDocument"