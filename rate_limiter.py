import time

class RateLimiter:
    def __init__(self, max_requests):
        self.requests = {}
        self.max_requests = max_requests

    def is_allowed(self, ip):
        current_time = time.time()

        if ip not in self.requests:
            self.requests[ip] = []

        # Remove old requests
        self.requests[ip] = [
            t for t in self.requests[ip] if current_time - t < 60
        ]

        if len(self.requests[ip]) >= self.max_requests:
            return False

        self.requests[ip].append(current_time)
        return True