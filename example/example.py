import logfiler.logfiler as logfiler
import os

# create a log instance
# if you omit the params then it will create the logger.txt file in the directory the script is run from
log = logfiler.Log(directory='', name='testing', usedatesinfilename=True)

# get the log file for writing to
logFile = log.get_log_file()

# write to it
logFile.write(
    '\n' +
    log.date + " - " +
    log.current_time +
    ' Hello World! '
)

# close it
logFile.close()

# create a log instance
log2 = logfiler.Log(directory=os.getcwd() + '\\test\\')

# write to it
log2.warning('Water needed!')
log2.critical('Food needed!')
log2.error('No energy')
log2.debug('Missing resource')
log2.info('Refueling')
