from dataclasses import dataclass
from io import StringIO
from typing import Union

from lib.utils.pandas.loader import load_df
from pandas import DataFrame


@dataclass
class Reader:
    filepath_or_buffer: Union[str, StringIO]

    def read(self, ext="csv"):
        df = load_df(self.filepath_or_buffer, ext)
        return self._parse(df)

    def _parse(self, df: DataFrame):
        df = df.fillna(0)

        return df
