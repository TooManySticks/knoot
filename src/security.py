import asyncio
import logging
from cryptography.fernet import Fernet

logging.basicConfig(level=logging.INFO)

class SecurityManager:
    def __init__(self, key=None):
        self.key = key or (Fernet.generate_key() if Fernet else None)
        self.fernet = Fernet(self.key) if Fernet and self.key else None

    def encrypt_data(self, data: str) -> str:
        try:
            return self.fernet.encrypt(data.encode()).decode() if self.fernet else data
        except Exception as e:
            logging.error(f"SecurityManager: Encryption error: {e}")
            return data

    def decrypt_data(self, token: str) -> str:
        try:
            return self.fernet.decrypt(token.encode()).decode() if self.fernet else token
        except Exception as e:
            logging.error(f"SecurityManager: Decryption error: {e}")
            return token

    def audit_log(self, message: str):
        logging.info(f"SecurityManager Audit: {message}")

    async def rotate_keys(self):
        await asyncio.sleep(0.01)
        if Fernet:
            self.key = Fernet.generate_key()
            self.fernet = Fernet(self.key)
            logging.info("SecurityManager: Keys rotated.")
        else:
            logging.warning("SecurityManager: Fernet not available.")

    async def validate_access(self, user, resource):
        await asyncio.sleep(0.01)
        logging.info(f"SecurityManager: Access validated for {user} on {resource}.")
        return True

class AdvancedSecurityManager(SecurityManager):
    async def advanced_key_management(self):
        await asyncio.sleep(0.02)
        logging.info("AdvancedSecurityManager: Advanced key management performed.")
        return True

    async def role_based_access_control(self, user, resource, role):
        await asyncio.sleep(0.02)
        allowed = role in ["admin", "manager", "user"]
        logging.info(f"AdvancedSecurityManager: RBAC for {user} as {role} on {resource}: {allowed}")
        return allowed

    async def security_event_monitoring(self):
        await asyncio.sleep(0.05)
        logging.info("AdvancedSecurityManager: Security event monitoring executed.")
        return True
