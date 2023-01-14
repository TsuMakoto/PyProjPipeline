from dataclasses import dataclass
from io import StringIO
from typing import Union

import pandas as pd
from utils.io import load_df


@dataclass
class Reader:
    filepath_or_buffer: Union[str, StringIO]

    def read(self):
        df = load_df(self.filepath_or_buffer)
        self._parse(df)

        return df

    def _parse(self, df: pd.core.DataFrame):
        df = df.fillna(0)

        return df
