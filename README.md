# logfiler
My first Python 3 venture, create named logs in a given directory, with a given name and write to them

## Install ##
To install via PIP
```
pip install git+git://github.com/inkwebable/logfiler.git
```

## Basic Usage ##

```
from logfiler.logfiler import Log
```

Create object from Log class
```logFile = Log()```

By default the log file will use the extension 'log' and have dates at the beginning of the file name

Logger has quite a few default parameters, they can be overwritten by defining them in the instance.
```
logFile = Log( directory='/var/log/myapp/', name='log-test', size_limit=1)
```

**NOTE:** _size_limit expects value in MB_

Methods for writing to the log
``` Python
logFile.warning('Water needed!')
logFile.critical('Food needed!')
logFile.error('No energy')
logFile.debug('Missing resource')
logFile.info('Refueling')
logFile.writer(message_type='[EQUIPPED]',message='Like a ninja!')
logFile.writer(message='Like a ninja 2!')
```

Sample of output from code above;
```
18-11-16, 15:01:28, [WARNING], Water needed!
18-11-16, 15:01:28, [CRITICAL], Food needed!
18-11-16, 15:01:28, [ERROR], No energy
18-11-16, 15:01:28, [DEBUG], Missing resource
18-11-16, 15:01:28, [INFO], Refueling
18-11-16, 15:01:28, [EQUIPPED], Like a ninja!
18-11-16, 15:01:28, [CUSTOM], Like a ninja 2!
```

Default parameters are below.  Please see the example.py file for further example usage.

```
filename_date_format: str = '%d-%m-%y',
log_date_format: str = '%d-%m-%y',
directory: str = '',
name: str = 'log',
use_dates_in_filename: bool = True,
size_limit: int = 0,
max_files_in_day: int = 0,
start_log_from: int = 0,
date_first: bool = True
```


***Please Note this project is W.I.P & is inteded for use with Python 3***
