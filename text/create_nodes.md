# Python для Cinema 4D
## Как создать узлы в Xpresso и соединить их

Получаем тег Xpresso и корневой узел:
```Python
# Получаем активный объект в документе
my_object = doc.GetActiveObject()

# Получаем тег Xpresso, предполагается, что он уже прикреплен к объекту
xpresso_tag = my_object.GetTag(c4d.Texpresso)

# Получаем мастер узлов и корневой узел
node_master = xpresso_tag.GetNodeMaster()
root = node_master.GetRoot()
```
Создадим узел объекта и математический узел:
```Python
node1 = node_master.CreateNode(root, c4d.ID_OPERATOR_OBJECT, x=200, y=100)
node2 = node_master.CreateNode(root, c4d.ID_OPERATOR_MATH, x=400, y=100)
```
Другие типы узлов смотрим в [документации][1], а их [параметры ищем тут][2]

У мат.оператора поменяем тип данных на целочисленный и тип функции на умножение. Для изменения этих параметров, сначала надо получить контейнер с настройками соответствующего узла:
```Python
bc = node2.GetOperatorContainer() # получаем контейнер мат.узла

bc[c4d.GV_DYNAMIC_DATATYPE] = c4d.DTYPE_LONG # меняем тип данных

bc[c4d.GV_MATH_FUNCTION_ID] = c4d.GV_MUL_NODE_FUNCTION # меняем функцию

node2.SetOperatorContainer(bc) # сохраняем изменения в узле

print(node2[c4d.GV_DYNAMIC_DATATYPE]) # можно вывести значение параметра
```
Обратите внимание: значение параметра можно прочитать обратившись к соответвующему свойству, но изменить его напрямую, присвоив значение нельзя (```node2[c4d.GV_DYNAMIC_DATATYPE] = c4d.DTYPE_LONG``` - выдаст ошибку!)

Можно задать узлу своё название:
```Python
node2.SetName("My Math operator")
```
Теперь, добавляем порты и соединяем:
```Python
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
```




[1]: https://developers.maxon.net/docs/py/23_110/types/gvnodes.html "Types and Symbols List » Graph View Node Types"
[2]: https://developers.maxon.net/docs/py/23_110/classic_resource/resource_overview.html#graphview-operators "Classic Resource overview"
