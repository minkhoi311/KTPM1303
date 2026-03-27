from .email_service import EmailService

class UserRegistrationService:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def register(self, email: str) -> None:
        self.email_service.send_welcome(email)