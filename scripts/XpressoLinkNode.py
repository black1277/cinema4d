import c4d
from c4d import documents

PYTHON_TAG_SCRIPT = """import c4d

def main():
    global Output1
    print ('Text')
    Output1 = Input1
"""


def main():
    # Получаем активный документ
    doc = documents.GetActiveDocument()

    # Получаем активный объект в документе
    my_object = c4d.BaseObject(c4d.Ocube)
    doc.InsertObject(my_object)

    xpresso_tag = c4d.BaseTag(c4d.Texpresso)
    my_object.InsertTag(xpresso_tag)

    # Получаем мастер узлов и корневой узел
    node_master = xpresso_tag.GetNodeMaster()
    root = node_master.GetRoot()

    # Создаем узлы в Xpresso
    node1 = node_master.CreateNode(root, c4d.ID_OPERATOR_OBJECT, x=200, y=100)
    node2 = node_master.CreateNode(root, c4d.ID_OPERATOR_MATH, x=400, y=100)


    # все узлы перечисленные в документации, расположены в столбик
    node_master.CreateNode(root, c4d.ID_GV_OPERATOR_DUMMY, x=10, y=50)
    node_master.CreateNode(root, c4d.ID_GV_OPERATOR_GROUP, x=10, y=100)
    node_master.CreateNode(root, c4d.ID_OPERATOR_ABS, x=10, y=150)
    node_master.CreateNode(root, c4d.ID_OPERATOR_ADAPTER, x=10, y=200)
    node_master.CreateNode(root, c4d.ID_OPERATOR_BITMAP, x=10, y=250)
    node_master.CreateNode(root, c4d.ID_OPERATOR_BOOL, x=10, y=300)
    node_master.CreateNode(root, c4d.ID_OPERATOR_BOX, x=10, y=350)
    node_master.CreateNode(root, c4d.ID_OPERATOR_CLAMP, x=10, y=400)
    node_master.CreateNode(root, c4d.ID_OPERATOR_CMP, x=10, y=450)
    node_master.CreateNode(root, c4d.ID_OPERATOR_COFFEE, x=10, y=500)
    node_master.CreateNode(root, c4d.ID_OPERATOR_COLLISION, x=10, y=550)
    node_master.CreateNode(root, c4d.ID_OPERATOR_COLORSPACE, x=10, y=600)
    node_master.CreateNode(root, c4d.ID_OPERATOR_COLORTEMP, x=10, y=650)
    node_master.CreateNode(root, c4d.ID_OPERATOR_COMMENT, x=10, y=700)
    node_master.CreateNode(root, c4d.ID_OPERATOR_CONDITION, x=10, y=750)
    node_master.CreateNode(root, c4d.ID_OPERATOR_CONST, x=10, y=800)
    node_master.CreateNode(root, c4d.ID_OPERATOR_CROSS, x=10, y=850)
    node_master.CreateNode(root, c4d.ID_OPERATOR_DEGREE, x=10, y=900)
    node_master.CreateNode(root, c4d.ID_OPERATOR_DETAILS, x=10, y=950)
    node_master.CreateNode(root, c4d.ID_OPERATOR_DISTANCE, x=10, y=1000)
    node_master.CreateNode(root, c4d.ID_OPERATOR_DOT, x=10, y=1050)
    node_master.CreateNode(root, c4d.ID_OPERATOR_EQU, x=10, y=1100)
    node_master.CreateNode(root, c4d.ID_OPERATOR_FLOATFUNC, x=10, y=1150)
    node_master.CreateNode(root, c4d.ID_OPERATOR_FLOATMATH, x=10, y=1200)
    node_master.CreateNode(root, c4d.ID_OPERATOR_FORMULA, x=10, y=1250)
    node_master.CreateNode(root, c4d.ID_OPERATOR_FREEZE, x=10, y=1300)
    node_master.CreateNode(root, c4d.ID_OPERATOR_HIERARCHY, x=10, y=1350)
    node_master.CreateNode(root, c4d.ID_OPERATOR_INCLUDE, x=10, y=1400)
    node_master.CreateNode(root, c4d.ID_OPERATOR_INV, x=10, y=1450)
    node_master.CreateNode(root, c4d.ID_OPERATOR_ITERATE, x=10, y=1500)
    node_master.CreateNode(root, c4d.ID_OPERATOR_LINK, x=10, y=1550)
    node_master.CreateNode(root, c4d.ID_OPERATOR_MATERIAL, x=10, y=1600)
    node_master.CreateNode(root, c4d.ID_OPERATOR_MATH, x=10, y=1650)
    node_master.CreateNode(root, c4d.ID_OPERATOR_MATRIX2VECT, x=10, y=1700)
    node_master.CreateNode(root, c4d.ID_OPERATOR_MATRIXCALCHPB, x=10, y=1750)
    node_master.CreateNode(root, c4d.ID_OPERATOR_MATRIXMULVECTOR, x=10, y=1800)
    node_master.CreateNode(root, c4d.ID_OPERATOR_MEMORY, x=10, y=1850)
    node_master.CreateNode(root, c4d.ID_OPERATOR_MIX, x=10, y=1900)
    node_master.CreateNode(root, c4d.ID_OPERATOR_MONOFLOP, x=10, y=1950)
    node_master.CreateNode(root, c4d.ID_OPERATOR_NEG, x=10, y=2000)
    node_master.CreateNode(root, c4d.ID_OPERATOR_NIL, x=10, y=2050)
    node_master.CreateNode(root, c4d.ID_OPERATOR_NOISE, x=10, y=2100)
    node_master.CreateNode(root, c4d.ID_OPERATOR_NOT, x=10, y=2150)
    node_master.CreateNode(root, c4d.ID_OPERATOR_OBJECT, x=10, y=2200)
    node_master.CreateNode(root, c4d.ID_OPERATOR_ORDER, x=10, y=2250)
    node_master.CreateNode(root, c4d.ID_OPERATOR_POINT, x=10, y=2300)
    node_master.CreateNode(root, c4d.ID_OPERATOR_POLYGON, x=10, y=2350)
    node_master.CreateNode(root, c4d.ID_OPERATOR_RANDOM, x=10, y=2400)
    node_master.CreateNode(root, c4d.ID_OPERATOR_RANGEMAPPER, x=10, y=2450)
    node_master.CreateNode(root, c4d.ID_OPERATOR_RAY, x=10, y=2500)
    node_master.CreateNode(root, c4d.ID_OPERATOR_REAL2VECT, x=10, y=2550)
    node_master.CreateNode(root, c4d.ID_OPERATOR_REFERENCE, x=10, y=2600)
    res = node_master.CreateNode(root, c4d.ID_OPERATOR_RESULT, x=10, y=2650)
    node_master.CreateNode(root, c4d.ID_OPERATOR_SELECTION, x=10, y=2700)
    node_master.CreateNode(root, c4d.ID_OPERATOR_SOUND, x=10, y=2750)
    node_master.CreateNode(root, c4d.ID_OPERATOR_SPLINE, x=10, y=2800)
    node_master.CreateNode(root, c4d.ID_OPERATOR_SPY, x=10, y=2850)
    node_master.CreateNode(root, c4d.ID_OPERATOR_SWITCH, x=10, y=2900)
    node_master.CreateNode(root, c4d.ID_OPERATOR_TAG, x=10, y=2950)
    node_master.CreateNode(root, c4d.ID_OPERATOR_TAKEOVERRIDE, x=10, y=3000)
    node_master.CreateNode(root, c4d.ID_OPERATOR_TIME, x=10, y=3050)
    node_master.CreateNode(root, c4d.ID_OPERATOR_TRACK, x=10, y=3100)
    node_master.CreateNode(root, c4d.ID_OPERATOR_TRIGGER, x=10, y=3150)
    node_master.CreateNode(root, c4d.ID_OPERATOR_TRIGO, x=10, y=3200)
    node_master.CreateNode(root, c4d.ID_OPERATOR_VECT2MATRIX, x=10, y=3250)
    node_master.CreateNode(root, c4d.ID_OPERATOR_VECT2REAL, x=10, y=3300)
    node_master.CreateNode(root, c4d.ID_OPERATOR_VECTCALCMATRIX, x=10, y=3350)
    node_master.CreateNode(root, c4d.ID_OPERATOR_WEIGHTMAP, x=10, y=3400)
    node_master.CreateNode(root, c4d.ID_OPERATOR_VERTEXCOLOR, x=10, y=3450)
    
    # а это узел Python
    py_node = node_master.CreateNode(root, 1022471, x=10, y=3500)
    bc = py_node.GetOperatorContainer() # получаем контейнер
    bc[c4d.GV_PYTHON_CODE] = PYTHON_TAG_SCRIPT # добавим свой код
    py_node.SetOperatorContainer(bc) # сохраняем изменения в узле
    py_out = py_node.GetOutPorts()[0] # получаем выходной порт узла питона
    res_in = res.GetInPorts()[0] # получаем входной порт узла результата
    py_out.Connect(res_in) # соединяем
    
    # Добавляем порты
    node1.AddPort(c4d.GV_PORT_INPUT, c4d.ID_BASEOBJECT_REL_POSITION)
    node1.AddPort(c4d.GV_PORT_OUTPUT, c4d.ID_BASEOBJECT_REL_POSITION)

    # Получаем порты узлов
    node1_out = node1.GetOutPorts()[0]
    node2_in = node2.GetInPorts()[0]

    # Соединяем порты
    node1_out.Connect(node2_in)

    # Обновляем документ
    c4d.EventAdd()

# Выполняем функцию main
if __name__=='__main__':
    main()