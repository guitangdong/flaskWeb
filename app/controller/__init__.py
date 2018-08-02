from flask import Flask

app = Flask(__name__)

from app.controller import hello
from app.controller import UserController
