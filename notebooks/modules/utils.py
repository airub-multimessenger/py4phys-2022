import numpy as np

DEFAULT_SEED = 0

class RNG:
    def __init__(self, seed : int = DEFAULT_SEED):
        # we no longer use np.random as an "external" entity provided by the numpy module
        self.rng = np.random.default_rng(seed=seed)

    def generate(self, shape : tuple = None):
        if shape is not None:
            return self.rng.random(shape)
        else:
            return self.rng.random()