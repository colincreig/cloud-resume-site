from api.HttpTrigger1 import main
import azure.functions as func

def test_example():
    req = func.HttpRequest(
        method='GET',
        url='/api/HttpTrigger1',
        params={'name': 'TestUser'},
        body=None
    )
    resp = main(req)
    assert resp.status_code == 200
    assert resp.get_body().decode() == "Hello, TestUser!"

