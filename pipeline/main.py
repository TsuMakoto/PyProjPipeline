from utils.pipe_operator import PipeOperator

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

            all_sets[key] = PipeOperator() * \
                funcs.search * \
                funcs.read >> \
                funcs.build_set

        return self.build_appendix(all_sets)

    def build_appendix(self, all_sets: dict[str, set[Element]]):
        outputs = {}
        for key in self.outputs:
            output = self.outputs[key]

            args_keys = output.args_keys
            appendix = output.appendix

            args = [all_sets[k] for k in args_keys]
            appendix.post_init(all_sets[key], *args)

            outputs[key] = appendix

        return outputs
