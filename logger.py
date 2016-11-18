import os
import time


class Log:
    def __init__(self, directory: str, name: str, usedatesinfilenames: bool = False):
        self.usedatesinfilenames = usedatesinfilenames
        self.directory = directory
        self.name = name
        self.current_time = time.strftime("%H:%M:%S")
        self.osdate = time.strftime("%d_%m_%y")
        self.date = time.strftime("%d-%m-%y")
        self.init()

    def has_log_file(self):

        if self.usedatesinfilenames is True:
            if os.path.isfile(self.directory + self.name + "-" + self.osdate + '.txt'):
                return True
            else:
                return False
        else:
            if os.path.isfile(self.directory + self.name + '.txt'):
                return True
            else:
                return False

    def make_log_file(self):

        # if got file return it else make new one and return that
        if self.usedatesinfilenames is True:
            thelogfile = open(self.directory + self.name + "-" + self.osdate + '.txt', 'w+')
        else:
            thelogfile = open(self.directory + self.name + '.txt', 'w+')

        thelogfile.write('Create log file at ' + self.current_time + " on " + self.osdate)
        thelogfile.close()

        return thelogfile

    def get_log_file(self):

        if self.usedatesinfilenames is True:
            thelogfile = open(self.directory + self.name + "-" + self.osdate + '.txt', 'a')
        else:
            thelogfile = open(self.directory + self.name + '.txt', 'a')

        return thelogfile

    def init(self):
        # no file , make it and state date created
        if not self.has_log_file():
            self.make_log_file()
