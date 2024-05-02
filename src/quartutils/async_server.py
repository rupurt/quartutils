import asyncio

from hypercorn.asyncio import serve
from hypercorn.config import Config
from quart import Quart

from quartutils.worker_class import WorkerClass


class AsyncServer:
    """
    todo...
    """

    config: Config
    app: Quart

    def __init__(
        self,
        app: Quart,
        *,
        host: str = "0.0.0.0",
        port: int = 8080,
        log_level: str = "info",
        use_reloader: bool = True,
        worker_class: WorkerClass = WorkerClass.ASYNCIO,
    ):
        config = Config()
        config.bind = [f"{host}:{port}"]
        config.loglevel = log_level
        config.use_reloader = use_reloader
        config.worker_class = worker_class.value

        self.config = config
        self.app = app

    def serve(self):
        return asyncio.run(
            serve(self.app, self.config),
        )
