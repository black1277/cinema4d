import c4d
from c4d import documents as docs

class TagIterator:

    def __init__(self, obj):
        currentTag = None
        if obj :
            self.currentTag = obj.GetFirstTag()

    def __iter__(self):
        return self

    def __next__(self):
        tag = self.currentTag
        if tag == None :
            raise StopIteration

        self.currentTag = tag.GetNext()
        return tag
    
if __name__ == '__main__':
    doc = docs.GetActiveDocument()
    obj = doc.GetFirstObject()

    tags = TagIterator(obj)
    for tag in tags:
        print (tag.GetTypeName())