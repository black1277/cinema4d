## Навигация по различным объектам сцены
В среде 3D-графики, такой как Cinema 4D, навигация и манипуляция объектами сцены являются основными задачами.
Рассмотрим основные методы работы с объектами сцены в Cinema 4D с использованием Python API.

```doc = documents.GetActiveDocument()``` - получение активного документа. Обычно в скрипте уже доступна глобальная переменая ```doc``` содержащая активный документ.
***
Активный объект — это объект сцены, который в настоящее время выбран пользователем. Для получения активного объекта используется следующий метод:
```python
op = doc.GetActiveObject()
```
Обычно в скрипте уже доступна глобальная переменая ```op``` содержащая активный объект.
Если ничего не выделено или выделено несколько объектов или только тег(-и) - вернет None
***
Получить список выделенных объектов меши, теги, камеры и др.:
```python
objList = doc.GetSelection()
```
 Если ничего не выделено вернет пустой список.
 ***

Сделать объект выделенным можно с помощью такого кода:
```python
doc.SetActiveObject(obj, mode=c4d.SELECTION_NEW) # SELECTION_ADD SELECTION_SUB
```
Причем результат будет зависить от параметра mode (можно сделать объект соло-выделенным или добавить его к уже выделенным, или убрать из выделенных)
***
Получить список объектов выделенных в менеджере объектов:
```python
lst = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_NONE)
# GETACTIVEOBJECTFLAGS_CHILDREN GETACTIVEOBJECTFLAGS_SELECTIONORDER
```
Аргумент отвечает: по умолчанию будут возвращены выделенные объекты верхнего уровня; будут возвращены включая дочерние объекты; объекты будут возвращены согласно порядку их выделения
***
Корневой объект сцены можно получить с помощью метода GetFirstObject(), который возвращает первый объект в иерархии сцены (независимо от того выделен он или нет):
```python
root = doc.GetFirstObject()
```
***
Для поиска объекта по имени в рамках документа используйте метод SearchObject():
```python
findedObj = doc.SearchObject("Null")
```
***
### Обход объектов:
Чтобы найти родительский объект для текущего выбранного объекта, используйте метод GetUp():
```python
parent = obj.GetUp()
```
***
Получение дочерних объектов (список):
```python
children = obj.GetChildren()
```
***
Возвращает последний дочерний элемент этого объекта в списке:
```python
last_child = obj.GetDownLast()
```
***
Получение следующего объекта в иерархии:
```python
next_object = obj.GetNext()
```
***
Получение предыдущего объекта:
```python
prev_object = op.GetPred()
```
***

### Работа с тегами
Теги добавляют дополнительные свойства к объектам. Например, теги могут контролировать рендеринг, материалы, деформации и многое другое.
Возвращает первый тег, связанный с объектом:
```python
tag = obj.GetFirstTag()
```
***
Возвращает последний тег, связанный с объектом:
```python
tag = obj.GetLastTag()
```
***
Получить список всех тегов, связанных с объектом:
```python
tagList = obj.GetTags()
```
***
Вернет список всех выделенных тегов:
```python
tagList = obj.GetActiveTags()
```
***
Получение конкретного типа тега:
```python
tag = obj.GetTag(c4d.Tnormal)
```
***
Скопировать теги объекта в другой объект:
```python
boolResult1 = obj.CopyTagsTo(dest, True, False, False) # скопировать тег фонга
boolResult2 = obj.CopyTagsTo(dest, True, False, True) # скопировать теги материала
boolResult3 = obj.CopyTagsTo(dest, c4d.NOTOK, c4d.NOTOK, c4d.NOTOK) # скопировать все теги
```
visible - видимость, variable - вариативность, hierarchical - иерархичность

### Работа с материалами
Материалы в Cinema 4D определяют визуальные характеристики объектов, такие как цвет, текстура, отражение и прозрачность.
Получение первого материала в документе:
```python
material = doc.GetFirstMaterial()
```
***
Возвращает выделенный (в менеджере материалов) материал:
```python
material = doc.GetActiveMaterial()
```
Если выделено больше одного - вернет None
***
Вернет список выделенных (в менеджере материалов) материалов:
```python
materialList = doc.GetActiveMaterials()
```
***
Поиск материала по имени:
```python
material = doc.SearchMaterial("Matname")
```
***
Вернет список всех материалов в документе:
```python
materialList = doc.GetMaterials()
```
Так же к материалам и тегам можно применять методы GetNext(), GetPred(), GetUp(), GetChildren() для навигации по иерархии.














