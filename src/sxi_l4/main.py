from astropy.io import fits

from cyclopts import App

app = App()

@app.default
def fit(filename: str):
    try:
        file = fits.open(filename)
    except(FileNotFoundError):
        raise("Input file not found.")
    

app()