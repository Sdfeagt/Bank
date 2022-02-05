import random


def get_poll():
    res = []
    x = 10000
    y = 99999

    while x < y:
        res.append(x)
        x = x + 1
    return res


poll = get_poll()


def get_newID():
    new_ID = random.choice(poll)
    poll.remove(new_ID)
    return new_ID


class Customer:
    def __init__(self, name):
        self.name = name
        self.ID = get_newID()

    def get_id(self):
        return self.ID

    def get_name(self):
        return self.name
