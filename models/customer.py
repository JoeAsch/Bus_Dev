import uuid
from typing import Dict
import re
import requests
from dataclasses import dataclass, field
from models.model import Model
import models.user.errors as UserErrors


@dataclass(eq=False)
class Customer(Model):
    collection: str = field(init=False, default="customers")
    name_first: str
    name_last: str
    company: str
    email: str
    phone: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)



    @classmethod
    def find_by_email(cls, email: str) -> "Customer":
        try:
            return cls.find_one_by("email", email)
        except TypeError:
            raise UserErrors.UserNotFoundError("Customer with this email not found")

    @classmethod
    def get_by_id(cls, _id: str) -> "Customer":
        return cls.find_one_by("_id", _id)

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "name_first": self.name_first,
            "name_last": self.name_last,
            "company": self.company,
            "email": self.email,
            "phone": self.phone
        }