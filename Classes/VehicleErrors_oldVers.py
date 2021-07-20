class VehicleError(ValueError):

    def __init__(self, err):
        self.err = err

    def __str__(self):
        if self.err == 'Already started':
            return 'Engine already started'
        elif self.err == 'Already stopped':
            return 'Engine already stopped'
        elif self.err == 'Overflow tank':
            return 'Overflow tank'
        elif self.err == 'Engine not running':
            return 'Movement not possible, engine not running'
        elif self.err == 'The tank is empty':
            return 'Movement not possible, the tank is empty'
        return 'Unknown error'
