class KeyValueStorage:
    def __init__(self, file_path):
        self.data = {}
        with open(file_path) as file:
            for line in file:
                key, value = line.strip().split('=')
                try:
                    value = int(value)
                except ValueError:
                    pass
                self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def __getattr__(self, attr):
        try:
            return self.data[attr]
        except KeyError:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attr}'")

    def __setattr__(self, attr, value):
        if attr == 'data':
            super().__setattr__(attr, value)
        elif attr in self.data:
            raise AttributeError(f"Cannot set attribute '{attr}', it's already in use as a key")
        else:
            self.data[attr] = value
