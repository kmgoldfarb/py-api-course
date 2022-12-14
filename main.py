from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "What did you have for breakfast?"}


@app.get("/posts")
def get_posts():
    return {"data": "These are your posts."}
