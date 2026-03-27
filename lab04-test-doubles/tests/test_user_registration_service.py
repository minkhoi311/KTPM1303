from src.user_registration_service import UserRegistrationService
from src.email_service import EmailService
from unittest.mock import Mock

def test_register_send_welcome_email():
    #mock chỉ có các thuộc tính / phương thức giông EmailService
    email_service =Mock(spec=EmailService)
    registration = UserRegistrationService(email_service)

    registration.register("user@test.com")
    email_service.send_welcome.assert_called_once_with("user@test.com")