from flask import Blueprint, request, jsonify
from models import BatchRequestSchema
from builder import builder_query
import os

main_bp = Blueprint('main', __name__)

FILE_NAME: str = 'data/apache_logs.txt'


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    data = request.json
    validation_data = BatchRequestSchema().load(data)

    result = None
    for query in validation_data['queries']:
        result = builder_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=FILE_NAME,
            data=result,
        )

    return jsonify(os.path.basename(FILE_NAME), result)
