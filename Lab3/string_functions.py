import logging

import json_lexer
import json_parser

logger = logging.getLogger('json_string_functions')


# Function used for obtaining string object from json string
# Input: string
# Output: python string
def from_json(json_string):
    assert type(json_string) == str
    logger.info('from_json: Received string: ' + json_string)
    tokens = json_lexer.lex(json_string)
    json_object = json_parser.parse(tokens, is_root=True)[0]
    assert type(json_object) == dict
    logger.info('from_json: Returned object: ' + str(json_object))
    return json_parser.parse(tokens, is_root=True)[0]


def to_json(obj):
    # print(type(obj))
    types = [dict, list, str, int, float, bool, type(None)]
    assert type(obj) in types, 'Not allowed type'
    logger.info('to_json: Received object: ' + str(obj))
    json_type = type(obj)
    if json_type is dict:
        string = '{'
        dict_len = len(obj)

        if dict_len == 0:
            logger.info('to_json: Returned string: {}')
            return '{}'

        for i, (key, val) in enumerate(obj.items()):
            string += '"{}": {}'.format(key, to_json(val))

            if i < dict_len - 1:
                string += ', '
            else:
                string += '}'

        logger.info('to_json: Returned string: ' + string)
        return string
    elif json_type is list:
        string = '['
        list_len = len(obj)

        if list_len == 0:
            logger.info('to_json: Returned string: []')
            return '[]'

        for i, val in enumerate(obj):
            string += to_json(val)

            if i < list_len - 1:
                string += ', '
            else:
                string += ']'

        logger.info('to_json: Returned string: ' + string)
        return string
    elif json_type is str:
        return '"{}"'.format(obj)
    elif json_type is bool:
        logger.info('to_json: Returned string: ' + str(obj).lower())
        return 'true' if obj else 'false'
    elif isinstance(obj, type(None)):
        logger.info('to_json: Returned string: null')
        return 'null'

    logger.info('to_json: Returned string: ' + str(obj))
    return str(obj)