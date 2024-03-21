# Welcome to the world of Python
# Author: black1277
# https://github.com/black1277/cinema4d/blob/main/scripts/multiGradient.py


import c4d

def main():
    # Создаем новый материал и шейдер градиента
    material = c4d.BaseMaterial(c4d.Mmaterial)
    shader = c4d.BaseShader(c4d.Xgradient)

    # Получаем копию данных c4d.Gradient, на которые ссылается шейдер градиента,
    # и копию данных узла, хранящихся в c4d.Gradient.
    # Данные узла выражаются в виде c4d.BaseCoontainer.
    gradient = shader[c4d.SLA_GRADIENT_GRADIENT]
    # добавим новый узел цвета (третий)
    gradient.InsertKnot(index = 2)
    # получим контейнер содержащий контейнеры всех узлов
    knotData = gradient.GetData(c4d.GRADIENT_KNOT)

    # print(len(knotData))# изначально 2 узла, но теперь 3

    # Переберем все узлы в контейнере данных узлов и установим для них интерполяцию.
    # Каждый узел в контейнере данных узла сам по себе является c4d.BaseContainer, хранящий данные для одного узла.
    for _, knot in knotData:
        knot[c4d.GRADIENTKNOT_INTERPOLATION] = c4d.GRADIENT_INTERPOLATION_NONE
        knot[c4d.GRADIENTKNOT_BIAS] = .65 # отклонение регулятора 65% от 0 до 100%
    #c4d.GRADIENT_INTERPOLATION_CUBICKNOT 0
    #c4d.GRADIENT_INTERPOLATION_SMOOTHKNOT 2
    #c4d.GRADIENT_INTERPOLATION_LINEARKNOT 3
    #c4d.GRADIENT_INTERPOLATION_NONE 5
    #c4d.GRADIENT_INTERPOLATION_EXP_UP 6
    #c4d.GRADIENT_INTERPOLATION_EXP_DOWN 7
    #c4d.GRADIENT_INTERPOLATION_BLEND 8

    gradColors = [ # список содержащий положение и цвет узлов градиента
        [0.0, c4d.Vector(1, 0, 0)],
        [0.33, c4d.Vector(0, 0, 1)],
        [0.66, c4d.Vector(1, 1, 1)]
    ]

    for i, dt in enumerate(gradColors):
        knot = knotData.GetIndexData(i) # получили данные одного узла
        knot[c4d.GRADIENTKNOT_POSITION] = dt[0] # установили позицию
        knot[c4d.GRADIENTKNOT_COLOR] = dt[1] # и цвет
        knotData.SetIndexData(i, knot) # записали измененные данные в узел

    # сохраним контейнер с узлами в градиент
    gradient.SetData(c4d.GRADIENT_KNOT, knotData)
    # а градиент в шейдер
    shader[c4d.SLA_GRADIENT_GRADIENT] = gradient
    # изменим тип градиента на вертикальный
    shader[c4d.SLA_GRADIENT_TYPE] = c4d.SLA_GRADIENT_TYPE_2D_V # 2001
    #c4d.SLA_GRADIENT_TYPE_2D_U              = 2000,
    #c4d.SLA_GRADIENT_TYPE_2D_V,
    #c4d.SLA_GRADIENT_TYPE_2D_DIAG,
    #c4d.SLA_GRADIENT_TYPE_2D_RAD,
    #c4d.SLA_GRADIENT_TYPE_2D_CIRC,
    #c4d.SLA_GRADIENT_TYPE_2D_BOX,
    #c4d.SLA_GRADIENT_TYPE_2D_STAR,
    #c4d.SLA_GRADIENT_TYPE_2D_FOUR_CORNER,
    #c4d.SLA_GRADIENT_TYPE_3D_LINEAR,
    #c4d.SLA_GRADIENT_TYPE_3D_CYLINDRICAL,
    #c4d.SLA_GRADIENT_TYPE_3D_SPHERICAL,  = 2010
    shader[c4d.SLA_GRADIENT_CYCLE] = False
    shader[c4d.SLA_GRADIENT_TURBULENCE] = 0.25 # до 100%
    shader[c4d.SLA_GRADIENT_OCTAVES] = 5.2 # до 10
    shader[c4d.SLA_GRADIENT_SCALE] = 0.1 # 10% без ограничений
    shader[c4d.SLA_GRADIENT_SEED] = 10 # 
    shader[c4d.SLA_GRADIENT_ANGLE] = c4d.utils.DegToRad(5) # угол в радианах
    # обязательно вставляем шейдер в материал.
    material.InsertShader(shader)
    # назначаем шейдер в канал цвета
    material[c4d.MATERIAL_COLOR_SHADER] = shader

    # вставляем материал в документ
    doc.InsertMaterial(material)
    c4d.EventAdd() # обновляем сцену

if __name__=='__main__':
    main()