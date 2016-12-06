import os
import time
import re


class Log:
    def __init__(
            self, file_ext: str = 'log',
            filename_date_format: str = '%d-%m-%y',
            log_date_format: str = '%d-%m-%y',
            directory: str = '',
            name: str = 'log',
            use_dates_in_filename: bool = True,
            size_limit: int = 0,
            max_files_in_day: int = 100,
            start_log_from: int = 2,
            date_first: bool = True
    ):
        self.use_dates_in_filename = use_dates_in_filename
        self.directory = directory
        self.name = name
        self.file_ext = file_ext
        self.filename_date_format = filename_date_format
        self.log_date_format = log_date_format
        self.current_time = time.strftime("%H:%M:%S")
        self.os_date = time.strftime(filename_date_format)
        self.date = time.strftime(log_date_format)
        self.size_limit = size_limit
        self.max_files_in_day = max_files_in_day
        self.start_log_from = start_log_from
        self.log_it_count = 0
        self.date_first = date_first
        self.init()

    def __combined_file_name(self):
        """
        Makes the file directory and name
        :return:
        """
        if self.date_first is True:
            if self.use_dates_in_filename is True:
                return self.directory + self.os_date + "-" + self.name + '.' + self.file_ext
            else:
                return self.directory + self.name + '.' + self.file_ext
        else:
            if self.use_dates_in_filename is True:
                return self.directory + self.name + "-" + self.os_date + '.' + self.file_ext
            else:
                return self.directory + self.name + '.' + self.file_ext

    def _has_log_file(self):
        """
        Checks for log file
        :return bool:
        """
        try:
            if os.path.isfile(self.__combined_file_name()):
                return True
            else:
                return False

        except Exception as e:
            raise

    def __make_log_file(self):
        """
        Writes a log file to directory stored in the object
        :return:
        """
        try:
            # if got file return it else make new one and return that
            the_log_file = open(self.__combined_file_name(), 'w+')
            the_log_file.write('Created log file at ' + self.current_time + " on " + self.os_date)
            the_log_file.close()

            return the_log_file
        except Exception as e:
            print('error')
            raise

    def get_log_file(self):
        """
        Gets the log file
        :return:
        """
        try:
            the_log_file = open(self.__combined_file_name(), 'a')

            return the_log_file
        except Exception as e:
            raise

    def __check_path(self):
        """
        Check if directory path exists returns true or creates it if dir does not exist
        :return:
        """
        if isinstance(self.directory, str) and self.directory is not '':
            if not os.path.exists(self.directory):
                try:
                    os.mkdir(self.directory)
                    print('made dir')
                except Exception as e:
                    raise e
            else:
                print('path exists')
                return True

    def get_file_size(self):
        """
        Returns the file size in bytes
        :return int:
        """
        try:
            size = os.path.getsize(self.__combined_file_name())

            return int(size)

        except Exception as e:
            raise e

    def file_size_ok(self):
        """
        Check if file size is within limit
        :return bool:
        """
        if self.size_limit > 0:
            kb = (self.get_file_size() / 1024)
            mb = kb / 1024
            if mb >= self.size_limit:
                return False

        # print('file_size_ok no answer')
        return True

    # Log writing methods
    def writer(self, file, message_type, message: str):
        """
        Writes the given messafe type to the log
        :param file:
        :param message_type:
        :param message:
        :return:
        """
        file.write(
            '\n' +
            self.date + ", " +
            self.current_time + ", " +
            message_type + ', ' +
            str(message)
        )

        file.close()

    def critical(self, message: str):
        """
        Write a [critcal] message to the log
        :param message:
        :return:
        """
        if self.file_size_ok() is False:
            self.make_new_file()

        temp = self.get_log_file()
        self.writer(temp, '[CRITICAL]', message)

    def warning(self, message: str):
        """
        Write a [warning] message to the log
        :param message:
        :return:
        """
        if self.file_size_ok() is False:
            self.make_new_file()

        temp = self.get_log_file()
        self.writer(temp, '[WARNING]', message)

    def info(self, message: str):
        """
        Write an [info] message to the log
        :param message:
        :return:
        """
        if self.file_size_ok() is False:
            self.make_new_file()

        temp = self.get_log_file()
        self.writer(temp, '[INFO]', message)

    def debug(self, message: str):
        """
        Write a [debug] message to the log
        :param message:
        :return:
        """
        if self.file_size_ok() is False:
            self.make_new_file()

        temp = self.get_log_file()
        self.writer(temp, '[DEBUG]', message)

    def error(self, message: str):
        """
        Write an [error] message to the log
        :param message:
        :return:
        """
        if self.file_size_ok() is False:
            self.make_new_file()

        temp = self.get_log_file()
        self.writer(temp, '[ERROR]', message)

    def make_new_file(self):
        """
        Makes a new log file, numbered based on existing logs
        :return:
        """

        # get original file name, no numbers
        original_name_list = re.findall("[^0-9]", self.name)

        # get log number - empty unless more than 1 log file
        # original_nums_list = re.findall("[0-9]+", self.name)

        if not self._has_log_file():
            self.__make_log_file()
        else:
            # remove last hyphen from name
            if original_name_list[len(original_name_list) - 1] == '-':
                del original_name_list[-1]

            # join the list to get the original file name ( note, if user used numbers in filename, name will be wrong )
            original_name = "".join(original_name_list)

            if self.log_it_count > 0:
                iterator_start = self.log_it_count
            else:
                iterator_start = self.start_log_from

            for i in range(iterator_start, (self.max_files_in_day + 1)):
                self.name = original_name + '-' + str(i)
                # look for an existing log file
                if self._has_log_file() is True:
                    # check it's size
                    if self.file_size_ok() is True:
                        # we have a file to write to, end loop
                        break
                else:
                    # set the range start count
                    self.log_it_count = i
                    # make new log file
                    self.__make_log_file()
                    break

                if self.max_files_in_day == i:
                    raise ValueError('max log files limit reached for the day!')

    def init(self):
        self.__check_path()
        # no file , make it and state date created
        if not self._has_log_file():
            self.make_new_file()
