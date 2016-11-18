
import logger

# create a log instance
log = logger.Log('', 'test', True)

# get it for writing
logFile = log.get_log_file()

# write to it
logFile.write(
    '\n' +
    log.date + " - " +
    log.current_time +
    ' Could not find destination '
)

# close it
logFile.close()
