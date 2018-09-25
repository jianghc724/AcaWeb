# -*- coding: utf-8 -*-
#


class BaseError(Exception):

    def __init__(self, code, msg):
        super(BaseError, self).__init__(msg)
        self.code = code
        self.msg = msg

    def __repr__(self):
        return '[ERRCODE=%d] %s' % (self.code, self.msg)


class InputError(BaseError):

    def __init__(self, msg):
        super(InputError, self).__init__(1, msg)


class LogicError(BaseError):

    def __init__(self, msg):
        super(LogicError, self).__init__(2, msg)


class ValidateError(BaseError):

    def __init__(self, msg):
        super(ValidateError, self).__init__(3, msg)


class UncompleteError(BaseError):

    def __init__(self, msg):
        super(UncompleteError, self).__init__(4, msg)


class UserStatusError(BaseError):

    def __init__(self, msg):
        super(UncompleteError, self).__init__(5, msg)


class QueryError(BaseError):

    def __init__(self, msg):
        super(UncompleteError, self).__init__(6, msg)
