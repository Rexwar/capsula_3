from fastapi import FastAPI	# Import the FastAPI class

app = FastAPI()	# Create an instance of the FastAPI class

@app.get("/helloworld")	# Define a route for the root URL

async def get_message():
    return {"message": "Hello, World!"}	# Return a JSON response