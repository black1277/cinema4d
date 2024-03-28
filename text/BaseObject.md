## [c4d.BaseObject][1]

- `BaseObject.GetAbsPos(self)` Возвращает абсолютное положение объекта. Это будут абсолютные локальные координаты внутри родительского объекта.
- `BaseObject.GetAbsScale(self)` Возвращает абсолютный масштаб объекта. Они будут относиться к родительскому объекту, если он у него есть
- `BaseObject.GetAbsRot(self)` Возвращает абсолютное вращение HPB объекта относительно любого родительского

- `BaseObject.GetRelPos(self)` Возвращает относительное положение объекта.
- `BaseObject.GetRelScale(self)` Возвращает относительный масштаб объекта.
- `BaseObject.GetRelRot(self)` Возвращает относительное вращение объекта.

- `BaseObject.GetFrozenPos(self)` Возвращает замороженное положение объекта.
- `BaseObject.GetFrozenScale(self)` Возвращает замороженный масштаб объекта.
- `BaseObject.GetFrozenRot(self)` Возвращает замороженное вращение HPB объекта.

Эти методы возвращают тип - `Vector(0, 0, 0)`
***
- `BaseObject.GetMl(self)` Получите локальную матрицу, которая представляет положение, масштаб и вращение объектов.
- `BaseObject.GetMg(self)` Получите мировую (глобальную) матрицу, которая представляет положение, масштаб и вращение объектов.
- `BaseObject.GetMln(self)` Получите локальную нормализованную матрицу, которая представляет положение, масштаб и вращение объектов.
- `BaseObject.GetMgn(self)` Получите глобальную нормализованную матрицу, которая представляет положение, масштаб и вращение объектов.
- `BaseObject.GetUpMg(self)` Получите глобальную матрицу родительского объекта, которая представляет положение, масштаб и вращение объектов. Если у объекта нет родительского объекта, то эта матрица будет единичной матрицей.

Эти методы возвращают тип - `Matrix(v1: (1, 0, 0); v2: (0, 1, 0); v3: (0, 0, 1); off: (0, 0, 0))`
***

- `BaseObject.GetMp(self)` Центр ограничивающей рамки (вектор) в локальном пространстве.
- `BaseObject.GetRad(self)` Это радиус ограничивающей рамки (x/y/z) объекта. Он работает для всех объектов и выполняется быстрее, чем поиск границ даже полигональных объектов вручную, радиус кэшируется внутри.



- `BaseObject.GetFirstTag(self)` возвращает первый тег на объекте
- `BaseObject.GetLastTag(self)` возвращает последний тег на объекте
- `BaseObject.GetTags(self)` возвращает все теги объекта
- `BaseObject.GetTag(self, type, nr=0)` возвращает тег определенного типа. type -Ttexture,Texpresso,Tphong,Tpython,Tpolygonselection... nr- Начальный индекс тега для поиска этого типа
- `BaseObject.KillTag(self, type, nr=0)` удаляет тег определенного типа



Примеры кода:
```python
import c4d

def tag_operations(obj):
    # Получение и вывод всех тегов объекта
    tags = obj.GetTags()
    print(f"Теги объекта: {', '.join([tag.GetName() for tag in tags])}")

    # Добавление нового тега Phong к объекту
    phong_tag = c4d.BaseTag(c4d.Tphong)
    obj.InsertTag(phong_tag)
    print("Добавлен тег Phong.")

    # Удаление всех тегов Phong у объекта
    while obj.GetTag(c4d.Tphong):
        obj.KillTag(c4d.Tphong)
    print("Все теги Phong удалены.")

def object_transformations(obj):
    # Вывод абсолютных координат объекта
    abs_pos = obj.GetAbsPos()
    abs_scale = obj.GetAbsScale()
    abs_rot = obj.GetAbsRot()
    print(f"Абсолютное положение: {abs_pos}")
    print(f"Абсолютный масштаб: {abs_scale}")
    print(f"Абсолютное вращение: {abs_rot}")

    # Вывод относительных координат объекта
    rel_pos = obj.GetRelPos()
    rel_scale = obj.GetRelScale()
    rel_rot = obj.GetRelRot()
    print(f"Относительное положение: {rel_pos}")
    print(f"Относительный масштаб: {rel_scale}")
    print(f"Относительное вращение: {rel_rot}")

    # Вывод замороженных координат объекта
    frozen_pos = obj.GetFrozenPos()
    frozen_scale = obj.GetFrozenScale()
    frozen_rot = obj.GetFrozenRot()
    print(f"Замороженное положение: {frozen_pos}")
    print(f"Замороженный масштаб: {frozen_scale}")
    print(f"Замороженное вращение: {frozen_rot}")

    # Вывод матриц объекта
    local_matrix = obj.GetMl()
    global_matrix = obj.GetMg()
    print(f"Локальная матрица: {local_matrix}")
    print(f"Глобальная матрица: {global_matrix}")

# Основная функция
def main():
    # Получаем активный объект
    active_obj = doc.GetActiveObject()
    if active_obj is None:
        print("Нет активного объекта.")
        return

    object_transformations(active_obj)
    tag_operations(active_obj)
    c4d.EventAdd()

# Вызов основной функции
if __name__=="__main__":
    main()
```




[1]: https://developers.maxon.net/docs/py/23_110/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html "c4d » c4d.C4DAtom » c4d.GeListNode » c4d.BaseList2D » c4d.BaseObject"
