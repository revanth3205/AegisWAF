from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import requests
import json
from rule_engine import RuleEngine
from rate_limiter import RateLimiter
from logger import log_attack, log_info

with open("config.json") as f:
    config = json.load(f)

rule_engine = RuleEngine(config)
rate_limiter = RateLimiter(config["max_requests_per_minute"])

class AdvancedWAF(BaseHTTPRequestHandler):

    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()

    def handle_request(self):
        client_ip = self.client_address[0]

        # IP Blacklist Check
        if client_ip in config["blacklisted_ips"]:
            self.block_request("Blacklisted IP")
            return

        # Rate Limiting
        if not rate_limiter.is_allowed(client_ip):
            self.block_request("Rate Limit Exceeded")
            return

        # Read request body
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode() if content_length > 0 else ""

        full_request_data = self.path + body

        # Rule Inspection
        anomaly_score, attack_type = rule_engine.inspect(full_request_data)

        if anomaly_score >= config["anomaly_threshold"]:
            log_attack(client_ip, attack_type, full_request_data)
            self.block_request(f"{attack_type} Detected")
            return

        # Forward Safe Request
        self.forward_request(body)

    def forward_request(self, body):
        backend_url = config["backend_url"] + self.path

        try:
            if self.command == "GET":
                response = requests.get(backend_url)
            else:
                response = requests.post(backend_url, data=body)

            self.send_response(response.status_code)
            self.end_headers()
            self.wfile.write(response.content)

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Backend Error")

    def block_request(self, reason):
        self.send_response(403)
        self.end_headers()
        self.wfile.write(f"Blocked by WAF: {reason}".encode())

if __name__ == "__main__":
    server = ThreadingHTTPServer(('', 8080), AdvancedWAF)
    print("Advanced WAF running on port 8080")
    server.serve_forever()