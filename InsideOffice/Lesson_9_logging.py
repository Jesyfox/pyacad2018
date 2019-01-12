import sys
import logging
import logging.config

LOGGING = {
   'version': 1,
   'disable_existing_loggers': True,
   'formatters': {
       'verbose': {
           'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
       },
       'simple': {
           'format': '%(levelname)s %(message)s'
       },
   },
   'handlers': {
       'null': {
           'level': 'DEBUG',
           'class': 'logging.NullHandler',
       },
       'console': {
           'level': 'DEBUG',
           'class': 'logging.StreamHandler',
           'formatter': 'verbose'
       },
       'consoleError': {
           'level': 'ERROR',
           'class': 'logging.StreamHandler',
           'formatter': 'simple'
       }
   },
   'loggers': {
       'A': {
           'handlers': ['null'],
           'propagate': True,
           'level': 'INFO',
       },
       'A.B': {
           'handlers': ['consoleError'],
           'level': 'DEBUG',
           'propagate': False,
       },
       'A.B.X': {
           'handlers': ['console'],
           'level': 'DEBUG',
           'propagate': True,
       },
       'C': {
           'handlers': ['console'],
           'level': 'INFO'
       }
   }
}


logging.config.dictConfig(LOGGING)

A = logging.getLogger('A')
AB = logging.getLogger('A.B')
ABX = logging.getLogger('A.B.X')
C = logging.getLogger('C')

A.error('A_asdasddasdasdasdas')
AB.error('AB_asdasddasdasdasdas')
ABX.error('ABX_asdasddasdasdasdas')
C.error('C_asdasddasdasdasdas')