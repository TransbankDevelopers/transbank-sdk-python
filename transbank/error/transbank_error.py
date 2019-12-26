class TransbankError(Exception):
    def __init__(self, message = "An error has happened, verify given parameters and try again.", code = 0):
        super()
        self.message = message
        self.code = code

    def __repr__(self):
        return "message: {}, code: {}".format(self.message, self.code)
