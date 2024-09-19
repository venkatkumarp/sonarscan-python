from fastapi import FastAPI
from mangum import Mangum  # Mangum adapter for AWS Lambda

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Add your myfile.py logic here or import it
import myfile

# Handler for AWS Lambda
handler = Mangum(app)
