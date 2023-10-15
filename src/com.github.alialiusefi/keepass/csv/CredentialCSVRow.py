from typing import Any, Dict, List
import CredentialsCSVHeader


class CredentialCSVRow:
    row: Dict[str, Any]

    def __int__(self, csv_header: CredentialsCSVHeader, values: List[Any]):
        local_dict: Dict[str, Any] = {}
        for key, value in zip(csv_header.columns, values):
            local_dict[key] = value
