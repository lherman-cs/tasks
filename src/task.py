class Task:
    def __init__(self, task, completion=0):
        self.task = task
        self.completion = completion

    def get_info(self):
        return "{} - {}%".format(self.task, self.completion)
