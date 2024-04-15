from fastapi import FastAPI

app = FastAPI()


@app.get('/test')
async def health():
    return {'message': 'Success'}
