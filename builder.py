from utils import filter_query


def builder_query(cmd: str, value: str, file_name: str):
    with open(file_name) as file:
        return list(filter_query(value, file))
