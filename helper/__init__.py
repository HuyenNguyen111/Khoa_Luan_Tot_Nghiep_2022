from .detect import detect
import onnxruntime
session = onnxruntime.InferenceSession("model.onnx")
