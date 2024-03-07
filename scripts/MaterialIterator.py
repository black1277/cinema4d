import c4d
from c4d import documents as docs

class MaterialIterator:
    def __init__(self, doc):
        self.doc = doc
        self.currentMaterial = None
        if doc == None : return
        self.currentMaterial = doc.GetFirstMaterial()

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentMaterial == None :
            raise StopIteration

        mat = self.currentMaterial
        self.currentMaterial = self.currentMaterial.GetNext()
        return mat


if __name__ == '__main__':
    doc = docs.GetActiveDocument()
    materials = MaterialIterator(doc)

    for mat in materials:
        print (mat.GetName, " - ", mat.GetTypeName())
