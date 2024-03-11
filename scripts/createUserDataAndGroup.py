import c4d

# создает на объекте пользовательские данные во вложенных группах
# на сцене должен быть объект, к которому они будут привязаны
# https://developers.maxon.net/topic/13517/how-to-add-a-userdata-child-to-a-group-via-script/4
def main():
   """
   """
   # Not required, as op is already predefined as the active object in a
   # script manger script.
   # op=doc.GetActiveObject()

   # Create a group element.
   outerGroupData = c4d.GetCustomDataTypeDefault(c4d.DTYPE_GROUP)
   outerGroupData[c4d.DESC_NAME] = "Outer Group"

   # A float element in the outer group.
   outerFloatData = c4d.GetCustomDataTypeDefault(c4d.DTYPE_REAL)
   outerFloatData[c4d.DESC_NAME] = "Some Float"
   outerFloatData[c4d.DESC_MIN] = -10
   outerFloatData[c4d.DESC_MAX] = 10
   outerFloatData[c4d.DESC_STEP] = 0.5
   #   descId = c4d.DescID(
   #       c4d.DescLevel(c4d.ID_USERDATA, c4d.DTYPE_SUBCONTAINER, 0),
   #       c4d.DescLevel(1, c4d.DTYPE_GROUP, 0))
   # Attach the float element to the outer group, the first element.
   descId = c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA, 5, 0),
                       c4d.DescLevel(1, 1, 0))# первая 1 это ID вкладки
   outerFloatData[c4d.DESC_PARENTGROUP] = descId

   # Create a group element.
   innerGroupData = c4d.GetCustomDataTypeDefault(c4d.DTYPE_GROUP)
   innerGroupData[c4d.DESC_NAME] = "Inner Group"
   # Add the inner group to the outer group, the first element.
   descId = c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA, 5, 0),
                       c4d.DescLevel(1, 1, 0))
   innerGroupData[c4d.DESC_PARENTGROUP] = descId

   # A float element in the inner group.
   innerFloatData = c4d.GetCustomDataTypeDefault(c4d.DTYPE_REAL)
   innerFloatData[c4d.DESC_NAME] = "Some Float"
   innerFloatData[c4d.DESC_MIN] = -10
   innerFloatData[c4d.DESC_MAX] = 10
   innerFloatData[c4d.DESC_STEP] = 0.5
   # Attach the float element to the inner group, the third element.
   descId = c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA, 5, 0),
                       c4d.DescLevel(3, 1, 0))# тройка это ID вкладки
   innerFloatData[c4d.DESC_PARENTGROUP] = descId

   innerLONGData = c4d.GetCustomDataTypeDefault(c4d.DTYPE_LONG)
   innerLONGData[c4d.DESC_NAME] = "Long"
   innerLONGData[c4d.DESC_MIN] = -10
   innerLONGData[c4d.DESC_MAX] = 10
   innerLONGData[c4d.DESC_STEP] = 2
   descId = c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA, 5, 0),
                       c4d.DescLevel(3, 1, 0))
   innerLONGData[c4d.DESC_PARENTGROUP] = descId
   
   # Add all element, the order matters here, since we index/reference the
   # elements in the DESC_PARENTGROUP values by index, so we have reflect
   # that order here.
   outerGroupId = op.AddUserData(outerGroupData)
   outerFloatId = op.AddUserData(outerFloatData)
   innerGroupId = op.AddUserData(innerGroupData)
   innerFloatId = op.AddUserData(innerFloatData)
   innerLONGId = op.AddUserData(innerLONGData)  

   # Set the float values.
   op[outerFloatId] = 3.1415
   op[innerFloatId] = 2. * 3.1415
   op[innerLONGId] = 4
   # Update Cinema 4D
   c4d.EventAdd()

if __name__ == "__main__":
    main()