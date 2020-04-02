import json
import logging
import os

from quart import Request


async def handle(body: bytes, req: Request) -> str:
    """handle a request to the function
    Args:
        body (bytes): request body
        req (str): original request object
    """
    payload = str(body, encoding="utf-8")
    logging.debug("host=%s", req.host)
    logging.debug("path=%s", req.path)
    for h, v in req.headers.items():
        logging.debug("headers=%s=%s", h, v)
    logging.debug("body=%s", payload)
    logging.debug("environment=%s", os.environ)
    return json.dumps(dict(os.environ.items()))
