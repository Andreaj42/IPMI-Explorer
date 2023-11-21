import os
from dotenv import load_dotenv

load_dotenv()

def load_variables(var : str):
    if var in os.environ:
        variable = os.environ[var]
        return variable

    raise RuntimeError(f'Please, define var : {var}')