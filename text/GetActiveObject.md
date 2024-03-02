## [doc.GetActiveObject][1]

Метод `doc.GetActiveObject()` возвращает активный объект в документе. Это тот объект, который выделен в данный момент в Cinema 4D. Вы можете использовать этот метод, чтобы получить ссылку на активный объект и затем изменять его свойства или вызывать методы этого объекта.

Например, если вы хотите изменить положение активного объекта, вы можете сделать это следующим образом:

```python
import c4d
from c4d import documents

def main():
    # Получаем активный документ
    doc = documents.GetActiveDocument()

    # Получаем активный объект в документе
    obj = doc.GetActiveObject()

    # Изменяем положение объекта
    obj.SetRelPos(c4d.Vector(100, 0, 0))

    # Обновляем документ
    c4d.EventAdd()

# Выполняем функцию main
if __name__=='__main__':
    main()
```

В этом примере мы получаем активный объект и устанавливаем его относительное положение в (100, 0, 0)
см. [GetActiveDocument][2] и [GetActiveObject][1]

[1]: https://developers.maxon.net/docs/py/23_110/modules/c4d.documents/BaseDocument/index.html?highlight=getactiveobject#BaseDocument.GetActiveObject "GetActiveObject"
[2]: https://developers.maxon.net/docs/py/23_110/modules/c4d.documents/index.html?highlight=getactivedocument#c4d.documents.GetActiveDocument "GetActiveDocument"