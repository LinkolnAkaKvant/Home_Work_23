from typing import Iterator, List, Any

from utils import filter_query, unique_query, limit_query, map_query, sort_query, regex_query

CMD_TO_FUNCTIONS = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'regex': regex_query,
}


def read_file(file_name: str) -> Iterator[str]:
    with open(file_name) as file:
        for line in file:
            yield line


def builder_query(cmd: str, value: str, file_name: str, data: Any[str]) -> List[str]:
    if data is None:
        prepared_data = read_file(file_name)
    else:
        prepared_data = data

    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepared_data))
