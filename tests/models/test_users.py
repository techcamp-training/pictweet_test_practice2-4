from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

class UserModelTest(TestCase):
    def test_nickname_cannot_be_blank(self):
        User = get_user_model()
        test_user = User(nickname="Test User", email="testuser@example.com", password="techcamp2024")
        test_user.nickname = ""

        with self.assertRaises(ValidationError) as cm:
            test_user.full_clean()

        self.assertIn('nickname', cm.exception.message_dict)
        self.assertEqual(cm.exception.message_dict['nickname'], ["このフィールドは空ではいけません。"])

    def test_email_cannot_be_blank(self):
        User = get_user_model()
        test_user = User(nickname="Test User", email="testuser@example.com", password="techcamp2024")
        test_user.email = ""

        with self.assertRaises(ValidationError) as cm:
            test_user.full_clean()

        self.assertIn('email', cm.exception.message_dict)
        self.assertEqual(cm.exception.message_dict['email'], ["このフィールドは空ではいけません。"])
