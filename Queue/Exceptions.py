class QueueOutOfRangeException(Exception):
 
    def __init__(self, message):
        self.message = message

    @property
    def msg(self):
        return self.message
