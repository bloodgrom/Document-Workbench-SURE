#!c:\users\anton\desktop\dissertation\pythonwebapp\django_project\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pdfplumber==0.6.0','console_scripts','pdfplumber'
__requires__ = 'pdfplumber==0.6.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pdfplumber==0.6.0', 'console_scripts', 'pdfplumber')()
    )
