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
            max_files_in_day: int = 0,
            start_log_from: int = 0,
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
        self.last_log_index = None
        self.current_log_name = None
        self.files = []
        self.init()

    def __combined_file_name(self):
        """
        Makes the file directory and name and returns full system string
        :return str:
        """

        # determine if the log file name needs the iteration attached to the filename
        if self.log_it_count > 0:
            if self.last_log_index is None:
                filename = self.name + '-' + str(self.start_log_from)
            else:
                filename = self.name + '-' + str(self.last_log_index + 1)
        else:
            if self.start_log_from > 0:
                filename = self.name + '-' + str(self.start_log_from)
            else:
                filename = self.name

        if self.use_dates_in_filename is True:
            if self.date_first is True:
                return os.path.join(self.directory, self.os_date + "-" + filename + '.' + self.file_ext)
            else:
                filename = filename + "-" + self.os_date + '.' + self.file_ext
                return os.path.join(self.directory, filename)
        else:
            return os.path.join(self.directory, filename + '.' + self.file_ext)

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
            self.current_log_name = self.__combined_file_name()
            # if got file return it else make new one and return that
            the_log_file = open(self.current_log_name, 'w+')
            the_log_file.write('Created log file at ' + self.current_time + " on " + self.os_date)
            the_log_file.close()

            return the_log_file
        except Exception as e:
            raise

    def _get_log_file(self):
        """
        Returns an open log file for appending to
        :return:
        """
        try:
            if self.current_log_name is None:
                the_log_file = open(self.__combined_file_name(), 'a')
            else:
                the_log_file = open(self.current_log_name, 'a')

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
                except Exception as e:
                    raise e
            else:
                return True

    def get_file_size(self):
        """
        Returns the file size in bytes
        :return int:
        """
        # print('get file size')
        try:
            if self.current_log_name is None:
                # print('current_log_name is none Checking size of ' + self.__combined_file_name())
                size = os.path.getsize(self.__combined_file_name())
            else:
                # print('Checking size of current log ' + self.current_log_name)
                size = os.path.getsize(self.current_log_name)

            return int(size)

        except Exception as e:
            raise e

    def file_size_ok(self):
        """
        Check if file size is within limit
        :return bool:
        """
        if self.size_limit > 0:
            kb = (self.get_file_size() / 1023)
            mb = kb / 1023
            if mb >= self.size_limit:
                return False

        # print('file_size_ok')
        return True

    # Log writing methods
    def writer(self, message_type='[CUSTOM]', message: str = ''):
        """
        Writes the given message type and message to the log
        :param message_type:
        :param message:
        :return:
        """

        # if last_log_index or current_log_name is none, assume self.name is current & only file
        # if it's size is not ok ( checks the original log file! )
        if self.file_size_ok() is False:
            if self.max_files_in_day > 0:
                # determine if there are other logs files besides the original
                if self.get_last_log_index() is False:
                    # only one log file
                    return False
                else:
                    # we have log files with indexes in the filename and current_log_name has be set to the most recent
                    # check file size (this now does checks with current_log_name)
                    if self.file_size_ok() is False:
                        # if size not ok and max file limit has not been reached
                        if self.max_files_in_day is not 0 and self.max_files_in_day <= self.log_it_count:
                            return False
                        else:
                            if self.max_files_in_day is 0:
                                # return false as the file has hit max limit
                                return False
                            else:
                                # at this point, last_log_index is set, current_log_name is populated
                                self.__make_log_file()
            else:
                return False

        file = self._get_log_file()

        self.current_time = time.strftime("%H:%M:%S")

        file.write(
            '\n' +
            self.date + ", " +
            self.current_time + ", " +
            message_type + ', ' +
            str(message)
        )

        file.close()

        return True

    def critical(self, message: str):
        """
        Write a [critcal] message to the log
        :param message:
        :return:
        """
        return self.writer( '[CRITICAL]', message)

    def warning(self, message: str):
        """
        Write a [warning] message to the log
        :param message:
        :return:
        """
        return self.writer('[WARNING]', message)

    def info(self, message: str):
        """
        Write an [info] message to the log
        :param message:
        :return:
        """
        return self.writer('[INFO]', message)

    def debug(self, message: str):
        """
        Write a [debug] message to the log
        :param message:
        :return:
        """
        return self.writer('[DEBUG]', message)

    def error(self, message: str):
        """
        Write an [error] message to the log
        :param message:
        :return:
        """
        return self.writer( '[ERROR]', message)

    def determine_path(self):
        """
        Gets the correct file system path based on the object directory string
        :return:
        """

        if self.directory == '':
            return os.path.dirname(os.path.abspath(__name__))
        else:
            return self.directory

    def get_last_log_index(self):
        """
        Get a list of files, iterate through them and determine log index, set current_log_name if any found
        :return:
        """

        # if we don't reset here the counting goes out the window
        self.files = []
        self.log_it_count = 0

        # self.set_log_count()
        # self.set_log_index()

        for x in os.listdir(self.determine_path()):

            if self.date_first is True:

                if re.match(r".*" + self.os_date + "-" + self.name + "." + self.file_ext, x) and not (x in self.files):
                    self.log_it_count += 1

                if re.match(r".*" + self.os_date + "-" + self.name + "-[0-9]+" + "." + self.file_ext, x) and not (x in self.files):
                    self.files.append(x)
                    nums = re.findall("[0-9]+", x)
                    self.last_log_index = int(nums[-1])
                    self.log_it_count += 1
            else:
                if re.match(r".*" + self.name + '-' + self.os_date + "." + self.file_ext, x) and not (x in self.files):
                    self.log_it_count += 1

                if re.match(r".*" + self.name + "-[0-9]+" + '-' + self.os_date + "." + self.file_ext, x) and not (x in self.files):
                    self.files.append(x)
                    nums = re.findall("[0-9]+", x)
                    self.last_log_index = int(nums[0])
                    self.log_it_count += 1

        if len(self.files) is 0:
            return False
        else:
            self.current_log_name = self.files[-1]
            return True

    def init(self):
        """
        Check for log file and create one if none found wjen object is initialised
        :return:
        """

        self.__check_path()
        # no file , make it and state date created
        if not self._has_log_file():
            self.__make_log_file()