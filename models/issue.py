import uuid
from typing import Dict
import re
import requests
from dataclasses import dataclass, field
from models.model import Model
from datetime import datetime, timedelta

@dataclass(eq=False)
class Issue(Model):
    collection: str = field(init=False, default="issues")
    status: str
    customer_id: str
    description: str
    date_start: datetime.date = field(default_factory=lambda:datetime.utcnow())
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @classmethod
    def get_by_id(cls, _id: str) -> "Issue":
        return cls.find_one_by("_id", _id)

    @classmethod
    def find_issues(cls, customer_id) -> "list":
        return cls.find_many('customer_id', customer_id)

    @classmethod
    def find_by_status(cls, status) -> "list":
        return cls.find_many("status", status)


    def json(self) -> Dict:
        return {
            "_id": self._id,
            "status": self.status,
            "customer_id": self.customer_id,
            "description": self.description,
            "date_start": self.date_start
        }