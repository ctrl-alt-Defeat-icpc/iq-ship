import iqs.config as config
from iqs.file.handler import run as file_runner
from iqs.utils import os, sys

def checkExistence(srcdir, desdir):
    if not os.path.exists(srcdir):
        sys.exit(f'{srcdir} not found!')
    if not os.path.exists(desdir):
        sys.exit(f'{desdir} not found!')

def checkFormatVersion(x, y):
    if 0 <= x and x <= config.VERSIONS_THRESHOLD and 0 <= y and y <= config.VERSIONS_THRESHOLD:
        return True
    sys.exit('versions are invalid!')

def main():
    srcdir = input('Enter soruce directory (src default): ').strip() or config.DEFAULT_SRC_DIR
    desdir = input('Enter destination directory (des default): ').strip() or config.DEFAULT_DES_DIR
    src_format_version = int(input(f'Enter version of srouce format ({config.DEFAULT_SRC_FORMAT_VERSION} default): ').strip() or config.DEFAULT_SRC_FORMAT_VERSION)
    des_format_version = int(input(f'Enter version of destination format ({config.DEFAULT_DES_FORMAT_VERSION} default): ').strip() or config.DEFAULT_DES_FORMAT_VERSION)

    checkExistence(srcdir, desdir)
    checkFormatVersion(src_format_version, des_format_version)

    details = {
        'srcdir': srcdir,
        'desdir': desdir,
        'srcver': src_format_version,
        'desver': des_format_version
    }

    file_runner(details)

if __name__ == "__main__":
    main()