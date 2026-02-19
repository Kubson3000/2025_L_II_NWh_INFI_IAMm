from flask import Flask
apps = Flask(__name__)

import hello_world.views # noqa
