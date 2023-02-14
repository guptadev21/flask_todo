import uuid

class tasks:
    def __init__(self, task):
        self.task = task
        self.completed = False

    def __str__(self):
        return f'# {self.task}'