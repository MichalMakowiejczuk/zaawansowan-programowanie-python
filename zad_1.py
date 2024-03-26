from fastapi import FastAPI

app = FastAPI()

class HelloWorld:
    async def get(self):
        return {'hello': 'world'}

hello_world = HelloWorld()

@app.get("/")
async def root():
    return await hello_world.get()
