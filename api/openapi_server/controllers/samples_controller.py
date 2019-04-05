import connexion
import six
import os
import ntpath
import json

from datetime import datetime

from flask import current_app, g
from openapi_server.models.sample import Sample  # noqa: E501
from openapi_server.db import get_db
from openapi_server import util

def format_sample(obj):
    """
    Format a sample
    """
    return {
        'id': obj['id'],
        'author_email': obj['author_email'],
        'created': obj['created'],
        'last_updated': obj['last_updated']
    }

def join_read_path_with_data_dir(read_path):
    """
    Joins a read path with the data directory
    """
    return os.path.join(os.getenv('DATA_DIR', os.getcwd()), ntpath.basename(read_path))

def samples_get():  # noqa: E501
    """List all samples

     # noqa: E501


    :rtype: List[Sample]
    """

    db = get_db()
    return [format_sample(db['samples'][sample]) for sample in db['samples'].keys()]

def samples_post(body=None):  # noqa: E501
    """Create new samples

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Sample
    """
    # Create samplepath
    samplepath = os.path.join(os.environ.get('BASE_DIR', os.getcwd()),'samples' )
    if not os.path.isdir(samplepath):
        os.mkdir(samplepath)

    print(body)
    # Save config and read files for each sample in new folder
    for s in body['samples']:
        conf = body['config']
        os.mkdir(os.path.join(samplepath, s['id']))
        with open(os.path.join(samplepath, s['id'], "nf_config.json"), 'w') as outfile:
            json.dump(conf, outfile)
        with open(os.path.join(samplepath, s['id'], "read_locations.tsv"), 'w') as outfile:
            paths = [join_read_path_with_data_dir(read_path) for read_path in [s['path_lr'], s.get('path_sr1', ""), s.get('path_sr2', "")] if len(read_path)]
            outfile.write(s['id'] + '\t' + "\t".join(paths) + '\n')

    # Store informations in dict db
    db = get_db()
    db['samples'][s['id']] = {
        'id':s['id'],
        'author_email':s['author_email'],
        'created':str(datetime.utcnow()),
        'last_updated':str(datetime.utcnow()),
        'status':"created",
        'zip':None
    }
    
    return body['samples']