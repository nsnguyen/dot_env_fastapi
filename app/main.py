import os

from dotenv import load_dotenv

from typing import Union

from fastapi import FastAPI

load_dotenv()

app = FastAPI()

here = os.getenv('location')

cool_dude = os.getenv('cool_dude')

@app.get("/")
def read_root():
    return {"Hello": here}

@app.get("/cool_dude")
def read_root():
    return {"Hello": cool_dude}
   

