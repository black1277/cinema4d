import c4d
from c4d import documents

def main():
    # Получаем активный документ
    doc = documents.GetActiveDocument()

    my_object = doc.GetActiveObject()

    # Получаем или создаем тег Xpresso, предполагается, что он уже прикреплен к объекту
    xpresso_tag = my_object.GetTag(c4d.Texpresso)
    if xpresso_tag is None: # если тега нет - создаем
        xpresso_tag = c4d.BaseTag(c4d.Texpresso)
        my_object.InsertTag(xpresso_tag) # вешаем на объект

    # Получаем мастер узлов и корневую группу
    node_master = xpresso_tag.GetNodeMaster() # GvNodeMaster
    # print(node_master.GetName())
    # print(node_master.GetTypeName())
    root = node_master.GetRoot() # XГруппа
    # print(root.GetName())
    # print(root.GetTypeName())

    # Создаем узел объект в Xpresso
    node = node_master.CreateNode(root, c4d.ID_OPERATOR_OBJECT, x=20, y=10)
    node[c4d.GV_OBJECT_OBJECT_ID] = my_object # привязываем узел к нашему объекту

    # Создаем пользовательские данные
    bc = c4d.GetCustomDatatypeDefault(c4d.DTYPE_LONG)
    bc[c4d.DESC_NAME] = "MyUserData"
    element = my_object.AddUserData(bc)

    # Создаем пользовательские данные
    bc = c4d.GetCustomDatatypeDefault(c4d.DTYPE_LONG)
    bc[c4d.DESC_NAME] = "OtherData"
    element = my_object.AddUserData(bc)


    # Создаем входной порт для пользовательских данных
    USERDATA_NUMBER = 1 # эта переменная должна быть равна ID в менеджере атрибутов
    node.AddPort(c4d.GV_PORT_INPUT, c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA, c4d.DTYPE_SUBCONTAINER, 0), c4d.DescLevel(USERDATA_NUMBER)), message=True)

    USERDATA_NUMBER = 2
    node.AddPort(c4d.GV_PORT_OUTPUT, c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA, c4d.DTYPE_SUBCONTAINER, 0), c4d.DescLevel(USERDATA_NUMBER)), message=True)

    # Обновляем документ
    c4d.EventAdd()

# Выполняем функцию main
if __name__=='__main__':
    main()