
## Как создать и применить к объекту тег
Для создания тега используют метод [MakeTag][1] объекта ```c4d.BaseObject```:
```python
cube = c4d.BaseObject(c4d.Ocube)# куб
# создаем тег фонга для куба
fong = cube.MakeTag(c4d.Tphong)
fong[c4d.PHONGTAG_PHONG_ANGLELIMIT] = True # ограничение угла
fong[c4d.PHONGTAG_PHONG_ANGLE] = c4d.utils.DegToRad(20)# угол 20 градусов
doc.InsertObject(cube)# вставляем куб в документ
c4d.EventAdd() # обновить сцену
```
Аргументом этот метод принимает один и [списка возможных тегов][2]

Так же есть класс тегов, который может хранить несколько элементов с переменным размером данных [c4d.VariableTag][3] Для его создания используется метод [MakeVariableTag][4]:
```python
# op - выделенный полигональный объект
tag = op.MakeVariableTag(c4d.Tvertexmap, op.GetPointCount())
op.InsertTag(tag)
c4d.EventAdd() # обновить сцену
```
Первый аргумент - один из [тегов списка][5], второй аргумент - размер данных (в приведенном примере это количество точек)






[1]: https://developers.maxon.net/docs/py/23_110/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html?highlight=maketag#BaseObject.MakeTag "MakeTag"
[2]: https://developers.maxon.net/docs/py/23_110/types/tags.html "types tags"
[3]: https://developers.maxon.net/docs/py/23_110/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/index.html "VariableTag"
[4]: https://developers.maxon.net/docs/py/23_110/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html?highlight=maketag#BaseObject.MakeVariableTag "MakeVariableTag"
[5]: https://developers.maxon.net/docs/py/23_110/types/tags_variable.html "types tags_variable"