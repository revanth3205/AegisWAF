import logging

logging.basicConfig(
    filename="firewall.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_attack(ip, attack_type, payload):
    logging.warning(f"[ATTACK] IP: {ip} | Type: {attack_type} | Payload: {payload}")

def log_info(message):
    logging.info(message)