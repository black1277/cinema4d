import c4d
import random

def main():
    # Определяем границы, внутри которых будут создаваться сферы
    x_min, x_max = -1000, 1000
    y_min, y_max = -1000, 1000
    z_min, z_max = -1000, 1000

    # Количество сфер для создания
    num_spheres = 10

    # Создаем каждую сферу
    for _ in range(num_spheres):
        # Генерируем случайные координаты для сферы
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        z = random.uniform(z_min, z_max)

        # Создаем новую сферу
        sphere = c4d.BaseObject(c4d.Osphere)

        # Устанавливаем радиус и позицию сферы
        sphere[c4d.PRIM_SPHERE_RAD] = random.uniform(50, 200) # Радиус сферы
        sphere[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(x, y, z)

        # Добавляем сферу в сцену
        doc.InsertObject(sphere)

    # Обновляем сцену
    c4d.EventAdd()

# Execute main()
if __name__=='__main__':
    main()
