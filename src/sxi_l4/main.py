from astropy.io import fits
from cyclopts import App

from fit import Fit

app = App()

@app.default
def fit(filename: str):
    try:
        file = fits.open(filename)
    except(FileNotFoundError):
        raise("Input file not found.")
    
    input = file[0]
    
    # call our encapsulated fitting function
    fitting = Fit()
    result = fitting.wharton2025(input)

    # and display the data
    print(result)

app()