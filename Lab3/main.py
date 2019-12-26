import logging

from string_functions import to_json, from_json

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
        level=logging.INFO
    )

    to_json([{"foo": [1, 2, '2']}])
    from_json('{ "foo" : [1, 2, 3, 4] }')
    from_json({})
