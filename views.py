from flask import Blueprint, request, jsonify

from builder import builder_query

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    data = request.json

    return jsonify(builder_query(cmd='', value='GET', file_name='data/apache_logs.txt'))
