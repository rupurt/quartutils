import asyncio
from threading import Thread
from typing import List, Tuple, Type

from quart import Quart

from quartutils.task_server import TaskServer
from quartutils.task_server_config import TaskServerConfig


class AsyncTaskServer:
    """
    todo...
    """

    loop: asyncio.AbstractEventLoop
    shutdown_event: asyncio.Event
    servers: List[TaskServer]

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        shutdown_event: asyncio.Event,
        servers: List[
            Tuple[
                Type[TaskServer],
                Quart,
                TaskServerConfig,
            ]
        ],
    ):
        self.loop = loop
        self.shutdown_event = shutdown_event
        self.servers = []
        for Server, app, config in servers:
            server = Server(
                app=app,
                loop=loop,
                shutdown_event=shutdown_event,
                config=config,
            )
            self.servers.append(server)

    def serve(self):
        """
        todo...
        """
        self.loop.run_forever()
        for t in self.servers:
            t.serve()
