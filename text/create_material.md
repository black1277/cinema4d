# Python для Cinema 4D
## Как создать и применить к объекту материал

Сначала, создадим сферу и поместим её на сцену:
```Python
  sphere = c4d.BaseObject(c4d.Osphere)
  doc.InsertObject(sphere)
```
Создадим базовый материал и дадим ему имя:
```Python
  mat = c4d.Material(c4d.Mbase)
  mat.SetName('red')
```
Другие типы материалов можно найти в [документации][2], (Mbanji,Mfog,Mmaterial,Mterrain и др.)

Установим цвет красный и отключим слой отражений:
```Python
  mat[c4d.MATERIAL_COLOR_COLOR] = c4d.Vector(1,0,0)
  mat[c4d.MATERIAL_USE_REFLECTION] = False
```
Чтобы настроить другие параметры материала сверяйтесь с [документацией][1] Методы объекта `c4d.Material` на странице [документации][4]

Поместим созданный материал в сцену:
```Python
  doc.InsertMaterial(mat)
```
Создадим на сфере тег текстуры и присвоим ему созданный материал:
```Python
  tag = sphere.MakeTag(c4d.Ttexture)
  tag[c4d.TEXTURETAG_MATERIAL] = mat
  c4d.EventAdd() # обновим сцену
```
Другие параметры тега текстуры в [документации][3]

[1]: https://developers.maxon.net/docs/py/23_110/classic_resource/material/mmaterial.html "Classic Resource overview » Material"
[2]: https://developers.maxon.net/docs/py/23_110/types/materials.html "Types and Symbols List » Material Types"
[3]: https://developers.maxon.net/docs/py/23_110/classic_resource/tag/ttexture.html "Classic Resource overview » Material Tag"
[4]: https://developers.maxon.net/docs/py/23_110/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/Material/index.html "c4d.Material"