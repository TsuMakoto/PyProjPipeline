from dataclasses import dataclass
from io import StringIO
from typing import Union

from pandas import DataFrame
from utils.pandas.loader import load_df


@dataclass
class Reader:
    filepath_or_buffer: Union[str, StringIO]

    def read(self):
        df = load_df(self.filepath_or_buffer)
        return self._parse(df)

    def _parse(self, df: DataFrame):
        df = df.fillna(0)

        return df
