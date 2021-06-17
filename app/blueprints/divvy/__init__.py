from flask import Blueprint

bp = Blueprint('divvy', __name__)

from . import models