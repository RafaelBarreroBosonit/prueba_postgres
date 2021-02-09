import datetime
import unittest
from src.db_interface.interface import PostgresMethods
from src.model.Customer import Customer


class TestDBInterface(unittest.TestCase):

    def test_ok_1(self):
        customer_list_postgres = PostgresMethods().get_customers_by_id([3])

        dict_postgres = {0: {"active": 1,
                             "activebool": True,
                             "address_id": 7,
                             "create_date": datetime.datetime.strptime("2006-02-14", "%Y-%m-%d").date(),
                             "customer_id": 3,
                             "email": "linda.williams@sakilacustomer.org",
                             "first_name": "Linda",
                             "last_name": "Williams",
                             "last_update": datetime.datetime.strptime("2013-05-26 14:49:45.738000",
                                                                       "%Y-%m-%d %H:%M:%S.%f"),
                             "store_id": 1}}
        expected_customer_list = [Customer(**value) for value in dict_postgres.values()]
        self.assertEqual(customer_list_postgres, expected_customer_list)

    def test_ok_2(self):
        customer_list_postgres = PostgresMethods().get_customers_by_id([1, 2, 3])

        dict_postgres = {0: {"active": 1,
                             "activebool": True,
                             "address_id": 5,
                             "create_date": datetime.datetime.strptime("2006-02-14", "%Y-%m-%d").date(),
                             "customer_id": 1,
                             "email": "mary.smith@sakilacustomer.org",
                             "first_name": "Mary",
                             "last_name": "Smith",
                             "last_update": datetime.datetime.strptime("2013-05-26 14:49:45.738000",
                                                                       "%Y-%m-%d %H:%M:%S.%f"),
                             "store_id": 1},
                         1: {"active": 1,
                             "activebool": True,
                             "address_id": 6,
                             "create_date": datetime.datetime.strptime("2006-02-14", "%Y-%m-%d").date(),
                             "customer_id": 2,
                             "email": "patricia.johnson@sakilacustomer.org",
                             "first_name": "Patricia",
                             "last_name": "Johnson",
                             "last_update": datetime.datetime.strptime("2013-05-26 14:49:45.738000",
                                                                       "%Y-%m-%d %H:%M:%S.%f"),
                             "store_id": 1},
                         2: {"active": 1,
                             "activebool": True,
                             "address_id": 7,
                             "create_date": datetime.datetime.strptime("2006-02-14", "%Y-%m-%d").date(),
                             "customer_id": 3,
                             "email": "linda.williams@sakilacustomer.org",
                             "first_name": "Linda",
                             "last_name": "Williams",
                             "last_update": datetime.datetime.strptime("2013-05-26 14:49:45.738000",
                                                                       "%Y-%m-%d %H:%M:%S.%f"),
                             "store_id": 1}
                         }
        expected_customer_list = [Customer(**value) for value in dict_postgres.values()]
        self.assertEqual(customer_list_postgres, expected_customer_list)

    def test_none(self):
        customer_list_postgres = PostgresMethods().get_customers_by_id(None)
        expected_error = {"Error": "ID(s) introducidos no válidos"}
        self.assertEqual(customer_list_postgres, expected_error)

    def test_list_none(self):
        customer_list_postgres = PostgresMethods().get_customers_by_id([None])
        expected_error = {"Error": "ID(s) introducidos no válidos",
                          "error_index": [0],
                          "error_type": [None]}
        self.assertEqual(customer_list_postgres, expected_error)

    def test_list_int_none(self):
        customer_list_postgres = PostgresMethods().get_customers_by_id([1, 2, None])
        expected_error = {"Error": "ID(s) introducidos no válidos",
                          "error_index": [2],
                          "error_type": [None]}
        self.assertEqual(customer_list_postgres, expected_error)

    def test_list_empty(self):
        customer_list_postgres = PostgresMethods().get_customers_by_id([])
        expected_error = {"Error": "ID(s) introducidos no válidos"}
        self.assertEqual(customer_list_postgres, expected_error)

    def test_list_string(self):
        customer_list_postgres = PostgresMethods().get_customers_by_id(["asdasd"])
        expected_error = {"Error": "ID(s) introducidos no válidos"}
        self.assertEqual(customer_list_postgres, expected_error)

    def test_list_int_string_none(self):
        customer_list_postgres = PostgresMethods().get_customers_by_id([1, "asdasd", None])
        expected_error = {"Error": "ID(s) introducidos no válidos",
                          "error_index": [1, 2],
                          "error_type": ["asdasd", None]}
        self.assertEqual(customer_list_postgres, expected_error)

    def test_id_error(self):
        customer_list_postgres = PostgresMethods().get_customers_by_id([999999999999999999])
        expected_error = {"Error": "ID(s) introducidos no válidos"}
        self.assertEqual(customer_list_postgres, expected_error)

    def test_id_not_exists(self):
        customer_list_postgres = PostgresMethods().get_customers_by_id([999])
        expected_error = {"Error": "ID(s) introducidos no válidos"}
        self.assertEqual(customer_list_postgres, expected_error)

    def test_id_exists_not_exists(self):
        customer_list_postgres = PostgresMethods().get_customers_by_id([1, 999])
        expected_error = {"Error": "ID(s) introducidos no válidos"}
        self.assertEqual(customer_list_postgres, expected_error)

    def test_id_not_list(self):
        customer_list_postgres = PostgresMethods().get_customers_by_id(999)
        expected_error = {"Error": "ID(s) introducidos no válidos"}
        self.assertEqual(customer_list_postgres, expected_error)


if __name__ == '__main__':
    unittest.main()
