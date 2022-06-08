from pandas import offsets
from get_test_app import creage_app


def test_get_company_list_found():
    app = creage_app()
    client = app.test_client()
    url = '/api/company/'
    response = client.get(url)
    assert len(response.json['bankinfo']) != 0
    assert response.status_code == 200

def test_single_company_found():
    app = creage_app()
    client = app.test_client()
    url = '/api/company/5/'
    response = client.get(url)
    assert response.json['bankinfo']['id'] == 5
    assert response.status_code == 200


def test_not_single_company_found():
    app = creage_app()
    client = app.test_client()
    url = '/api/company/9999/'
    response = client.get(url)
    assert len(response.json['bankinfo']) == 0
    assert response.status_code == 200



# limit amd offset is mandatory parmas 
def test_filter_api_success():
    app = creage_app()
    client = app.test_client()
    url = '/api/company/?HasPatent=True&Exporter=0.0&limit=10&offset=1'
    response = client.get(url)
    assert len(response.json['bankinfo']) != 0
    assert response.status_code == 200


def test_filter_api_failed():
    app = creage_app()
    client = app.test_client()
    url = '/api/company/?HasPatent=True&Exporter=1.5&limit=10&offset=1'
    response = client.get(url)
    import pdb;pdb.set_trace()
    assert len(response.json['bankinfo']) == 0
    assert response.status_code == 200
