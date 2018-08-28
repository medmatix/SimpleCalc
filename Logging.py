'''
Created on Aug 25, 2018

@author: david
'''

# ==========================
# imports 
# ==========================

from os import path, makedirs
import time
from datetime import datetime



class LogLevel:
    '''Define logging levels.'''
    OFF = 0
    MINIMUM = 1
    NORMAL = 2
    DEBUG = 3

class Logger:
    ''' Create a test log and write to it. '''
    #-------------------------------------------------------
    def __init__(self, fullTestName, loglevel=LogLevel.MINIMUM):
        testName = path.splitext(path.basename(fullTestName))[0]
        logName = testName + '.log'
        logsFolder = 'logs'
        if not path.exists(logsFolder):
            makedirs(logsFolder, exist_ok = True)
        self.log = path.join(logsFolder, logName)
        self.createLog()
        self.loggingLevel = loglevel
        print("initial loglevel = " + str(loglevel))
        self.startTime = time.perf_counter()
            
    #------------------------------------------------------
    def createLog(self):
        with open(self.log, mode='w', encoding='utf-8') as logFile:
            logFile.write(str(datetime.now()) + '\t\t*** Starting Test ***\n')
        logFile.close()
    
    def writeToLog(self, msg, loglevel=LogLevel.MINIMUM):
        # control how much gets logged
        print("writeLog loglevel = " + str(loglevel))
        if loglevel > self.loggingLevel:
            return
        # open log file in append mode
        with open(self.log, mode='a', encoding='utf-8') as logFile:
            msg = str(msg)
            if msg.startswith('\n'):
                msg = msg[1:]
            logFile.write(str(datetime.now()) + '\t\t' + msg + '\n')
            logFile.close()  