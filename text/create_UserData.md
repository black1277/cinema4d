
## Как создать пользовательские данные(атрибуты) на объекте
Поскольку в менеджере атрибутов могут быть очень разнообразные виды данных - вкладки, кнопки, разделители, сплайны и др. начнем с простых типов. Создадим сначала
### десятичный и целочисленный типы атрибутов.
1. создаем контейнер с нужным типом. ```c4d.DTYPE_REAL``` - создает число с плавающей точкой. Другие типы смотрим в [документации][1]
```Python
FloatData = c4d.GetCustomDataTypeDefault(c4d.DTYPE_REAL)
```
2. дадим ему название
```Python
FloatData[c4d.DESC_NAME] = "Float Data"
FloatData[c4d.DESC_SHORT_NAME] = "FData"
```
3. зададим параметры. Узнать о других можно [тут][2]
```Python
FloatData[c4d.DESC_MIN] = -10  # минимальное
FloatData[c4d.DESC_MAX] = 10   # максимальное значение
FloatData[c4d.DESC_STEP] = 0.25# шаг изменения
FloatData[c4d.DESC_DEFAULT] = 6.25# можно задать значение по умолчанию
FloatData[c4d.DESC_ANIMATE] = c4d.DESC_ANIMATE_ON # может анимироваться
```
4. добавим этот контейнер на выделенный объект
```Python
FloatId = op.AddUserData(FloatData)
```
Получим идентификатор объекта, который будем использовать для назначения и получения данных
```Python
op[FloatId] = 3.1415 # зададим значение или
param = op[FloatId]  # получим значение
c4d.EventAdd() # для обновления
```
Для создания атрибута с целочисленным значением все будет то же самое, за исключением того, что в первом пункте используем тип ```c4d.DTYPE_LONG```, а в третьем пункте параметры ```c4d.DESC_STEP``` и ```c4d.DESC_DEFAULT``` должны быть только целыми числами (иначе будет ошибка)

### разделительную линию:
```Python
separator = c4d.GetCustomDataTypeDefault(c4d.DTYPE_SEPARATOR)
separator[c4d.DESC_CUSTOMGUI] = 11
separator[c4d.DESC_NAME] = "Separator Title" # Надпись возле линии. Можно оставить пустой
separator[c4d.DESC_SHORT_NAME] = "Separator Title" # аналогично
separator[c4d.DESC_SEPARATORLINE] = 1
separatorId = op.AddUserData(separator)
c4d.EventAdd()
```
Примечание: разделительная линия становится видна только когда находится между данными, которые разделяет.

### группы вкладок:
1. для создания вкладки используем ```c4d.DTYPE_GROUP```:
```Python
myGroup = c4d.GetCustomDataTypeDefault(c4d.DTYPE_GROUP)
myGroup[c4d.DESC_NAME] = "MyBigGroup" # установим имя
```
2. создадим атрибут, который хотим поместить во вкладку:
```Python
innerLONGData = c4d.GetCustomDataTypeDefault(c4d.DTYPE_LONG)
innerLONGData[c4d.DESC_NAME] = "Long"
innerLONGData[c4d.DESC_MIN] = -10
innerLONGData[c4d.DESC_MAX] = 10
innerLONGData[c4d.DESC_STEP] = 2
```
3. теперь нужно создать дескриптор, посредством которого можно прикрепить атрибут к созданной вкладке:
```Python
descId = c4d.DescID(
    c4d.DescLevel(c4d.ID_USERDATA, c4d.DTYPE_SUBCONTAINER, 0),# пользовательские данные, тип субконтейнер
    c4d.DescLevel(1, c4d.DTYPE_GROUP, 0)) # единица - это ID вкладки
```
сначала, бывает непонятно что это за конструкция. Нужно почитать больше о том, что такое ```c4d.DescID``` и ```c4d.DescLevel```

4. назначаем родителем нашего атрибута созданную вкладку
```Python
innerLONGData[c4d.DESC_PARENTGROUP] = descId
```
5. добавляем вкладку и атрибут на выделенный объект
```Python
outerGroupId = op.AddUserData(myGroup)
innerLONGDId = op.AddUserData(innerLONGData)
```
:exclamation: Внимание: тут важен порядок добавления (нам нужно чтобы ID вкладки был равен единице - именно ее мы использовали в дескрипторе)

### создание сплайновых данных
1. Сначала, создаем контейнер нужного типа
```Python
bc = c4d.GetCustomDataTypeDefault(c4d.CUSTOMDATATYPE_SPLINE)
```
2. Дадим ему имя и настроим параметры
```Python
bc[c4d.DESC_NAME] = "MySpline"
bc[c4d.DESC_SHORT_NAME] = "MySpline"
bc[c4d.SPLINECONTROL_GRID_H] = False # Disable the horizontal grid lines in the SplineCustomGui.
```
Другие параметры настройки SPLINECONTROL_ смотрим в [документации][3]

3. добавим этот контейнер на выделенный объект
```Python
paramId = op.AddUserData(bc)
```
4. Теперь создадим сплайн(кубический) из 5 точек
```Python
spline = c4d.SplineData()
spline.MakeCubicSpline(5) # тип сплайна кубический
#spline.MakeUserSpline("1.0 - sin(x * PI)", 5) # по формуле
#spline.MakeLinearSplineLinear(5) # линейный
```
В качестве примера закомментированы сплайн по формуле и линейный. Другие типы сплайнов в [документации][4]

5. назначаем сплайн в атрибут выделенного объекта и обновляем сцену
```Python
op[paramId] = spline
c4d.EventAdd()
```

### создание кнопки
В обычном скрипте нет смысла создавать кнопки в атрибутах объекта - скрипт отработал и не сможет реагировать на нажатия. Но если предполагается длительная работа и нужно проверять состояние кнопки то вот:
```Python
import c4d
from c4d import gui

def main():
    # создадим нуль-объект
    null_object = c4d.BaseObject(c4d.Onull)

    btn_bc = c4d.GetCustomDatatypeDefault(c4d.DTYPE_BUTTON)
    btn_bc.SetString(c4d.DESC_NAME, "Click")
    btn_bc.SetString(c4d.DESC_SHORT_NAME, "click")
    btn_bc.SetInt32(c4d.DESC_CUSTOMGUI, c4d.CUSTOMGUI_BUTTON) # назначим интерфейс в виде кнопки

    btnID = null_object.AddUserData(btn_bc) # установим на нуль-объект
    null_object[btnID] = False # считаем что не нажата
    c4d.SendCoreMessage(c4d.COREMSG_CINEMA, c4d.BaseContainer(c4d.COREMSG_CINEMA_FORCE_AM_UPDATE))

    doc.InsertObject(null_object) # добавим наш нуль-объект в сцену

    btnValue = null_object[c4d.ID_USERDATA,1]  #<---вернет true/false в зависимости от состояния кнопки
    print (btnValue)

    c4d.EventAdd()

if __name__=='__main__':
    main()
```
Так же здесь использован другой синтаксис для назначения параметров объекту контейнера. В плагинах, генераторах и тегах питона используется метод message для доступа к событию нажатия кнопки.





[1]: https://developers.maxon.net/docs/py/23_110/modules/c4d/index.html?highlight=c4d%20getcustomdatatypedefault#c4d.GetCustomDataTypeDefault "c4d.GetCustomDataTypeDefault"
[2]: https://developers.maxon.net/docs/py/23_110/modules/c4d/Description/index.html "c4d.Description"
[3]: https://developers.maxon.net/docs/py/23_110/modules/c4d.gui/BaseCustomGui/SplineCustomGui/index.html "c4d.gui.SplineCustomGui"
[4]: https://developers.maxon.net/docs/py/23_110/modules/c4d/CustomDataType/SplineData/index.html "c4d.SplineData"
