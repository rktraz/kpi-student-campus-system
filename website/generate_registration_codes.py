import random
import string
import json


def generate_registration_code(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


registration_code_dict = {}

for number in [1, 3, 4] + list(range(6, 21)):
    registration_code_dict[generate_registration_code(16)] = number

with open('registration_codes.json', 'w') as fp:
    json.dump(registration_code_dict, fp)
