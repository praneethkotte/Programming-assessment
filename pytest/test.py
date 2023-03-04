import unittest
import datausa.py
from app import app

class TestApp(unittest.TestCase):
  def SetUp(self):
    app.testing=True
    self.app=app.test_client()


  def test_index(self):
    response=self.app.get('/')
    self.assertEqual(response.status_code,200)




  def test_datausa():
    response=self.app.get('/')
    self.assertEqual(response.status_code,200)
    self.assertEqual(response.data,b'datausa')

if __name__=='__main__':
  unittest.main()