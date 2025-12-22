from fastapi import FastAPI

app = FastAPI(title="Vaultrix Backend")

@app.get("/")
def health_check():
    return {"status": "Vaultrix backend running"}
