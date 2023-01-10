from typing import Dict, List, Set

from inputs.file_info import FileInfo
from steps.reader import Element, Reader


class Inputs:
    key: str
    info: FileInfo


class Output:
    def build(self, )


class Outputs:



class Params:
    inputs: Dict[str, FileInfo]


class Pipeline:
    def __init__(self, inputs: Dict[str, FileInfo]):
        """
        params: {
            inputs: {
                'sample-file01': FileInfo(),
                'sample-file02': FileInfo(),
                'sample-file03': FileInfo()
            }
        }
        """
        self.inputs = inputs

    def do(self):
        all_sets = {}
        for key in self.inputs:
            file = self.inputs[key].search()
            reader = Reader(file)
            reader.build_set()

            all_sets[key] = reader.sets

        appendix = build_appendix(all_sets)

    def build_appendix(
            self,
            all_sets: Dict[str, Set[Element]],
            key_map: Dict[str, List[str]]):
        outputs = {}
        for key in key_map:
            args_keys = key_map[key]

            args = [all_sets[k] for k in args_keys]
            klass = self.params.outputs[key]

            output = klass(*args)

            outputs[key] = output

        return outputs
