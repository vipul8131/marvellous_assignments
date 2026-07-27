import os
from pathlib import Path
import re
def ValidateDir(dir):
    if not Path(dir).is_absolute():
        return "Error: Given directory path is not full path or absolute path."
    else:
        if not os.path.isdir(dir):
            return "Error: Directory is not exists or given path is wrong."
        else:
            canRead = os.access(dir, os.R_OK)
            canWrite = os.access(dir, os.W_OK)
            if canRead == True and canWrite == True:
                return True
            else:
                return "Error: Given directory does not have access to read or write."


def ValidateEmail(email):
    EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.fullmatch(EMAIL_REGEX, email):
        return True
    else:
        return False

def ValidateInterval(intervals):
    if not int(intervals):
        return "Error: Give interval should have in int format."
    else:
        if intervals > 0:
            return True
        else:
            return False