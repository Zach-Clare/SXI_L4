from astropy.io import fits
from cyclopts import App

from sxi_l4.fit import Fit

app = App()

@app.default
def help():
    help_str = """Use the following commands:
    fit: Creates and saves a result of a fitted image. Requires string argument of input FITS file location."""
    print(help_str)

@app.command
def fit(filename: str):
    try:
        file = fits.open(filename)
    except(FileNotFoundError) as e:
        raise FileNotFoundError(e, "Input file not found.")
    
    input = file[0]
    
    # call our encapsulated fitting function
    fitting = Fit()
    result = fitting.wharton2025(input)

    # and display the data
    print(result)

if __name__ == "__main__":
    app()