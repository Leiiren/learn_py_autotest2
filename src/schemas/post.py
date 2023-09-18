POST_SCHEMA_GET_COMPANIES = {
    "type": "object",
    "properties": {
        "company_id": {"type": "number"},
        "company_name": {"type": "string"},
        "company_address": {"type": "string"},
        "company_status": {"type": "string"}
    }
}

# tests/test_something.py::test_getting_post
# {'data': [
# {'company_id': 1, 'company_name': 'Tesla', 'company_address': 'Nicholastown, IL 80126', 'company_status': 'ACTIVE'},
# {'company_id': 2, 'company_name': 'Google', 'company_address': '1093 Cooke Harbor Apt. 908', 'company_status': 'ACTIVE'},
# {'company_id': 3, 'company_name': 'Toyota', 'company_address': 'Davidberg, MN 88952', 'company_status': 'ACTIVE'}],
# 'meta': {'limit': 3, 'offset': 0, 'total': 7}}