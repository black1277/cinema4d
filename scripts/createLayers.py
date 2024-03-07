import c4d
from c4d import gui

def CreateLayer2 (name, layercolor): 
    layer = c4d.documents.LayerObject() 
    layer[c4d.ID_LAYER_COLOR] = layercolor 
    layer.SetName(name) 
    # Get the invisible root layer
    layerRoot = doc.GetLayerObjectRoot() 
    # Insert the layer under the parent 
    layer.InsertUnder(layerRoot)

# Main function
def main():
    CreateLayer2 ('MyLayer', c4d.Vector(0.5, 0.3, 0.9) )
    print(op[c4d.ID_LAYER_LINK] )
    #ly = c4d.CallCommand(100004738) # создать новый слой
    root = doc.GetLayerObjectRoot()  # Gets the layer manager
    LayersList = root.GetChildren()  # Get Layer list

    for layers in LayersList:
        name = layers.GetName()
        print('=========== ',name, ' =============')
        print('ID_LAYER_SOLO ', layers[c4d.ID_LAYER_SOLO])
        print('ID_LAYER_VIEW ', layers[c4d.ID_LAYER_VIEW])
        print('ID_LAYER_RENDER ', layers[c4d.ID_LAYER_RENDER])
        print('ID_LAYER_MANAGER ', layers[c4d.ID_LAYER_MANAGER])
        print('ID_LAYER_LOCKED ', layers[c4d.ID_LAYER_LOCKED])
        print('ID_LAYER_GENERATORS ', layers[c4d.ID_LAYER_GENERATORS])
        print('ID_LAYER_DEFORMERS ', layers[c4d.ID_LAYER_DEFORMERS])
        print('ID_LAYER_EXPRESSIONS ', layers[c4d.ID_LAYER_EXPRESSIONS])
        print('ID_LAYER_ANIMATION ', layers[c4d.ID_LAYER_ANIMATION])
        print('ID_LAYER_COLOR ', layers[c4d.ID_LAYER_COLOR])
        print('ID_LAYER_XREF ', layers[c4d.ID_LAYER_XREF])
        print('BIT_ACTIVE ', layers.GetBit(c4d.BIT_ACTIVE))
        # layers[c4d.ID_LAYER_MANAGER] = 0
        # layers[c4d.ID_LAYER_LOCKED] = 1
        # obj[c4d.ID_LAYER_LINK] = layers #привязать объект к слою
        
        layer_data = layers.GetLayerData(doc)# другой способ доступа
        lockValue = layer_data["locked"]
        # layers.SetLayerData(doc, layer_data)
        print(layer_data)# {'solo': False, 'view': True, 'render': True, 'manager': True, 'locked': False, 'generators': True, 'deformers': True, 'expressions': True, 'animation': True, 'color': Vector(0.5, 0.3, 0.9), 'xref': True}

    c4d.EventAdd()
# Execute main()
if __name__=='__main__':
    main()