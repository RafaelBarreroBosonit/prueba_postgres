from datetime import datetime


class Customer:
    def __init__(self, customer_id: int, store_id: int, first_name: str, last_name: str, email: str, address_id: int,
                 activebool: bool, create_date: datetime, last_update: datetime, active: int):
        self._customer_id = customer_id
        self._store_id = store_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._address_id = address_id
        self._activebool = activebool
        self._create_date = create_date
        self._last_update = last_update
        self._active = active

    def __eq__(self, other):
        return self._customer_id == other.customer_id and \
               self._store_id == other.store_id and \
               self._first_name == other.first_name and \
               self._last_name == other.last_name and \
               self._email == other.email and \
               self._address_id == other.address_id and \
               self._activebool == other.activebool and \
               self._create_date == other.create_date and \
               self._last_update == other.last_update and \
               self._active == other.active

    @property
    def customer_id(self) -> int:
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: int):
        self._customer_id = customer_id

    @property
    def store_id(self) -> int:
        return self._store_id

    @store_id.setter
    def store_id(self, store_id: int):
        self._store_id = store_id

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def address_id(self) -> int:
        return self._address_id

    @address_id.setter
    def address_id(self, address_id: int):
        self._address_id = address_id

    @property
    def activebool(self) -> bool:
        return self._activebool

    @activebool.setter
    def activebool(self, activebool: bool):
        self._activebool = activebool

    @property
    def create_date(self) -> datetime:
        return self._create_date

    @create_date.setter
    def create_date(self, create_date: datetime):
        self._create_date = create_date

    @property
    def last_update(self) -> datetime:
        return self._last_update

    @last_update.setter
    def last_update(self, last_update: datetime):
        self._last_update = last_update

    @property
    def active(self) -> int:
        return self._active

    @active.setter
    def active(self, active: int):
        self._active = active

