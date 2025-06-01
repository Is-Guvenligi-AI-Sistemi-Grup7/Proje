from Core.Utilities.Interceptors import MethodInterception
from contextlib import contextmanager
import sqlite3  # or your preferred database connection

class TransactionScope:
    def __init__(self, connection=None):
        self.connection = connection
        self.is_completed = False
    
    def __enter__(self):
        if self.connection:
            self.connection.execute("BEGIN")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_type is None and self.is_completed:
                self.connection.execute("COMMIT")
            else:
                self.connection.execute("ROLLBACK")
        return False  # Don't suppress exceptions
    
    def complete(self):
        self.is_completed = True
    
    def dispose(self):
        if self.connection and not self.is_completed:
            self.connection.execute("ROLLBACK")

class TransactionScopeAspect(MethodInterception):
    def __init__(self, connection=None):
        self.connection = connection
    
    def intercept(self, invocation):
        with TransactionScope(self.connection) as transaction_scope:
            try:
                invocation.proceed()
                transaction_scope.complete()
            except Exception as e:
                transaction_scope.dispose()
                raise