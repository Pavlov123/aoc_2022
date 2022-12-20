import requests
from copy import deepcopy


class AOCClient:
    def __init__(self):
        with open("session", "r") as session_storage:
            self.session_cookie = session_storage.read().strip()

    def _request(self, _method, *args, **kwargs):
        cookies = deepcopy(kwargs.pop("cookies", {}))
        cookies["session"] = self.session_cookie

        return getattr(requests, _method)(
            *args,
            cookies=cookies,
            **kwargs
        )

    def get(self, *args, **kwargs):
        return self._request("get", *args, **kwargs)
