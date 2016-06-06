import string, os
import numpy as np
import codecs
import shapefile
import shutil
import glob

f = open('colorlib.txt', 'r')
Lines = f.readlines()
f.close()
colorlib = {'0':['255','255','255']}
i=0
while i<len(Lines):
    if i < 2:
        i+=1
        continue
    else:
        newData = [ ]
        for data in Lines[i].split():
            newData.append(data)
        colorlib[newData[0]]=[newData[1],newData[2],newData[3]]
    i+=1

t00Files = glob.glob("*.t00")

# $gain is used to modify the size of text
gain = 3

for t00file in t00Files:
    print 'Processing', t00file
    w_point = shapefile.Writer(shapefile.POINT)
    w_point.field('Height')
    w_point.field('Width')
    w_point.field('Angle')
    w_point.field('fRGB')
    w_point.field('Have_Graph')
    w_point.field('Layer')
    w_point.field('Label','C','200')

    w_point_90 = shapefile.Writer(shapefile.POINT)
    w_point_90.field('Height')
    w_point_90.field('Width')
    w_point_90.field('Angle')
    w_point_90.field('fRGB')
    w_point_90.field('Have_Graph')
    w_point_90.field('Layer')
    w_point_90.field('Label','C','200')

    w_point_270 = shapefile.Writer(shapefile.POINT)
    w_point_270.field('Height')
    w_point_270.field('Width')
    w_point_270.field('Angle')
    w_point_270.field('fRGB')
    w_point_270.field('Have_Graph')
    w_point_270.field('Layer')
    w_point_270.field('Label','C','200')

    w_point_left = shapefile.Writer(shapefile.POINT)
    w_point_left.field('Height')
    w_point_left.field('Width')
    w_point_left.field('Angle')
    w_point_left.field('fRGB')
    w_point_left.field('Have_Graph')
    w_point_left.field('Layer')
    w_point_left.field('Label','C','200')

    w_point_right = shapefile.Writer(shapefile.POINT)
    w_point_right.field('Height')
    w_point_right.field('Width')
    w_point_right.field('Angle')
    w_point_right.field('fRGB')
    w_point_right.field('Have_Graph')
    w_point_right.field('Layer')
    w_point_right.field('Label','C','200')

    w_point_graph = shapefile.Writer(shapefile.POINT)
    w_point_graph.field('Graph_ID')

    w_polyline = shapefile.Writer(shapefile.POLYLINE)
    w_polyline.field('fRGB')
    w_polyline.field('Width')
    w_polyline.field('Is_Dash')
    w_polyline.field('Layer')
    w_polyline.field('AliasName')

    w_polygon = shapefile.Writer(shapefile.POLYGON)
    w_polygon.field('fRGB')
    w_polygon.field('Layer')
    w_polygon.field('AliasName')

    CurvDict = {0:['point1','point2']}

    f = open(t00file, 'r')
    Lines = f.readlines()
    f.close()
    i=0
    CurvNum=1
    GraphNum=0
    polylineNum=0
    polygonNum=0
    w_pointNum=0
    point_leftNum=0
    point_rightNum=0
    point_90Num=0
    point_270Num=0
    while i<len(Lines):
        if i < 1:
            i+=1
            continue
        else:
            newData = [ ]
            for data in Lines[i].split(','):
                newData.append(data)
            if newData[0] == "Text":
                if newData[-1].decode('gbk')[0]!='"':
                    w_point_left.point(float(newData[1]), float(newData[2]))
                    w_point_left.record(float(newData[3])*72/25.4/gain, newData[4], float(newData[5]),str(colorlib[newData[7]][0])+','+str(colorlib[newData[7]][1])+','+str(colorlib[newData[7]][2]),'false',newData[11],(newData[-2]+newData[-1]).decode('gbk').encode('gbk').replace('"','').replace('\@','\n').replace('//','/'))
                    point_leftNum+=1
                elif len(newData[-1].decode('gbk'))>50:
                    w_point_left.point(float(newData[1])-4, float(newData[2])-4)
                    w_point_left.record(float(newData[3])*72/25.4/gain, newData[4], float(newData[5]),str(colorlib[newData[7]][0])+','+str(colorlib[newData[7]][1])+','+str(colorlib[newData[7]][2]),'false',newData[11],newData[-1].decode('gbk').encode('gbk').replace('"','').replace('\@','\n'))
                    point_leftNum+=1
                elif float(newData[5]) == 90.0:
                    w_point_90.point(float(newData[1]), float(newData[2]))
                    w_point_90.record(float(newData[3])*72/25.4/gain, newData[4], float(newData[5]),str(colorlib[newData[7]][0])+','+str(colorlib[newData[7]][1])+','+str(colorlib[newData[7]][2]),'false',newData[11],newData[-1].decode('gbk').encode('gbk').replace('"','').replace('\@','\n').replace('//','/'))
                    point_90Num+=1
                elif float(newData[5]) == 270.0:
                    w_point_270.point(float(newData[1]), float(newData[2]))
                    w_point_270.record(float(newData[3])*72/25.4/gain, newData[4], float(newData[5]),str(colorlib[newData[7]][0])+','+str(colorlib[newData[7]][1])+','+str(colorlib[newData[7]][2]),'false',newData[11],newData[-1].decode('gbk').encode('gbk').replace('"','').replace('\@','\n').replace('//','/'))
                    point_270Num+=1
                elif int(newData[-2]) == 1026 or int(newData[-2]) == 2 or int(newData[-2]) == 514 or int(newData[-2]) == 258:
                    w_point_left.point(float(newData[1]), float(newData[2]))
                    w_point_left.record(float(newData[3])*72/25.4/gain, newData[4], float(newData[5]),str(colorlib[newData[7]][0])+','+str(colorlib[newData[7]][1])+','+str(colorlib[newData[7]][2]),'false',newData[11],newData[-1].decode('gbk').encode('gbk').replace('"','').replace('\@','\n').replace('//','/'))
                    point_leftNum+=1
                elif int(newData[-2]) == 1028 or int(newData[-2]) == 1030 or int(newData[-2]) == 6 or int(newData[-2]) == 518 or int(newData[-2]) == 262:
                    w_point_left.point(float(newData[1]), float(newData[2]))
                    w_point_left.record(float(newData[3])*72/25.4/gain, newData[4], float(newData[5]),str(colorlib[newData[7]][0])+','+str(colorlib[newData[7]][1])+','+str(colorlib[newData[7]][2]),'true',newData[11],newData[-1].decode('gbk').encode('gbk').replace('"','').replace('\@','\n').replace('//','/'))
                    point_leftNum+=1
                elif int(newData[-2]) == 3074 or int(newData[-2]) == 2562 or int(newData[-2]) == 2050 or int(newData[-2]) == 2306:
                    w_point.point(float(newData[1]), float(newData[2]))
                    w_point.record(float(newData[3])*72/25.4/gain, newData[4], float(newData[5]),str(colorlib[newData[7]][0])+','+str(colorlib[newData[7]][1])+','+str(colorlib[newData[7]][2]),'false',newData[11],newData[-1].decode('gbk').encode('gbk').replace('"','').replace('\@','\n').replace('//','/'))
                    w_pointNum+=1
                elif int(newData[-2]) == 3078 or int(newData[-2]) == 2566 or int(newData[-2]) == 2054 or int(newData[-2]) == 2310:
                    w_point.point(float(newData[1]), float(newData[2]))
                    w_point.record(float(newData[3])*72/25.4/gain, newData[4], float(newData[5]),str(colorlib[newData[7]][0])+','+str(colorlib[newData[7]][1])+','+str(colorlib[newData[7]][2]),'true',newData[11],newData[-1].decode('gbk').encode('gbk').replace('"','').replace('\@','\n').replace('//','/'))
                    w_pointNum+=1
                elif int(newData[-2]) == 5122 or int(newData[-2]) == 4610 or int(newData[-2]) == 4354 or int(newData[-2]) == 4098:
                    w_point_right.point(float(newData[1]), float(newData[2]))
                    w_point_right.record(float(newData[3])*72/25.4/gain, newData[4], float(newData[5]),str(colorlib[newData[7]][0])+','+str(colorlib[newData[7]][1])+','+str(colorlib[newData[7]][2]),'false',newData[11],newData[-1].decode('gbk').encode('gbk').replace('"','').replace('\@','\n').replace('//','/'))
                    point_rightNum+=1
                elif int(newData[-2]) == 5126 or int(newData[-2]) == 5124 or int(newData[-2]) == 4614 or int(newData[-2]) == 4358 or int(newData[-2]) == 4102:
                    w_point_right.point(float(newData[1]), float(newData[2]))
                    w_point_right.record(float(newData[3])*72/25.4/gain, newData[4], float(newData[5]),str(colorlib[newData[7]][0])+','+str(colorlib[newData[7]][1])+','+str(colorlib[newData[7]][2]),'true',newData[11],newData[-1].decode('gbk').encode('gbk').replace('"','').replace('\@','\n').replace('//','/'))
                    point_rightNum+=1
            elif (newData[0] == "Grap" and int(newData[-6]) == 407):
                w_point_graph.point(float(newData[1]), float(newData[2]))
                w_point_graph.record(int(newData[-6]));
                GraphNum+=1
            elif newData[0] == "Curv":
                pointNum = newData[1]
                i+=1
                startLine=i
                Points = [[ ]]
                while i<(startLine+int(pointNum)):
                    Points[0].append([float(Lines[i].split(',')[0]), float(Lines[i].split(',')[1])])
                    i+=1
                w_polyline.line(parts=Points)
                if int(newData[2]) == 2:
                    w_polyline.record(str(colorlib[newData[4]][0])+','+str(colorlib[newData[4]][1])+','+str(colorlib[newData[4]][2]),newData[6],'true',newData[9], newData[-1].decode('gbk').encode('gbk').replace('"',''))
                    polylineNum+=1
                else:
                    w_polyline.record(str(colorlib[newData[4]][0])+','+str(colorlib[newData[4]][1])+','+str(colorlib[newData[4]][2]),newData[6],'flase',newData[9], newData[-1].decode('gbk').encode('gbk').replace('"',''))
                    polylineNum+=1
                continue
            elif newData[0] == "Farc":
                pointNum = newData[1]
                i+=1
                startLine=i
                Points = [[ ]]
                while i<(startLine+int(pointNum)):
                    Points[0].append([float(Lines[i].split(',')[0]), \
                                      float(Lines[i].split(',')[1])])
                    i+=1
                CurvDict[CurvNum]=Points[0]
                CurvNum+=1
                continue
            elif newData[0] == "Fill":
                CountCurv = newData[1]
                i+=1
                startLine=i
                Points=[[ ]]
                while i<(startLine+int(CountCurv)):
                    NumCurv = int(Lines[i].split(',')[0])
                    Order = int(Lines[i].split(',')[1])
                    if Order==0:
                        Points[0]=Points[0]+CurvDict[NumCurv]
                    else:
#                        print list(reversed(CurvDict[NumCurv]))
                        Points[0]=Points[0]+list(reversed(CurvDict[NumCurv]))
                    i+=1
                w_polygon.poly(parts=Points)
                w_polygon.record(str(colorlib[newData[-7]][0])+','+str(colorlib[newData[-7]][1])+','+str(colorlib[newData[-7]][2]),newData[-5],newData[-1])
                polygonNum+=1
                continue

        i+=1

    newpath=t00file[:-4]
    if not os.path.exists(newpath): os.makedirs(newpath)
    if w_pointNum > 0:
        w_point.save(newpath+'/point')
    if point_leftNum > 0:
        w_point_left.save(newpath+'/point_left')
    if point_rightNum > 0:
        w_point_right.save(newpath+'/point_right')
    if point_90Num > 0:
        w_point_90.save(newpath+'/point_90')
    if point_270Num > 0:
        w_point_270.save(newpath+'/point_270')
    if GraphNum > 0:
        w_point_graph.save(newpath+'/point_graph')
    if polylineNum > 0:
        w_polyline.save(newpath+'/line')
    if polygonNum > 0:
        w_polygon.save(newpath+'/polygon')
    shutil.copy2('arcgis_vbscript.txt', newpath)
