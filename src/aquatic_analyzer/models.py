from dataclasses import dataclass
from pathlib import Path
@dataclass
class WorkbookInfo:
    path: Path
    filename: str
    sheet_names: list[str]
