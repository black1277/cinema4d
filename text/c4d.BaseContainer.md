## [c4d.BaseContainer][1]

Контейнер — это коллекция отдельных значений. Каждое значение имеет свой идентификатор и тип.  Контейнер также может содержать любое количество дочерних контейнеров. Нет никакой гарантии, что значение находится в контейнере. По возможности используйте значения по умолчанию при доступе к значениям.

После того как вы установили значение контейнера с использованием одного типа, вы не должны ни пытаться получить к нему доступ с использованием другого типа, ни перезаписывать его значением другого типа!

Оригинал или копию контейнера можно получить из объекта [c4d.BaseList2D][2] с помощью методов BaseList2D.GetDataInstance(self) и BaseList2D.GetData(self) соответсвенно:
```python
import c4d

def main():
    shader = c4d.BaseShader(c4d.Xfusion)

    bc = shader.GetDataInstance() // оригинал контейнера
    bc.SetInt32(c4d.SLA_FUSION_MODE,c4d.SLA_FUSION_MODE_NORMAL)
    bc.SetFloat(c4d.SLA_FUSION_BLEND,0.1)
    bc.SetBool(c4d.SLA_FUSION_USE_MASK,True)
    bc.SetBool(c4d.SLA_FUSION_INVERT_MASK,True)
    bc.SetBool(c4d.SLA_FUSION_INVERT_OUTPUT,True)

if __name__=='__main__':
    main()
```
Следующие методы иллюстрируют какие типы данных могут быть получены из контейнера:
`BaseContainer.GetData(self, id)` Возвращает данные элемента по идентификатору.

`BaseContainer.GetDataPointer(self, id)` Получает указатель для прямого доступа к данным.

`BaseContainer.GetBool(self, id[, preset])` Возвращает логическое значение с указанным идентификатором или заданное значение, если оно не существует.

`BaseContainer.GetInt32(self, id[, preset])`  .. целое ..

`BaseContainer.GetInt64(self, id[, preset])`  .. целое ..

`BaseContainer.GetFloat(self, id[, preset])`  .. десятичное ..

`BaseContainer.GetVector(self, id[, preset])`  .. вектор ..

`BaseContainer.GetMatrix(self, id[, preset])`  .. матрицу ..

`BaseContainer.GetString(self, id[, preset])`  .. строковое ..

`BaseContainer.GetFilename(self, id[, preset])`  .. строковое (путь к файлу) ..

`BaseContainer.GetUuid(self, id, preset)`  .. UUID ..

`BaseContainer.GetTime(self, id[, preset])`  .. c4d.BaseTime ..

`BaseContainer.GetContainer(self, id)` Возвращает копию подконтейнера с указанным идентификатором или пустой контейнер, если он не существует.

`BaseContainer.GetContainerInstance(self, id)` живой подконтейнер или пустой контейнер, если он не существует

`BaseContainer.GetLink(self, id[, doc, ...])` возвращает связанный объект (c4d.BaseList2D)

`BaseContainer.GetObjectLink(self, id[, doc])` возвращает связанный объект (c4d.BaseObject)

`BaseContainer.GetMaterialLink(self, id[, doc])` возвращает связанный материал

`BaseContainer.GetCustomDataType(self, id)` Возвращает копию пользовательского типа данных или None, если не существует.

Помимо методов получения свойств, существуют аналогичные методы для установки свойств, например:

`BaseContainer.SetBool(self, id, b)` устанавливает логическое свойство

Примеры кода:
```python
import c4d

bc = c4d.BaseContainer() # создаем пустой контейнер
bc[1000] = "hello" # заполняем данными
bc[2000] = "world"

# выведем текушее содержимое
print ("Original:")
for dataid, data in bc:
    print (dataid, data)
# 1000 hello
# 2000 world

dataptr = bc.GetDataPointer(1000) # получим указатель
bc.InsDataAfter(3000, "beautiful", dataptr) # добавим новые данные после указателя

# выведем новое содержимое
print ("Changed:")
for dataid, data in bc:
    print (dataid, data)
# 1000 hello
# 3000 beautiful
# 2000 world
```



[1]: https://developers.maxon.net/docs/py/23_110/modules/c4d/BaseContainer/index.html "documentation » c4d » c4d.BaseContainer"
[2]: https://developers.maxon.net/docs/py/23_110/modules/c4d/C4DAtom/GeListNode/BaseList2D/index.html "c4d » c4d.C4DAtom » c4d.GeListNode » c4d.BaseList2D"
