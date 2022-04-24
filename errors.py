"""
Custom exceptions
"""


class InsufficientBalance(ValueError):
    def __init__(self, message="Insufficient account balance for the operation"):
        super().__init__(self.message)
