import subprocess
import asyncio
from uvicorn import Server, Config


class MyServer(Server):
    async def run(self, sockets=None):
        self.config.setup_event_loop()
        return await self.serve(sockets=sockets)


async def run():
    apps = []
    config_list = [("services.user.app:app", 8001), ("services.item.app:app", 8002), ("services.cart.app:app", 8003)]
    for cfg in config_list:
        config = Config(cfg[0], host="127.0.0.1",
                        port=cfg[1])
        server = MyServer(config=config)
        apps.append(server.run())
    return await asyncio.gather(*apps)


def start():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())

#
# def auto_format():
#     subprocess.call(["black", "services"])
#
#
# def run_linter():
#     subprocess.call(["flake8", "services"])


def run_tests():
    subprocess.call(["pytest"])

#
# def create_dependency_graph():
#     subprocess.call(["pydeps", "services", "--cluster"])
#
#
# def check_types():
#     subprocess.call(["mypy", "services"])


if __name__ == "__main__":
    run_tests()
    start()
