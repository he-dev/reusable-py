import os
import tempfile
import json
from pathlib import Path
from datetime import datetime, date
from typing import Any, Dict


class _JsonDateTimeEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, (date, datetime)):
            return o.isoformat()


class _JsonDateTimeDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.parse_datetime_or_default)

    @staticmethod
    def parse_datetime_or_default(d: Dict):
        r = dict()
        for k in d.keys():
            r[k] = d[k]
            if isinstance(d[k], str):
                try:
                    r[k] = datetime.fromisoformat(d[k])  # try parse date-time
                except ValueError:
                    pass  # default value is already set
        return r
