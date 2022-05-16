from app import app
from unittest import TestCase

class CurrencyRates(TestCase):
  def test_currency_form(self):
    with app.test_client() as client:
        # import pdb
        # pdb.set_trace()
        res = client.get('/')
        html = res.get_data(as_text=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn('<h1>Conversion Form</h1>',html)

  def test_currency_form(self):
    with app.test_client() as client:
        res = client.get('/results?frm=USD&to=USD&amt=1000')
        html = res.get_data(as_text=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn('<h1>Your converted results are:</h1>',html)
        self.assertIn('<h2>$1000.0</h2>',html)

     