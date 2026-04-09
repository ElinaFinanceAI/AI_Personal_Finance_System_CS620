class Alerts:
    def send_alert(self, total, limit):
        if total > limit:
            return "Alert: Budget exceeded"
        else:
            return "No alert"