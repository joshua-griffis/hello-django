from django.test import SimpleTestCase

# Create your tests here.


class TestHelloView(SimpleTestCase):
    def test_hello_nate(self):
        response = self.client.get("/hey/nate/")
        self.assertContains(response, "Hey, nate!")

    def test_hello_paul(self):
        response = self.client.get("/hey/paul/")
        self.assertContains(response, "Hey, paul!")

    def test_hello_me(self):
        response = self.client.get("/hey/me/")
        self.assertContains(response, "Hey, me!")
