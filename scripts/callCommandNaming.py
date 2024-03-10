import c4d  
from c4d import gui  
  
def main() :  
  
  c4d.CallCommand(1019952)  
  tool=doc.GetAction()  
  tool=c4d.plugins.FindPlugin(tool, c4d.PLUGINTYPE_TOOL)  
  tool[c4d.ID_CA_JOINT_NAMING_REPLACE] = "Cube"               #Set the text to replace
  tool[c4d.ID_CA_JOINT_NAMING_REPLACE_WITH]= "Object"          #Set the new text      
  c4d.CallButton(tool, c4d.ID_CA_JOINT_NAMING_REPLACE_APPLY)  
  c4d.EventAdd()  
  
if __name__=='__main__':  
  main()