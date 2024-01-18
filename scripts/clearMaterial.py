import c4d

def main():
    # doc - предустановленная переменная
    # Получаем активный документ, теперь не нужно
    #doc = documents.GetActiveDocument()

    # Создаем список для материалов, которые нужно удалить
    materials_to_remove = []

    # Получаем первый материал в документе
    material = doc.GetFirstMaterial()

    # Проходимся по всем материалам в документе
    while material is not None:
        # Если имя материала начинается на "mat"
        if material.GetName().startswith("mat"):
            # Добавляем материал в список для удаления
            materials_to_remove.append(material)
        # Переходим к следующему материалу
        material = material.GetNext()

    # это нужно для отмены по ctrl+Z
    doc.StartUndo()
    # Удаляем все материалы в списке
    for material in materials_to_remove:
        # добавляем действие в стек для отмены
        doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ,material)
        material.Remove()
    # закрываем стек для запоминания отмены
    doc.EndUndo()

    # Обновляем документ
    c4d.EventAdd()

# Выполняем функцию main
if __name__=='__main__':
    main()