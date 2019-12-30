# -*- coding:utf-8 -*-
import os
from flask import Flask, render_template, jsonify
from werkzeug.exceptions import HTTPException
#from flaskwebgui import FlaskUI

from traceback import format_exc

from JavHelper.views.emby_actress import emby_actress
from JavHelper.views.parse_jav import parse_jav
from JavHelper.views.scan_directory import directory_scan
from JavHelper.core.ini_file import recreate_ini, DEFAULT_INI


def create_app():
    # create and configure the app
    app = Flask(__name__, template_folder='templates')
    app.register_blueprint(emby_actress)
    app.register_blueprint(parse_jav)
    app.register_blueprint(directory_scan)

    app.config['JSON_AS_ASCII'] = False
    #ui = FlaskUI(app)

    # init setting file
    if not os.path.isfile(DEFAULT_INI):
        print('ini file {} doesn\'t exists, recreate one and apply default settings'.format(DEFAULT_INI))
        recreate_ini(DEFAULT_INI)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('home.html')

    @app.errorhandler(Exception)
    def handle_exception(e):
        # pass through HTTP errors
        if isinstance(e, HTTPException):
            return e

        # now you're handling non-HTTP exceptions only
        return jsonify({'errors': format_exc()}), 500

    return app


def create_app_backend():
    # create and configure the app
    app = Flask(__name__, template_folder='templates')
    app.register_blueprint(emby_actress)
    app.register_blueprint(parse_jav)
    app.register_blueprint(directory_scan)

    app.config['JSON_AS_ASCII'] = False

    # init setting file
    if not os.path.isfile(DEFAULT_INI):
        print('ini file {} doesn\'t exists, recreate one and apply default settings'.format(DEFAULT_INI))
        recreate_ini(DEFAULT_INI)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('home.html')

    @app.errorhandler(Exception)
    def handle_exception(e):
        # pass through HTTP errors
        if isinstance(e, HTTPException):
            return e

        # now you're handling non-HTTP exceptions only
        return jsonify({'errors': format_exc()}), 500

    return app
