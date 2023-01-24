from typing import Dict, Set

from lib.utils.operators.pipe import PipeOperator

from .params import Params
from .steps.element import Element


class Pipeline:
    def __init__(self, params: Params):
        """
        params: {
            inputs: {
                'sample-file01': Input(),
                'sample-file02': Input(),
                'sample-file03': Input()
            },
            outputs: {
                'sample-file01': Output(),
                'sample-file02': Output(),
                'sample-file03': Output()
            }

        }
        """
        self.inputs = params.inputs
        self.outputs = params.outputs

    def do(self):
        all_sets = {}
        for key in self.inputs:
            funcs = self.inputs[key]

            all_sets[key] = PipeOperator() >> \
                funcs.search >> \
                funcs.read > \
                funcs.build_set

        return self.build_indexes(all_sets)

    def build_indexes(self, all_sets: Dict[str, Set[Element]]):
        outputs = {}
        for key in self.outputs:
            output = self.outputs[key]

            indexer = output.indexer(all_sets[key])
            outputs[key] = indexer

        for key in self.outputs:
            args_keys = self.outputs[key].args_keys
            indexer = outputs[key]

            args = [outputs[k] for k in args_keys]
            indexer.compile(*args)

        return outputs
