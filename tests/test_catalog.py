import unittest
from unittest.mock import patch
import database

class CatalogFilterTest(unittest.TestCase):
    @patch("database.fetch_all", return_value=[])
    def test_supplier_and_search_use_both_conditions(self, fetch):
        database.get_products({"supplier": "Поставщик А", "search_query": "LAB-100",
                               "sort_by": "stock_quantity", "sort_order": "asc"})
        sql, params = fetch.call_args.args
        self.assertIn("ILIKE %s", sql)
        self.assertIn("AND s.supplier_name = %s", sql)
        self.assertIn("p.stock_quantity ASC", sql)
        self.assertEqual(params, ("%LAB-100%", "%LAB-100%", "%LAB-100%", "Поставщик А"))

    @patch("database.fetch_all", return_value=[])
    def test_all_suppliers_has_no_restriction(self, fetch):
        database.get_products({"supplier": "Все поставщики"})
        sql, params = fetch.call_args.args
        self.assertNotIn("s.supplier_name = %s", sql)
        self.assertEqual(params, ())

if __name__ == "__main__":
    unittest.main()

