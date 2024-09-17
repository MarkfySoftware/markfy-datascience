import pickle
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_cluster():
    with open('models/customer-segment.pkl', 'rb') as file:
        model = pickle.load(file=file)
    return model


customer_segment = load_cluster()

@app.get("/")
def read_root():
    return {"message": "Bem vindo ao Machine Learning da Markfy!"}


@app.get("/segment-analysis")
def segment_analysis():
    data = customer_segment.to_dict()
    return {"segment-analysis": data}