import json

FILE_NAME = 'sides_template.json'


def get_side_pattern(template, file=FILE_NAME):
    with open(file) as f:
        return json.load(f)[template]


def get_available_patterns(file=FILE_NAME):
    with open(file) as f:
        return json.load(f)


def safe_pattern(template_name, file=FILE_NAME):
    with open(file) as f:
        json_db = json.load(f)
        json_db.update(template_name)
        json.dump(json_db, open(file, 'w'), indent=4)


def delete_pattern(template_key, file=FILE_NAME):
    with open(file) as f:
        json_db = json.load(f)
        json_db.pop(template_key)
        json.dump(json_db, open(file, 'w'), indent=4)


if __name__ == '__main__':

    test = {
        'test_template_1': {
            'side_1': [
                [
                    ('soldier', {}),
                    ('vehicle', {'operator': 'soldier', 'u_count': 1}),
                    ('soldier', {}),
                    ('soldier', {})
                ],
                [
                    ('soldier', {}),
                    ('vehicle', {'operator': 'soldier', 'u_count': 2})
                ],
            ],
            'side_2': [
                [
                    ('soldier', {}),
                    ('vehicle', {'operator': 'soldier', 'u_count': 3})
                ]
            ]
        },

    }

    safe_pattern(test)
