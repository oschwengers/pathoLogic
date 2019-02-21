#!/usr/bin/env python3

import os
import connexion
import json
from flask import request, send_from_directory, g
from flask_cors import CORS
from swagger_server import encoder
from swagger_server import db

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'pathoLogic'})

    # Serve results under /v1/result/PATH
    app.app.config['STATIC_URL_PATH'] = os.path.abspath(os.getenv('BASE_DIR', os.getcwd()))

    @app.app.route('/v1/result/<path:path>')
    def send_result(path):
        return send_from_directory('runs', path)

    #Temporary fix: use dictionary as db

    # Create route for nextflow weblog (assembly)
    @app.app.route('/v1/nf_assembly/<runid>', methods=['POST'])
    def nf_assembly(runid):
        req_data = request.get_json()
        print(req_data)
        db['status_assembly'][runid] = req_data
        print(json.dumps(db['status'][runid]))
        return 'NF Request received'

    # Create route for nextflow weblog (plasmident)
    @app.app.route('/v1/nf_plasmident/<runid>', methods=['POST'])
    def nf_plasmident(runid):
        req_data = request.get_json()
        print(req_data)
        db['status_plasmident'][runid] = req_data
        print(json.dumps(db['status'][runid]))
        return 'NF Request received'

    CORS(app.app) # enable CORS everywhere
    app.run(port=os.getenv('HTTP_PORT', 8080))

if __name__ == '__main__':
    main()
