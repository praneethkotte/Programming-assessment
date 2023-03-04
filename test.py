def test_datausa():
  response=app.get('/')
  assert response.status_code==200
  asser response.data==b'datausa'