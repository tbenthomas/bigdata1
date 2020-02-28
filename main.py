from src.apicall import api_call
from src.input import  get_inputs
import os

if __name__=="__main__":
    inputs = get_inputs()
    api_call(inputs)

