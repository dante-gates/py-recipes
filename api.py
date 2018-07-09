import logging

import requests as rq


class Endpoint:
    _logger = logging.getLogger(__name__)

    def __init__(self, url, http_client=None):
        self.url = url
        self.http_client = rq if http_client is None else http_client

    def get(self, **kwargs):
        url = self.url + self._format_query_params(**kwargs)
        self._logger.debug('GET {url}'.format(url=url))
        return self.http_client.get(url)

    def post(self, *, data=None, **kwargs):
        url = self.url + self._format_query_params(**kwargs)
        self._logger.debug('POST {url}'.format(url=url))
        return self.http_client.post(self.url, data=data)

    @staticmethod
    def _format_query_params(**query_params):
        return f"?{'&'.join(f'{k}={v}' for k, v in query_params.items())}"


if __name__ == '__main__':
    class Mock:
        def __call__(self, *args, **kwargs):
            return Mock()
        def __getattr__(self, attr):
            return Mock()
    logging.basicConfig(level='DEBUG')
    endpoint = Endpoint('https://foo.bar/baz', http_client=Mock())
    endpoint.get(some='thing', somethng_else=1)
    endpoint.post(data={}, some='thing', somethng_else=1)
