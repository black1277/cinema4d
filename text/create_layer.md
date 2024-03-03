# Python для Cinema 4D
## Как создать слой Layer

Создадим новый слой:
```Python
layer = c4d.documents.LayerObject() 
```
см. [LayerObject][1]

Назначим ему цвет и дадим имя:
```Python
layer[c4d.ID_LAYER_COLOR] = c4d.Vector(0.5, 0.3, 0.9)
layer.SetName("MyLayer") 
```
Получим невидимый корневой слой и добавим в него созданный:
```Python
layerRoot = doc.GetLayerObjectRoot() 
layer.InsertUnder(layerRoot)
```
см. [GetLayerObjectRoot][2]

Чтобы добавить объект к созданному слою нужно:
```Python
obj[c4d.ID_LAYER_LINK] = layer #привязать объект к слою
```

Чтобы изменить свойства слоя, нужно обратиться к соответствующим [параметрам слоя][3]. Пример ниже выведет все свойства всех слоев в документе:
```Python
root = doc.GetLayerObjectRoot()  # Gets the layer manager
LayersList = root.GetChildren()  # Get Layer list

for layers in LayersList:
    name = layers.GetName()
    print('=========== ',name, ' =============')
    print('ID_LAYER_SOLO', layers[c4d.ID_LAYER_SOLO])
    print('ID_LAYER_VIEW', layers[c4d.ID_LAYER_VIEW])
    print('ID_LAYER_RENDER', layers[c4d.ID_LAYER_RENDER])
    print('ID_LAYER_MANAGER', layers[c4d.ID_LAYER_MANAGER])
    print('ID_LAYER_LOCKED', layers[c4d.ID_LAYER_LOCKED])
    print('ID_LAYER_GENERATORS', layers[c4d.ID_LAYER_GENERATORS])
    print('ID_LAYER_DEFORMERS', layers[c4d.ID_LAYER_DEFORMERS])
    print('ID_LAYER_EXPRESSIONS', layers[c4d.ID_LAYER_EXPRESSIONS])
    print('ID_LAYER_ANIMATION', layers[c4d.ID_LAYER_ANIMATION])
    print('ID_LAYER_COLOR', layers[c4d.ID_LAYER_COLOR])
    print('ID_LAYER_XREF', layers[c4d.ID_LAYER_XREF])
    print('BIT_ACTIVE', layers.GetBit(c4d.BIT_ACTIVE))
```
Есть и другой синтаксис доступа к параметрам:
```Python
layer_data = layers.GetLayerData(doc)# другой способ доступа
print(layer_data)# выведет {'solo': False, 'view': True, 'render': True, 'manager': True, 'locked': False, 'generators': True, 'deformers': True, 'expressions': True, 'animation': True, 'color': Vector(0.5, 0.3, 0.9), 'xref': True}
lockValue = layer_data["locked"] # получить значение
layer_data["locked"] = True # изменить значение
layers.SetLayerData(doc, layer_data) # установить новые значения на слой
```




[1]: https://developers.maxon.net/docs/py/23_110/modules/c4d.documents/LayerObject/index.html "LayerObject"
[2]: https://developers.maxon.net/docs/py/23_110/modules/c4d.documents/BaseDocument/index.html?highlight=getlayerobjectroot#BaseDocument.GetLayerObjectRoot "GetLayerObjectRoot"
[3]: https://developers.maxon.net/docs/py/23_110/classic_resource/base_list/olayer.html "Layer"