import os
import time


class Log:
    def __init__(self, file_ext: str = 'txt', filename_date_format: str = '%d-%m-%y', log_date_format: str = '%d-%m-%y',
                 directory: str = '', name: str = 'logger', use_dates_in_filename: bool = False):
        self.__use_dates_in_filename = use_dates_in_filename
        self.__directory = directory
        self.__name = name
        self.__file_ext = file_ext
        self.__filename_date_format = filename_date_format
        self.__log_date_format = log_date_format
        self.current_time = time.strftime("%H:%M:%S")
        self.os_date = time.strftime(filename_date_format)
        self.date = time.strftime(log_date_format)
        self.init()

    def has_log_file(self):
        try:
            if self.__use_dates_in_filename is True:
                if os.path.isfile(self.__directory + self.__name + "-" + self.os_date + '.' + self.__file_ext):
                    return True
                else:
                    return False
            else:
                if os.path.isfile(self.__directory + self.__name + '.' + self.__file_ext):
                    return True
                else:
                    return False
        except Exception as e:
            raise

    def __make_log_file(self):
        try:
            # if got file return it else make new one and return that
            if self.__use_dates_in_filename is True:
                the_log_file = open(self.__directory + self.__name + "-" + self.os_date + '.' + self.__file_ext, 'w+')
            else:
                the_log_file = open(self.__directory + self.__name + '.' + self.__file_ext, 'w+')

            the_log_file.write('Created log file at ' + self.current_time + " on " + self.os_date)
            the_log_file.close()

            return the_log_file
        except Exception as e:
            print('error')
            raise

    def get_log_file(self):
        try:
            if self.__use_dates_in_filename is True:
                the_log_file = open(self.__directory + self.__name + "-" + self.os_date + '.' + self.__file_ext, 'a')
            else:
                the_log_file = open(self.__directory + self.__name + '.txt', 'a')

            return the_log_file
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
