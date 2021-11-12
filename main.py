import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from qkdsimulationprotocol import QKDSimulationProtocol


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/qkd/")
def qkd_protocol_run(
    initial_key_length: int,
    eavesdropping_rate: float,
    error_estimation_sampling_rate: float,
    error_reconciliation_efficiency: float
):

    qkd_protocol = QKDSimulationProtocol(initial_key_length, eavesdropping_rate, error_estimation_sampling_rate, error_reconciliation_efficiency)
    qkd_protocol.run()
    qkd_protocol.print_summary()

    return JSONResponse(content=json.loads(qkd_protocol.output()))
