from enum import Enum

class WorkerClass(str, Enum):
    ASYNCIO = "asyncio"
    UVLOOP = "uvloop"
