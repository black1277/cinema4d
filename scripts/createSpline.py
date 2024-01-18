import c4d
z = 0

def createSpline(name, type):
    spline = c4d.SplineObject(4, type)
    spline.SetPoint(0, c4d.Vector(0, 0, z))
    spline.SetPoint(1, c4d.Vector(100, 0, z))
    spline.SetPoint(2, c4d.Vector(100, 100, z))
    spline.SetPoint(3, c4d.Vector(0, 100, z))
    z = z + 50
    spline.SetName(name)
    doc.InsertObject(spline)
    spline.Message(c4d.MSG_UPDATE)

def main():

    # Get the spline object from the document
    spline = doc.SearchObject("spline")
    if spline == None:
        createSpline("SPLINETYPE_LINEAR", c4d.SPLINETYPE_LINEAR)
        createSpline("SPLINETYPE_CUBIC", c4d.SPLINETYPE_CUBIC)
        createSpline("SPLINETYPE_AKIMA", c4d.SPLINETYPE_AKIMA)
        createSpline("SPLINETYPE_BSPLINE", c4d.SPLINETYPE_BSPLINE)
        createSpline("SPLINETYPE_BEZIER", c4d.SPLINETYPE_BEZIER)
        c4d.EventAdd()
        return
    #SPLINETYPE_LINEAR Linear 0
    #SPLINETYPE_CUBIC Cubic   1
    #SPLINETYPE_AKIMA Akima   2
    #SPLINETYPE_BSPLINE B-Spline 3
    #SPLINETYPE_BEZIER Bezier 4

    interp = spline.GetInterpolationType()
    print('InterpolationType:',interp)

    closed = spline.IsClosed()
    print('IsClosed:',closed)

    Scount = spline.GetSegmentCount()
    print('SegmentCount:',Scount)

    Spoint = spline.GetSplinePoint(0,0)
    print('SplinePoint 0:', Spoint)
    if Scount > 0:
        # возвращает касательную третьего сегмента в позиции 1  (0 < t < 1)
        Tgpoint1  = spline.GetSplineTangent(1,2)
        print('SplineTangent 0:', Tgpoint1)
    Tgpoint1  = spline.GetSplineTangent(0,0)
    print('SplineTangent 0:', Tgpoint1)
    Spoint = spline.GetSplinePoint(.5,0)
    print('SplinePoint 1:', Spoint)
    print('All vector:', spline.GetAllPoints())
    print('PointCount:', spline.GetPointCount())

if __name__=='__main__':
    main()