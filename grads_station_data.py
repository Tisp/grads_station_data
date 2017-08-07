from ctypes import *
import struct 
import argparse

""" Representa a estrutura do struct rpthdr 
    struct rpthdr { 
        char id[8];          /* Character station id           */
        float lat;            /* Latitude of report             */
        float lon;            /* Longitude of report            */
        float t;              /* Time in relative grid units    */
        int  nlev;            /* Number of levels following     */
        int flag;             /* Level independent var set flag */
      } hdr;
"""
class ReportHeader(Structure):
    _fields_ = [('id', c_char * 8),
                ('lat', c_float),
                ('lon', c_float),
                ('t', c_float),
                ('nlev', c_int),
                ('flag', c_int)]

def write_station_data(infile, outfile, latc, lonc, stidc=None):
    hdr = ReportHeader()
    """ Read, write loop """
    ids = 1
    with open(outfile, "wb") as of :
        with open(infile, "r") as f:
            for line in f:
                line_data = line.rstrip().split()
                lat = line_data[latc]
                lon = line_data[lonc]

                hdr.lat = float(lat) 
                hdr.lon = float(lon)
                hdr.flag = 1
                hdr.nlev = 1
                hdr.t = 0.0

                if not stidc: 
                    hdr.id = str(ids) 
                    ids += 1
                else: 
                    stid = line_data[stidc]
                    hdr.id = stid[:8] #force get 8 chars
                    line_data.remove(stid) #remove from list
                                
                #remove lat and lon from list
                line_data.remove(lat)
                line_data.remove(lon)

                """ write header """
                of.write(hdr)
                
                """ write data """
                for data in line_data:
                    of.write(struct.pack('f', float(data)))

        hdr.nlev = 0
        of.write(hdr)


def main():
    parser = argparse.ArgumentParser(
        description="Station data creator for GrADS"
    )      

    parser.add_argument('--infile', '-i', action="store", required=True,
    help="Input file, station data file")

    parser.add_argument('--outfile', '-o', action="store", required=True,
    help="Output file")

    parser.add_argument('--latc', action="store",  default=1, type=int,
    help="Latitude column number [starts on 0]")

    parser.add_argument('--lonc', action="store",  default=2, type=int,
    help="Longitude column number [starts on 0]")

    parser.add_argument('--stidc', action="store", type=int,
    help="Station id column number [starts on 0]")

    args = parser.parse_args()
    parser.print_help()
    write_station_data(args.i, args.o, args.latc, args.lonc, args.stidc)

if __name__ == '__main__':
    main()


