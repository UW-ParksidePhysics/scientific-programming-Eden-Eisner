import numpy as np

def read_two_columns_text(filename: str):
    try:
        # Read the data from the file and ensure it has two columns
        data = np.loadtxt(filename).T  # Transpose to get the shape (2, M)
        if data.shape[0] != 2:
            raise ValueError("The file does not have exactly two columns of data.")
        return data
    except OSError:
        raise OSError(f"Could not open or find the file: {filename}")
    except ValueError as e:
        raise ValueError(str(e))
