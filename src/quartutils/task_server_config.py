from pydantic import BaseModel, Field

from quartutils.worker_class import WorkerClass


class TaskServerConfig(BaseModel):
    """
    todo...
    """

    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8080)
    log_level: str = Field(default="info")
    use_reloader: bool = Field(default=True)
    worker_class: WorkerClass = Field(default=WorkerClass.ASYNCIO)
