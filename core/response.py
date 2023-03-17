import orjson


class APIResponse:
    def __init__(self, status, message, data=None, **kwargs):
        """
        A class for api responses that can be converted to json

        :param status:
        :param message:
        :param data:
        :param kwargs:
        """
        self.status = status
        self.message = message
        self.data = data
        self.__dict__.update(kwargs)
        self.meta = {'version': '1.0.0', 'author': 'AyberkEnis.com.tr', 'github': 'https://github.com/ayberkenis/ayberkenis-api'}

    def to_json(self):
        return orjson.dumps(self.__dict__)

    def to_dict(self):
        return self.__dict__