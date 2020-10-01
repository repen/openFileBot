import configparser, time, re, os
from tools import log as lo, listdir_fullpath

config = configparser.ConfigParser()
config.read('setting.conf')

args = config['site']

#load config
PATH_DIR = args['dir']
TIMEOUT01 = float( args['timeout01'] )
OUTPUT = args['output']

log = lo( "openFileBot", "main.log")


def script_files():

    files = listdir_fullpath(PATH_DIR)
    log.info("Load files:\n%s", "\n".join(files))


    files = sorted(files, key= lambda x :  os.path.basename(x)  )
    files = list( filter( lambda x : re.search(r"\.txt", x), files) )
    log.info("Sorted and Filter files:\n%s", "\n".join(files))

    if not files:
        log.info("No files")
        return -1

    values = []
    for file in files:
        with open(file) as f:
            data = f.read()
        data = data.strip()
        if not data:
            values.append( "0;0;0;0;0" )
        else:
            values.append( data )
    string = ";".join(values)
    log.info("Join values: %s", string)
    with open(OUTPUT, "w") as f:
        f.write( string )
    log.info("Save %s", OUTPUT)

while True:
    script_files()
    log.info("======= Sleep {} =======".format(TIMEOUT01))
    time.sleep( TIMEOUT01 )