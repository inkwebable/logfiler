import logfiler.logfiler as logfiler
import os

# create a log instance
# if you omit the params then it will create the log file in the directory the script is run from
logFile = logfiler.Log(name='testing', directory='logs', date_first=False)

# write to it with a custom message type
logFile.writer(message_type='[EQUIPPED]',message='Like a ninja!')
logFile.writer(message='Like a ninja 2!')

# logFile5 = logfiler.Log(name='11', directory='logs', size_limit=1, date_first=False)

# create another log instance with size limitation in MB and a limited numer of files to create
log2 = logfiler.Log(directory=os.getcwd() + '\\logs\\', size_limit=1, max_files_in_day=2, use_dates_in_filename=False)

# write to it
log2.warning('Water needed!')
log2.critical('Food needed!')
log2.error('No energy')
log2.debug('Missing resource')
log2.info('Refueling')

# add counter to log files, reversed date format, ascertain if write was successful
log3 = logfiler.Log(directory='',
                    name='move',
                    log_date_format='%y-%m-%d',
                    file_ext='log',
                    use_dates_in_filename=True,
                    size_limit=1,
                    max_files_in_day=3,
                    start_log_from=1
                    )

for i in range(1,50000):
    if log3.info('Refueling ' + str(i)) is False:
        print('max file limit reached')
        exit()

