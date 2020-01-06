import logging

from json_builder import JSONObject
from json_lexer import lex
from string_functions import to_json, from_json

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
        level=logging.INFO
    )

    print(lex(''))
    to_json([{"foo": [1, 2, '2']}])
    from_json('{ "foo" : [1, 2, 3, 4] }')

    jo = JSONObject().put_string("JSON1", "Hello World!"). \
        put_string("JSON2", "Hello my World!"). \
        put_string(1, JSONObject().put_list("key1", "value1")).\
        put_list('list', [1, 2, True]).\
        put_object('obj', {'k1': 2, 'k2': 3}).\
        put_list('list2', ['1"']).\
        put_object('obj', JSONObject().put_list("key1", [])). \
        put_list('list3', [1, JSONObject().put_list("key1", [])])

    print(jo.to_json())
