from typing import Dict

from inputs.file_info import FileInfo


class Params:
    inputs: Dict[str, FileInfo]


class Pipeline:
    def __init__(self, params: Params):
        """
        params: {
            inputs: {
                'sample-file01': FileInfo(),
                'sample-file02': FileInfo(),
                'sample-file03': FileInfo()
            }
        }
        """
        self.params = params

    def do(self):
        readers = dict([
            (key, self.params.inputs[key].search())
            for key in self.params.inputs
        ])
