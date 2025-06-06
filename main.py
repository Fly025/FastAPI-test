from fastapi import FastAPI

app = FastAPI()

#modifica
# incremento minor release

# Elenco modifiche in Brach Nuova-funzione
# prima modifica

# prova release


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
