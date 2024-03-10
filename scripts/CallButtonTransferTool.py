import c4d  
from c4d import plugins  
  
def main() :  
  # сфера должна быть выделена
  # исполнение скрипта перемещает сферу к кубу
  movedObj = doc.SearchObject("Sphere")  
  targetObj = doc.SearchObject("Cube")  
    
  c4d.CallCommand(c4d.ID_MODELING_TRANSFER_TOOL)   #Launch the Transfer tool  
    
  tool = plugins.FindPlugin(doc.GetAction(), c4d.PLUGINTYPE_TOOL)  
  if tool is not None:  
      tool[c4d.MDATA_TRANSFER_OBJECT_LINK] = targetObj  
      c4d.CallButton(tool, c4d.MDATA_APPLY)  
  c4d.EventAdd()  
  
if __name__=='__main__':  
  main()  