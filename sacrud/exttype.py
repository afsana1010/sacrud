import os
from sqlalchemy.types import TypeDecorator, VARCHAR


class FileStore(TypeDecorator):
    impl = VARCHAR

    def __init__(self, path='', abspath='', *arg, **kw):
        TypeDecorator.__init__(self, *arg, **kw)
        self.path = path
        self.abspath = abspath

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = os.path.join(self.path, value)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = value
        return value
