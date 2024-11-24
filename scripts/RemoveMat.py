import c4d
from c4d import documents as docs
"""
Скрипт удаляет со всех объектов сцены теги материалов, которых нет в менеджере материалов (теги с вопросами)
"""
class ObjectIterator:
    def __init__(self, baseObject):
        self.baseObject = baseObject
        self.currentObject = baseObject
        self.objectStack = []
        self.depth = 0
        self.nextDepth = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentObject == None :
            raise StopIteration

        obj = self.currentObject
        self.depth = self.nextDepth

        child = self.currentObject.GetDown()
        if child :
            self.nextDepth = self.depth + 1
            self.objectStack.append(self.currentObject.GetNext())
            self.currentObject = child
        else :
            self.currentObject = self.currentObject.GetNext()
            while( self.currentObject == None and len(self.objectStack) > 0 ) :
                self.currentObject = self.objectStack.pop()
                self.nextDepth = self.nextDepth - 1
        return obj


def removeTag(all_tags, all_materials):
    # для подсчета удаленных тегов
    rem_tags = 0
    # Проходим по каждому тегу
    for tag in all_tags:
        # print('Текущий тег: ', tag)
        # Проверяем, что это тег и он является тегом материала
        if isinstance(tag, c4d.BaseTag) and tag.GetType() == c4d.Ttexture:
            # Получаем материал, связанный с тегом
            material = tag[c4d.TEXTURETAG_MATERIAL]
            # print('Материал тега: ', material)
            # Если материал не в списке материалов, удаляем тег
            if material not in all_materials:
                doc.AddUndo(c4d.UNDOTYPE_DELETE, tag)
                tag.Remove()
                rem_tags = rem_tags + 1
    return rem_tags # вернем сколько всего удалили

def main():
    # Получаем активный документ
    doc = c4d.documents.GetActiveDocument()
    obj = doc.GetFirstObject()
    # получаем все объекты сцены
    scene = ObjectIterator(obj)

    # Получаем список всех материалов в документе
    all_materials = doc.GetMaterials()
    # для отслеживания количества удаленных тегов
    removed_tags = 0

    doc.StartUndo()
    for obj in scene:
        # print (scene.depth, scene.depth*'    ', obj.GetName())
        flagDel = removeTag(obj.GetTags(), all_materials)
        removed_tags = removed_tags + flagDel
    doc.EndUndo()

    # Если были удалены теги, выводим сообщение
    if removed_tags > 0:
        c4d.gui.MessageDialog(f"Теги с отсутствующими материалами были удалены! Всего = {removed_tags}")
    else:
        c4d.gui.MessageDialog('Нет тегов с отсутствующими материалами')

    # Обновляем документ
    c4d.EventAdd()

if __name__=='__main__':
    main()