from datetime import datetime
class CurrentDate:
    def current_month(self):
        current_time = datetime.now()
        return current_time.month
