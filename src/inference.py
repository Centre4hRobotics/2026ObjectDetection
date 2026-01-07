""" Object Detection Inference """

from ai_edge_litert.interpreter import Interpreter, load_delegate

class Inference:
    """ Manages the object detection model"""

    def __init__(self, # pylint: disable=dangerous-default-value
                 model_path: str,
                 delegate_options: dict = { 'backend_type' : 'htp'},
                 delegate_library: str = "libQnnTFLiteDelegate.so") -> None:
        self.delegate_options = delegate_options
        self.delegate = load_delegate(library=delegate_library, options=self.delegate_options)

        self.interpreter = Interpreter(model_path=model_path, experimental_delegates=self.delegate)
        self.interpreter.allocate_tensors()
