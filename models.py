from typing import Any, Union

from marshmallow import Schema, fields, validates_schema, ValidationError
import os

VALID_CMD_COMMANDS = ('filter', 'unique', 'limit', 'map', 'sort', 'regex',)

FILE_NAME: str = 'data/apache_logs.txt'


class RequestSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str()
    file_name = fields.Str()

    @validates_schema
    def check_all_cmd_valid(self, values: dict[str, str], *args: str, **kwargs: str) -> Any:
        if values['cmd'] not in VALID_CMD_COMMANDS:
            raise ValidationError('"cmd" contains invalid value')

        if values['file_name'] != os.path.basename(FILE_NAME):
            raise FileExistsError


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
