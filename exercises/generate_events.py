import argparse
# IMPORT YOUR MODULE!

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

    ### YOUR CODE HERE ###

    print(f"Saving data to `{output_file}`.")

if __name__ == "__main__":
    main()