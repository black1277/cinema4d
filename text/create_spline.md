
## Как создать [сплайн][1]

Создаем сплайн-примитив (круглый)

```Python
circle = c4d.BaseObject(c4d.Osplinecircle)
```
А так же [Osplinearc, Osplinestar, Osplineflower, Osplineformula][2] и др.


либо создаем пользовательский сплайн, первый аргумент - количество точек

```Python
spline = c4d.SplineObject(2, c4d.SPLINETYPE_LINEAR)
```
типы точек: [SPLINETYPE_LINEAR, SPLINETYPE_CUBIC, SPLINETYPE_AKIMA, SPLINETYPE_BSPLINE][3].

Если нужно задать количество сегментов или изменить количество точек:

```Python
spline.ResizeObject(8,2)
```
первый аргумент количество точек, второй сегментов


Задаем количество точек в сегменте
```Python
spline.SetSegment(0, 4, True)
```

Задаем точки
```Python
spline.SetPoint(0, c4d.Vector(-100, -100, -100))
spline.SetPoint(1, c4d.Vector(100, -100, -100))
spline.SetPoint(2, c4d.Vector(100, 100, -100))
spline.SetPoint(3, c4d.Vector(-100, 100, -100))
```

Вставляем в документ и обновляем
```Python
doc.InsertObject(spline)
c4d.EventAdd()
```
У SPLINETYPE_LINEAR и SPLINETYPE_BSPLINE нет ручек для настройки кривых (тангенсов)

[1]: https://developers.maxon.net/docs/py/23_110/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/SplineObject/index.html "SplineObject"
[2]: https://developers.maxon.net/docs/py/23_110/types/objects.html "objects"
[3]: https://developers.maxon.net/docs/py/23_110/types/spline.html "spline types"