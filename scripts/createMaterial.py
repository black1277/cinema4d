import c4d

def apply_material():
    doc = c4d.documents.GetActiveDocument()
    if doc is None:
        doc = c4d.documents.BaseDocument()
        c4d.documents.InsertBaseDocument(doc)

    sphere = c4d.BaseObject(c4d.Osphere)
    doc.InsertObject(sphere)

    mat = c4d.Material(c4d.Mbase)
    mat.SetName('red')
    mat[c4d.MATERIAL_COLOR_COLOR] = c4d.Vector(1,0,0)
    mat[c4d.MATERIAL_USE_REFLECTION] = False
    doc.InsertMaterial(mat)
    tag = sphere.MakeTag(c4d.Ttexture)
    tag[c4d.TEXTURETAG_MATERIAL] = mat

    c4d.EventAdd()

if __name__=='__main__':
    apply_material()