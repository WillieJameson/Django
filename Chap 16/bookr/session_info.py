import base64
import json
import pprint
import sys


def get_session_dictionary(session_key):
    binary_key, payload = base64.b64decode(session_key).split(b':', 1)
    session_dictionary = json.loads(payload.decode())
    return session_dictionary


if __name__ == '__main__':
    if len(sys.argv)>1:
        session_key = '.eJxVjDsOwjAQBe_iGlkyG9sbSnrOYD2v1ySAEimfKuLuECkFtG9m3mYS1qVL66xT6ou5GDKn3y1DnjrsoDww3Ecr47BMfba7Yg8629tY9HU93L-DDnP3rRkEytAWAS1wbj2L51gdqAmVSxQmocYxVychZkXDgHpXfFQpZN4f-6Q4oA:1nX1ap:OvB8WZInaCC-uoyfkLzF8GCEb7gXnCTtp8C0PHwsZ7k'
        session_dictionary = get_session_dictionary(session_key)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(session_dictionary)