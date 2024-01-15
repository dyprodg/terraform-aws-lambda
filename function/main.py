import os

def handler(event, ctx):
    name = os.environ.get("NAME", "World")  
    return {
        "message": f"Hello {name}!"
    }