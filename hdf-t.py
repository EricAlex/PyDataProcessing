from pyhdf.SD import *
import glob

hdfFiles = glob.glob("*.hdf")
names = ['EV_1KM_Emissive','EV_1KM_RefSB','EV_250_Aggr1km_RefSB','EV_500_Aggr1km_RefSB','Latitude','Longitude','SolarZenith']
subnames = {
    'EV_1KM_Emissive':'_Emi1km.txt',
    'EV_1KM_RefSB':'_Ref1km.txt',
    'EV_250_Aggr1km_RefSB':'_Ref250.txt',
    'EV_500_Aggr1km_RefSB':'_Ref500.txt',
    'Latitude':'_latit.txt',
    'Longitude':'_longi.txt',
    'SolarZenith':'_SolarZenith.txt'
}

for hdffile in hdfFiles:
    try:
        # Open HDF file
        f = SD(hdffile)
        print 'Processing', hdffile
        for name in names:
            newFile = open(hdffile[:-4]+subnames[name], "w")
            print '\tWriting', hdffile[:-4]+subnames[name]
            # Get dataset instance
            ds = f.select(name)
            data = ds.get()
            t = data.shape
            for i in range(len(t)):
                print >> newFile, "dimension", i
                print >> newFile, t[i]
            data.tofile(newFile,'\n')
            newFile.close()


    except HDF4Error as msg:
        print("HDF4Error", msg)