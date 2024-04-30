import asyncio

from hypercorn.asyncio import serve
from hypercorn.config import Config
from quart import Quart

from quartutils.worker_class import WorkerClass


class TaskServer:
    config: Config
    loop: asyncio.AbstractEventLoop
    shutdown_event: asyncio.Event
    app: Quart

    def __init__(
        self,
        app: Quart,
        loop: asyncio.AbstractEventLoop,
        shutdown_event: asyncio.Event,
        *,
        host: str = "0.0.0.0",
        port: int = 8080,
        log_level: str = "info",
        use_reloader: bool = True,
        worker_class: WorkerClass = WorkerClass.UVLOOP,
    ):
        config = Config()
        config.bind = [f"{host}:{port}"]
        config.loglevel = log_level
        config.use_reloader = use_reloader
        config.worker_class = worker_class.value

        self.config = config
        self.app = app
        self.loop = loop
        self.shutdown_event = shutdown_event

    def serve(self):
        return self.loop.create_task(
            serve(
                self.app,
                self.config,
                shutdown_trigger=self.shutdown_event.wait,
            )
        )
