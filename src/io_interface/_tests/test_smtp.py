import unittest
from unittest.mock import Mock, patch
from mymodule import send


class TestSendMail(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_send(self, mock_smtp):
        mock_smtp_instance = mock_smtp.return_value
        mock_smtp_instance.login.return_value = (235, b'2.7.0 Accepted')
        send(subject='Test Subject', body='Test Body')
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        mock_smtp_instance.starttls.assert_called_once_with()
        mock_smtp_instance.login.assert_called_once_with(
            'test_user', 'test_password')
        mock_smtp_instance.sendmail.assert_called_once_with(
            'test_user', 'one.last.bit@gmail.com', mock_smtp_instance.send_message.return_value.as_string.return_value
        )
        mock_smtp_instance.quit.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
