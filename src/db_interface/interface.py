from abc import ABC, abstractmethod
from typing import List, Tuple, Union, Dict

from src.db_controller.postgres_manager import PostgreSQLManager
from src.model.Customer import Customer


class Interface(ABC):

    @abstractmethod
    def get_customers_by_id(self, ids: [int]) -> List[Customer]:
        pass

    @abstractmethod
    def get_config(self) -> Tuple:
        pass


class PostgresMethods(Interface):

    def get_config(self) -> Tuple:
        host = "localhost"
        database = "dvdrental"
        user = "postgres"
        password = "changeme"
        port = "5432"
        return host, database, user, password, port

    def get_customers_by_id(self, ids: [int]) -> Union[List[Customer], Dict]:
        customer_list = []
        try:
            if ids and all(isinstance(x, int) for x in ids):
                with PostgreSQLManager(*self.get_config()) as postgres:
                    if postgres:
                        for customer_id in ids:
                            sql = f"select * from public.customer where customer_id = '{customer_id}'"
                            customer_dict = Customer(**postgres.select(sql)[0])
                            customer_list.append(customer_dict)
                        return customer_list
                    else:
                        del postgres
            elif None in ids:
                bad_items = [[i, x] for i, x in enumerate(ids) if not isinstance(x, int)]
                indexes = [bad_items[0] for bad_items in bad_items]
                items = [bad_items[1] for bad_items in bad_items]
                return {"Error": "ID(s) introducidos no válidos",
                        "error_index": indexes,
                        "error_type": items}
            else:
                return {"Error": "ID(s) introducidos no válidos"}
        except TypeError:
            return {"Error": "ID(s) introducidos no válidos"}
