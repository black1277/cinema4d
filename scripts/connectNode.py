import c4d

from c4d.modules import graphview as gv
# https://developers.maxon.net/topic/15093/adding-ports-to-nodes/2
doc: c4d.documents.BaseDocument

def main():
    """
    """
    # Create and name the two objects.
    cubeA: c4d.BaseObject = c4d.BaseObject(c4d.Ocube)
    cubeB: c4d.BaseObject = c4d.BaseObject(c4d.Ocube)
    
    doc.InsertObject(cubeA)
    doc.InsertObject(cubeB)
    cubeA.SetName("A")
    cubeB.SetName("B")

    # Create the tag, get the node master and the root of the Xpresso graph.
    tag: c4d.BaseTag = cubeA.MakeTag(c4d.Texpresso)
    master: gv.GvNodeMaster = tag.GetNodeMaster()
    root: gv.GvNode = master.GetRoot()

    # You said that you want to "create an output port with global data for a node". That is very
    # ambivalent or not possible. You cannot create a port for arbitrary data on a GvNode. You can
    # only create ports for the parameters a node holds. In the case of an object node also the
    # parameters of the scene element it wraps. The parameters are referenced via DescIDs and in
    # case of creating ports we must be quite precise. See [2] for details on the subject.
    
    # The parameter ID for the editor visibility of an object. We will use it both for the in and
    # output port, because they both target the same parameter.
    did: c4d.DescID = c4d.DescID(
        c4d.DescLevel(c4d.ID_BASEOBJECT_VISIBILITY_EDITOR, # ID of the element.
                      c4d.DTYPE_LONG,                      # Its data type, an integer.
                      0))                                  # The creator, the correct value would be
                                                           # Ocube or cubeA.GetType(), but 0, i.e.,
                                                           # undefined also works here.

    # Create the two nodes and set the referenced objects. When setting the references we do not
    # have to be as precise as when defining ports with our IDs.
    nodeA: gv.GvNode = master.CreateNode(root, c4d.ID_OPERATOR_OBJECT)
    nodeB: gv.GvNode = master.CreateNode(root, c4d.ID_OPERATOR_OBJECT, x=200)
    nodeA[c4d.GV_OBJECT_OBJECT_ID] = cubeA
    nodeB[c4d.GV_OBJECT_OBJECT_ID] = cubeB

    # Add an input and output port.
    outPort: gv.GvPort = nodeA.AddPort(c4d.GV_PORT_OUTPUT, did, c4d.GV_PORT_FLAG_IS_VISIBLE)
    inPort: gv.GvPort = nodeB.AddPort(c4d.GV_PORT_INPUT, did, c4d.GV_PORT_FLAG_IS_VISIBLE)
    
    # And connect them.
    outPort.Connect(inPort)

    c4d.EventAdd()

if __name__ == "__main__":
    main()