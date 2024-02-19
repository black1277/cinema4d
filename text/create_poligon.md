## Python

### Как создать полигон в Cinema 4D
https://developers.maxon.net/docs/Cinema4DPythonSDK/html/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.html

Создаем новый полигон с тремя точками

```Python
    polygon = c4d.PolygonObject(3, 1)
```

Устанавливаем координаты точек полигона

```Python
    points = polygon.GetAllPoints()
    points[0] = c4d.Vector(0, 0, 0)
    points[1] = c4d.Vector(20, 0, 0)
    points[2] = c4d.Vector(0, 25, 0)
    polygon.SetAllPoints(points)
```

какие точки надо соединить
от последовательности зависит куда направлена нормаль

```Python
    poly = c4d.CPolygon(0, 1, 2)
    polygon.SetPolygon(0, poly)
```

обновить
```Python
  polygon.Message(c4d.MSG_UPDATE)
```