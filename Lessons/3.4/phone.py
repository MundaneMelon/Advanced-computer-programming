"""
Definition of Phone class.
"""

class Phone:
    def __init__(self, model, storage, megapixels):
        self._model = model
        self._storage = storage
        self._megapixels = megapixels

    def get_mode1(self):
        return self._model

    def set_mode1(self, new_mode1):
        self._model = new_mode1