import numpy as np

class BackgroundSource:
    """
    Class representing a background source for the detector.
    """
    def __init__(self, r_b : float, mu_Eb : float, sigma_Eb: float):
        self.r_b = r_b
        self.mu_Eb = mu_Eb
        self.sigma_Eb = sigma_Eb
        self.rng = np.random.default_rng()

    def generate_sample_size(self, T : float):
        """
        Generates the number of events for a background event sample of duration T.
        The number of event is a Poisson-distributed variable with mean r_b * T.
        """
        return self.rng.poisson(self.r_b * T)

    def generate_true_energy(self, n : int):
        """
        Generates 
        """
        return self.rng.normal(self.mu_Eb, self.sigma_Eb, n)

class Detector:
    """
    To use a numpy structured array in generate_background(), we need to define a numpy data type. In practice, we need to declare a list of fields and their type. Remember that a numpy array has a statically-defined memory allocation. We specify all fields as float variables (f) using 32 bits (4 bytes) but since we may want the maximum possible precision for time, we will reserve 64 bits (8 bytes).
    """
    event_dtype = np.dtype([
            ('x', 'f4'),
            ('y', 'f4'),
            ('z', 'f4'),
            ('d_x', 'f4'),
            ('d_y', 'f4'),
            ('d_z', 'f4'),
            ('t', 'f8'),
            ('E_true', 'f4'),
            ('E_rec', 'f4')
    ])      

    def __init__(self, R : float, delta_Erec: float, background_source : BackgroundSource):
        self.R = R
        self.delta_Erec = delta_Erec
        self.bg = background_source
        self.rng = np.random.default_rng()


    def generate_background(self, T : int):
        # determine the number of events in the sample
        n_ev = self.bg.generate_sample_size(T)

        # pre-allocate the numpy array
        data = np.zeros(shape=n_ev, dtype=self.event_dtype)

        """
        We need to generate coordinates within a spherical volume, this means that while x, y, z can each go up to R, the distance from the centre of the volume must be always <= R. There are different ways to achieve this, one is to sample random positions with each coordinate in [0,R] and keep only the values for which the distance from the centre is <= R.

        We could generate events one by one to fill our `data` array, but this can become very inefficient. We will try to use numpy as much as possible to perform batch calculations.
        """
        i = 0 # index up to which `data` is full
        while(i < n_ev - 1):
            n_dim = 3 # generating coordinates in three dimensions
            sample = np.random.uniform(low=-self.R, high=self.R, size=(n_ev, n_dim))
            # event axis: 0, coordinate axis: 1
            # we calculate the norm along axis 1 (coordinates) to get the radius
            valid_elements = np.linalg.norm(sample, axis=1) < self.R
            filtered_sample = sample[valid_elements]
            # now we determine how many events to read from `sample` and write to `data`
            m = (n_ev - 1) - i # number of events to fill in `data`
            n = filtered_sample.shape[0] # number of events in `sample`
            data['x'][i:i+min(m,n)] = filtered_sample[0:min(m,n),0]
            data['y'][i:i+min(m,n)] = filtered_sample[0:min(m,n),1]
            data['z'][i:i+min(m,n)] = filtered_sample[0:min(m,n),2]
            i += min(m,n)
            
        for q in ['d_x', 'd_y', 'd_z']:
            data[q] = self.rng.uniform(low=-1.0, high=1.0, size=n_ev)

        data['E_true'] = self.bg.generate_true_energy(n_ev)

        # the reconstructed energies are sampled from a normal distribution which is dependent on E_true
        # numpy makes this easy, as we can just pass the mean and stdev in the form of arrays
        mu, sigma = data['E_true'], self.delta_Erec * data['E_true']
        data['E_rec'] = self.rng.normal(loc=mu, scale=sigma)
        

        data['t'] = self.rng.uniform(low=0.0, high=T, size=n_ev)

        # let's be kind to the user and sort the data in time!
        data.sort(order='t')

        return data