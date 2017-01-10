
import xml.etree.ElementTree as ET
from zipfile import ZipFile


def is_twb_filename(filename):
    return filename.endswith('.twb')


def is_tds_filename(filename):
    return filename.endswith('.tds')


def is_tde_filename(filename):
    return filename.endswith('.tde')


def handle_twb_file(filename, fd):
    # tableau work book
    root = ET.fromstring(fd.read())
    print(ET.dump(root))


def handle_tds_file(filename, fd):
    # tableau data source
    root = ET.fromstring(fd.read())
    print(ET.dump(root))


def handle_tde_file(filename, fd):
    # tableau data extract
    pass


if __name__ == '__main__':

    import sys

    if len(sys.argv) < 2:
        print('Usage: {} path/to/workbook.twbx'.format(sys.argv[0]))
        sys.exit(1)

    with ZipFile(sys.argv[1], 'r') as z:
        print(dir(z))
        print(z.filelist)
        for x in z.filelist:
            if is_twb_filename(x.filename):
                handle_twb_file(x.filename, z.open(x.filename))
            elif is_tds_filename(x.filename):
                handle_tds_file(x.filename, z.open(x.filename))
            elif is_tde_filename(x.filename):
                handle_tde_file(x.filename, z.open(x.filename))
