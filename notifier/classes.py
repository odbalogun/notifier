import datetime


class Notification:
    """
    Class representing a single notification item.
    It has the following attributes: title, subtitle, message, duration(seconds), timer(seconds), date_created
    """
    def __init__(self, duration, timer, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.duration = duration
        self.timer = timer
        self.date_created = datetime.datetime.now()

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Notification duration must be an integer")
        self._duration = value

    @property
    def timer(self):
        return self._timer

    @timer.setter
    def timer(self, value):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Timer must be an integer")
        self._timer = value


class Alert(object):
    ALERT_TYPES = ['MAC_OS']

    def __init__(self, alert_type, notification):
        self.alert_type = alert_type
        self._notification = notification

    @property
    def alert_type(self):
        return self._alert_type

    @alert_type.setter
    def alert_type(self, value):
        if value not in Alert.ALERT_TYPES:
            raise ValueError('Invalid alert type provided')
        self._alert_type = value
