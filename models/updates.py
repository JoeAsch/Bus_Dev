import uuid
from typing import Dict
import re
import requests
from dataclasses import dataclass, field
from models.model import Model
from datetime import datetime, date


@dataclass(eq=False)
class Update(Model):
    collection: str = field(init=False, default="updates")
    issue_id: str
    description: str
    date_update: datetime.date = field(default_factory=lambda:datetime.utcnow())
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @classmethod
    def get_by_id(cls, _id: str) -> "Update":
        return cls.find_one_by("_id", _id)

    @classmethod
    def find_updates(cls, issue_id: str) -> "list":
        return cls.find_many('issue_id', issue_id)

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "issue_id": self.issue_id,
            "description": self.description,
            "date_update": self.date_update
        }