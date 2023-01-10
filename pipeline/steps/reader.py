from dataclasses import dataclass
from io import StringIO
from typing import Union

from utils.io import load_df


@dataclass
class Reader:
    filepath_or_buffer: Union[str, StringIO]

    def __post_init__(self):
        df = load_df(self.filepath_or_buffer)
        df = df.fillna(0)

        self.df = df

    def _element(self):
        return
