import datetime as date


class Block(object):

    def __init__(self, data, previous_hash, index):
        object.__setattr__(self, "index", index)
        object.__setattr__(self, "timestamp", date.datetime.now())
        object.__setattr__(self, "data", data)
        object.__setattr__(self, "previous_hash", previous_hash)
        object.__setattr__(self, "hash", self.__hash__())

    def __setattr__(self, *args):
        raise NotImplementedError(
            "This is not allowed. Block attributes cannot be edited.")

    def __delattr__(self, *args):
        raise NotImplementedError(
            "This is not allowed. Block attributes cannot be deleted.")
