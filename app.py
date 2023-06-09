import time
from fastapi import FastAPI
from hello import sum_xy

import logging

from data_models import SamplePostRequest

app = FastAPI()

log_format = "[%(name)s][%(levelname)-6s] %(message)s"
logging.basicConfig(format=log_format)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@app.get("/")
def home():
    return "Another hello"

@app.get("/sum/{c}")
def sum_xy_endpoint(c:str, a: int, b: int):
    logger.info("Recievevd request.")

    try:
        unknown_function(c)
    except Exception:
        logger.error("Can't find `unknown_function`")
    start_time = time.time()
    output = c + " " + str(sum_xy(a, b))
    end_time = time.time()
    total_time = end_time - start_time

    logger.info(f"The processing took {total_time}s")
    
    logger.debug(f"Debug: Recieved {c=}, {a=}, {b=}")
    return output

@app.post("/predict")
def predict(request: SamplePostRequest):

    return [request.a + request.c[0]]

@app.get("/predict")
def predict():
    return "From predict function get"

@app.get("/health")
def health_check():
    return "OK"
