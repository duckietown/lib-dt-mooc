import os
import re

import torch
from dt_data_api import DataClient

from dt_mooc.utils import plain_progress_monitor


class Storage:

    def __init__(self, token: str):
        self._client = DataClient(token)
        self._space = self._client.storage("user")
        self._folder = 'courses/mooc/2021/data'

    @staticmethod
    def export_model(name: str, model: torch.nn.Module, input: torch.Tensor):
        if not re.match('^[^0-9a-zA-Z-_.]+$', name):
            raise ValueError("The model name can only container letters, numbers and these "
                             "symbols '.,-,_'")
        # ---
        # export the model
        torch.onnx.export(model,  # model being run
                          input,  # model input (or a tuple for multiple inputs)
                          f"{name}.onnx",
                          # where to save the model (can be a file or file-like object)
                          export_params=True,
                          # store the trained parameter weights inside the model file
                          opset_version=10,  # the ONNX version to export the model to
                          do_constant_folding=True,
                          # whether to execute constant folding for optimization
                          input_names=['input'],  # the model's input names
                          output_names=['output'],  # the model's output names
                          dynamic_axes={'input': {0: 'batch_size'},  # variable lenght axes
                                        'output': {0: 'batch_size'}})

    def upload_model(self, name: str, model: torch.nn.Module, input: torch.Tensor):
        # export the model
        self.export_model(name, model, input)
        # define source/destination paths
        source = f"{name}.onnx"
        destination = os.path.join(self._folder, 'nn_models', f"{name}.onnx")
        # upload the model
        handler = self._space.upload(source, destination)
        handler.register_callback(plain_progress_monitor)
        # wait for the upload to finish
        handler.join()
