import c4d
import math

def main():
    # Определяем параметры анимации
    fps = doc.GetFps() # Количество кадров в секунду
    duration = 10 # Продолжительность анимации в секундах
    amplitude = 500 # Амплитуда синусоиды
    frequency = 0.5 # Частота синусоиды
    phase = 0 # Фаза синусоиды

    # Получаем список всех сфер в сцене
    spheres = [obj for obj in doc.GetObjects() if obj.GetType() == c4d.Osphere]

    # Анимируем каждую сферу
    for sphere in spheres:
        # Получаем начальную позицию сферы
        x0 = sphere[c4d.ID_BASEOBJECT_REL_POSITION].x
        y0 = sphere[c4d.ID_BASEOBJECT_REL_POSITION].y
        z0 = sphere[c4d.ID_BASEOBJECT_REL_POSITION].z

        # Создаем новые треки позиции для сферы
        track_x = c4d.CTrack(sphere, c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION, c4d.DTYPE_VECTOR, 0),
                    c4d.DescLevel(c4d.VECTOR_X, c4d.DTYPE_REAL, 0)))
        track_y = c4d.CTrack(sphere, c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION, c4d.DTYPE_VECTOR, 0),
                    c4d.DescLevel(c4d.VECTOR_Y, c4d.DTYPE_REAL, 0)))
        track_z = c4d.CTrack(sphere, c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION, c4d.DTYPE_VECTOR, 0),
                    c4d.DescLevel(c4d.VECTOR_Z, c4d.DTYPE_REAL, 0)))

        sphere.InsertTrackSorted(track_x)
        sphere.InsertTrackSorted(track_y)
        sphere.InsertTrackSorted(track_z)

        # Создаем новые кривые для треков
        curve_x = track_x.GetCurve()
        curve_y = track_y.GetCurve()
        curve_z = track_z.GetCurve()

        # Добавляем ключевые кадры для кривых
        for t in range(duration * fps + 1):
            # Вычисляем новую позицию сферы по синусоидальной формуле
            x = x0
            y = y0 + amplitude * math.sin(2 * math.pi * frequency * t / fps + phase)
            z = z0

            # Создаем новые ключевые кадры
            key_x = c4d.CKey()
            key_y = c4d.CKey()
            key_z = c4d.CKey()

            key_x.SetTime(curve_x, c4d.BaseTime(t, fps))
            key_y.SetTime(curve_y, c4d.BaseTime(t, fps))
            key_z.SetTime(curve_z, c4d.BaseTime(t, fps))

            key_x.SetValue(curve_x, x)
            key_y.SetValue(curve_y, y)
            key_z.SetValue(curve_z, z)

            # Добавляем ключевые кадры в кривые
            curve_x.InsertKey(key_x)
            curve_y.InsertKey(key_y)
            curve_z.InsertKey(key_z)

    # Обновляем сцену
    c4d.EventAdd()

# Execute main()
if __name__=='__main__':
    main()
