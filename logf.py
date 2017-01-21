# function decorators for logging function calls

import logging

class logF(object):
    def __init__(self, logLevel=logging.DEBUG, onEntry=True, onExit=True):
        self.logLevel = logLevel
        self.onEntry = onEntry
        self.onExit = onExit

    def _log_entry(self, funcName, funcArgs, funcKwargs):
        msg = "Entering function %s(args=%s, kwargs=%s)" % (funcName, str(funcArgs), str(funcKwargs))
        logging.log(self.logLevel, msg)

    def _log_exit(self, func_name):
        msg = "Leaving function %s" % func_name
        logging.log(self.logLevel, msg)

    def __call__(self, f):
        def wrapped_f(*args, **kwargs):
            func_name = f.func_name
            if self.onEntry:
                self._log_entry(func_name, args, kwargs)
            f(*args, **kwargs)
            if self.onExit:
                self._log_exit(func_name)
        return wrapped_f

