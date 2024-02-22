import c4d

def main():
    cube = c4d.BaseObject(c4d.Ocube)
    # устанавливаем стороны для куба по 45
    cube[c4d.PRIM_CUBE_LEN] = c4d.Vector(45.,45., 45.)
    cloner = c4d.BaseObject(1018544)
    cloner.SetName('сloner')
    cloner[c4d.ID_MG_MOTIONGENERATOR_MODE]=1
    cloner[c4d.MG_LINEAR_COUNT]=7
    cloner[c4d.MG_LINEAR_OBJECT_POSITION] = c4d.Vector(50, 0, 0)
    #cloner[c4d.MG_LINEAR_OBJECT_POSITION,c4d.VECTOR_X] = 50
    #cloner[c4d.MG_LINEAR_OBJECT_POSITION,c4d.VECTOR_Y] = 0
    cube.InsertUnder(cloner)# подчиняем куб клонеру
    doc.InsertObject(cloner) # добавили клонер
    # Обновляем сцену после добавления новых объектов
    c4d.EventAdd()

if __name__=='__main__':
    main()