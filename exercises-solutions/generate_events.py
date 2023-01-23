import argparse
from detector import Detector, BackgroundSource

import numpy as np

"""
Declaration of the constant parameters.
"""
RADIUS = 30.0                   # m
ENERGY_RESOLUTION = 0.25
BACKGROUND_RATE = 10            # s^{-1}
BACKGROUND_ENERGY_SIGMA = 0.05  # MeV


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("livetime", help="Livetime in seconds of the required background sample.")
    # optional arguments start with `--`
    parser.add_argument("--background_energy", help="Background mean energy", required=False, default=10.0)
    parser.add_argument("--output_file", help="Output filename", required=False, default="background_sample.txt")
    args = parser.parse_args()

    # We now process our arguments from `args`
    T = float(args.livetime)
    background_energy_mean = float(args.background_energy)
    output_file = args.output_file

    print(f"Generating {T} s of background events with mean energy {background_energy_mean}.")

    bg = BackgroundSource(r_b = BACKGROUND_RATE, mu_Eb = background_energy_mean, sigma_Eb = BACKGROUND_ENERGY_SIGMA)
    det = Detector(R = RADIUS, delta_Erec = ENERGY_RESOLUTION, background_source = bg)

    background_sample = det.generate_background(T)

    print(f"Saving data to `{output_file}`.")
    np.save(output_file, background_sample)

if __name__ == "__main__":
    main()