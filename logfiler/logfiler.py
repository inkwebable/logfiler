import os
import time

class Log:
    def __init__(self, directory: str = '', name: str = 'logger', usedatesinfilename: bool = False):
        self.__usedatesinfilename = usedatesinfilename
        self.__directory = directory
        self.__name = name
        self.current_time = time.strftime("%H:%M:%S")
        self.osdate = time.strftime("%d_%m_%y")
        self.date = time.strftime("%d-%m-%y")
        self.init()

    def has_log_file(self):
        try:
            if self.__usedatesinfilename is True:
                if os.path.isfile(self.__directory + self.__name + "-" + self.osdate + '.txt'):
                    return True
                else:
                    return False
            else:
                if os.path.isfile(self.__directory + self.__name + '.txt'):
                    return True
                else:
                    return False
        except Exception as e:
            raise

    def __make_log_file(self):
        try:
            # if got file return it else make new one and return that
            if self.__usedatesinfilename is True:
                thelogfile = open(self.__directory + self.__name + "-" + self.osdate + '.txt', 'w+')
            else:
                thelogfile = open(self.__directory + self.__name + '.txt', 'w+')

            thelogfile.write('Created log file at ' + self.current_time + " on " + self.osdate)
            thelogfile.close()

            return thelogfile
        except Exception as e:
            print('error')
            raise

    def get_log_file(self):
        try:
            if self.__usedatesinfilename is True:
                thelogfile = open(self.__directory + self.__name + "-" + self.osdate + '.txt', 'a')
            else:
                thelogfile = open(self.__directory + self.__name + '.txt', 'a')

            return thelogfile
        except Exception as e:
            raise

    def check_path(self):
        if isinstance(self.__directory, str) and self.__directory is not '':
            if not os.path.exists(self.__directory):
                os.mkdir(self.__directory)
                print('made dir')
            else:
                print('path exists')

    # Log writing methods
    def critical(self, message: str):
        temp = self.get_log_file()
        temp.write(
            '\n' +
            self.date + ", " +
            self.current_time + ", " +
            '[CRITICAL], ' +
            str(message)
        )

        temp.close()

    def warning(self, message: str):
        temp = self.get_log_file()
        temp.write(
            '\n' +
            self.date + ", " +
            self.current_time + ", " +
            '[WARNING], ' +
            str(message)
        )

        temp.close()

    def info(self, message: str):
        temp = self.get_log_file()
        temp.write(
            '\n' +
            self.date + ", " +
            self.current_time + ", " +
            '[INFO], ' +
            str(message)
        )

        temp.close()

    def debug(self, message: str):
        temp = self.get_log_file()
        temp.write(
            '\n' +
            self.date + ", " +
            self.current_time + ", " +
            '[DEBUG], ' +
            str(message)
        )

        temp.close()

    def error(self, message: str):
        temp = self.get_log_file()
        temp.write(
            '\n' +
            self.date + ", " +
            self.current_time + ", " +
            '[ERROR], ' +
            str(message)
        )

        temp.close()

    def init(self):
        self.check_path()
        # no file , make it and state date created
        if not self.has_log_file():
            self.__make_log_file()
