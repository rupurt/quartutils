import asyncio

from hypercorn.asyncio import serve
from hypercorn.config import Config as HypercornConfig
from quart import Quart

from quartutils.task_server_config import TaskServerConfig


class TaskServer:
    """
    todo...
    """

    hypercorn_config: HypercornConfig
    app: Quart
    loop: asyncio.AbstractEventLoop
    shutdown_event: asyncio.Event

    def __init__(
        self,
        app: Quart,
        loop: asyncio.AbstractEventLoop,
        shutdown_event: asyncio.Event,
        config: TaskServerConfig,
    ):
        hypercorn_config = HypercornConfig()
        hypercorn_config.bind = [f"{config.host}:{config.port}"]
        hypercorn_config.loglevel = config.log_level
        hypercorn_config.use_reloader = config.use_reloader
        hypercorn_config.worker_class = config.worker_class.value

        self.hypercorn_config = hypercorn_config
        self.app = app
        self.loop = loop
        self.shutdown_event = shutdown_event

    def serve(self):
        """
        todo...
        """
        return self.loop.create_task(
            serve(
                self.app,
                self.hypercorn_config,
                shutdown_trigger=self.shutdown_event.wait,
            )
        )
