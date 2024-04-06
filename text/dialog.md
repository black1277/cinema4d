## Как создать диалоговое окно в Cinema4D

Большинство диалоговых окон являются производными от класса [GeDialog][1]
Диалог — это окно или панель, на которой расположены кнопки, поля редактирования, значки, изображения и другие элементы.
Эти кнопки, ползунки, значки и т. д. называются виджетами.
Диалоги действуют как интерфейсы для плагина.
Для начала нужно определить класс производный от `c4d.gui.GeDialog` и в нём методы `CreateLayout` и `Command`:
```python
import c4d
from c4d import gui

# Идентификаторы для элементов управления
COLOR_ID = 1000
APPLY_BUTTON_ID = 1001

class ColorChangerDialog(gui.GeDialog):
    def CreateLayout(self):
        # Устанавливаем заголовок окна диалога
        self.SetTitle("Color Changer")

        # Добавляем цветовой выбор
        self.AddColorField(COLOR_ID, c4d.BFH_SCALEFIT, initw=150, inith=0)

        # Добавляем кнопку для применения цвета
        self.AddButton(APPLY_BUTTON_ID, c4d.BFH_CENTER, name="Apply Color")

        return True

    def Command(self, id, msg):
        # Обработка событий от элементов управления
        if id == APPLY_BUTTON_ID:
            # Получаем выбранный цвет из цветового поля
            color = self.GetColorField(COLOR_ID)

            # Получаем активный объект в документе
            active_object = doc.GetActiveObject()

            # Если объект выбран, устанавливаем его цвет
            if active_object:
                active_object[c4d.ID_BASEOBJECT_USECOLOR] = c4d.ID_BASEOBJECT_USECOLOR_ALWAYS
                active_object[c4d.ID_BASEOBJECT_COLOR] = color['color']
                active_object.Message(c4d.MSG_UPDATE)
                c4d.EventAdd()
            else:
                gui.MessageDialog("No object selected.")
            # Закрываем окно
            self.Close()
        return True

# Главная функция
def main():
    # Создаем экземпляр диалога
    dlg = ColorChangerDialog()

    # Открываем диалог модально
    dlg.Open(dlgtype=c4d.DLG_TYPE_MODAL, defaultw=300, defaulth=50)

if __name__ == "__main__":
    main()
```
Этот простенький пример создает диалоговое окно, в котором можно выбрать цвет и после нажатия кнопки `Apply Color` он будет применен к выделенному объекту (не к материалу), а так же у него будет включено цветовое отображение во вьюпорте.










[1]: https://developers.maxon.net/docs/py/23_110/modules/c4d.gui/GeDialog/index.html "c4d.gui » c4d.gui.GeDialog"