from .detect import detect
from .utils import allocate_buffers
import tensorrt as trt

# TRT_LOGGER = trt.Logger()
TRT_LOGGER = trt.Logger(trt.Logger.INFO)
trt.init_libnvinfer_plugins(TRT_LOGGER, namespace="")
with open("./model_fp16.engine", "rb") as f, trt.Runtime(TRT_LOGGER) as runtime:
    engine = runtime.deserialize_cuda_engine(f.read())

context = engine.create_execution_context()
context.set_binding_shape(0, (1, 3, 416, 416))
buffers = allocate_buffers(engine, 1)
