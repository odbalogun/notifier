import datetime


class Notification:
    """
    Class representing a single notification item.
    It has the following attributes: title, message, timer(seconds), date_created
    """
    def __init__(self, timer: int, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.timer = timer
        self.date_created = datetime.datetime.now()

    @property
    def timer(self):
        return self._timer

    @timer.setter
    def timer(self, value: int):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Timer must be an integer")
        self._timer = value


class Alert(object):
    ALERT_TYPES = {'mac': 'MAC_OS'}

    def __call__(self, *args, **kwargs):
        import os
        os.system("""
            osascript -e 'display notification "{}" with title "{}"'
        """.format(self._notification.message, self._notification.title))

    def __init__(self, alert_type: str, notification: Notification):
        self.alert_type = alert_type
        self._notification = notification

    @property
    def alert_type(self):
        return self._alert_type

    @alert_type.setter
    def alert_type(self, value: str):
        if value not in Alert.ALERT_TYPES.values():
            raise ValueError('Invalid alert type provided')
        self._alert_type = value
