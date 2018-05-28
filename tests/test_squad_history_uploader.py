from bae_bot.squad_history_uploader import main



def test_upload_success():
    assert True
    resp = main(None, None)
    assert resp['statusCode'] == 200