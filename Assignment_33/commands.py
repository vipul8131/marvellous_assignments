def Help():
    print("Duplicate File Removal Automation\n")
    print("This script scans a directory, identifies duplicate files using checksums , deletes duplicate files, creates a log file, and sends the log file through email.\n")
    print("Usage:\n")
    print("python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>\n")

def Usage():
    print("Usage :\n")
    print("python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>\n")