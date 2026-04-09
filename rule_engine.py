import re

class RuleEngine:

    def __init__(self, config):
        self.config = config

    def inspect(self, data):
        anomaly_score = 0
        attack_type = None

        if self.config["rules"]["sql_injection"]:
            if self.detect_sqli(data):
                anomaly_score += 3
                attack_type = "SQL Injection"

        if self.config["rules"]["xss"]:
            if self.detect_xss(data):
                anomaly_score += 2
                attack_type = "XSS"

        if self.config["rules"]["command_injection"]:
            if self.detect_cmd_injection(data):
                anomaly_score += 3
                attack_type = "Command Injection"

        return anomaly_score, attack_type

    def detect_sqli(self, data):
        patterns = [
            r"(\bUNION\b)", r"(\bSELECT\b)", r"(\bDROP\b)",
            r"(\bINSERT\b)", r"(\bOR\b.+\=)"
        ]
        return any(re.search(p, data, re.IGNORECASE) for p in patterns)

    def detect_xss(self, data):
        patterns = [
            r"<script.*?>.*?</script>",
            r"javascript:",
            r"onerror="
        ]
        return any(re.search(p, data, re.IGNORECASE) for p in patterns)

    def detect_cmd_injection(self, data):
        patterns = [
            r";\s*\b(ls|cat|whoami|id)\b",
            r"\|\|",
            r"&&"
        ]
        return any(re.search(p, data, re.IGNORECASE) for p in patterns)