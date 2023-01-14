from typing import Dict, List, Set

from input import Input
from steps.appendix import Appendix
from steps.reader import Element


class Output:
    appendix: Appendix
    args_keys: List[str]


class Params:
    inputs: Dict[str, Input]
    outputs: Dict[str, Output]


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
            pipeline = self.inputs[key]
            pipeline.search()
            pipeline.read()
            pipeline.build_set()

            all_sets[key] = pipeline.sets

        return self.build_appendix(all_sets)

    def build_appendix(self, all_sets: Dict[str, Set[Element]]):
        outputs = {}
        for key in self.outputs:
            output = self.outputs[key]

            args_keys = output.args_keys
            appendix = output.appendix

            args = [all_sets[k] for k in args_keys]
            appendix.post_init(*args)

            outputs[key] = appendix

        return outputs
