from sanic import Sanic
from sanic.response import json
from tortoise.contrib.sanic import register_tortoise
import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv('DB_URL')

app = Sanic(__name__)

register_tortoise(
    app, db_url=db_url, modules={"models": ["models"]}, generate_schemas=True
)
 
 
@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    return json({'hello': path})