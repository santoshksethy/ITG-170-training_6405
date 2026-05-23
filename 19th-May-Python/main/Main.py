from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def base_url():
    return {'status':200,
            'message':"Hello World"}


@app.get('/hello/{name}')
def hello_world(name:str):
    return f'Hello {name}'

@app.put('/user/{id}')
def hello_world(id:int):
    return f'Found user  {id} as Santosh'

@app.put('/user/{id}')
def hello_world(id:int):
    return f'Found user  {id} as Santosh'