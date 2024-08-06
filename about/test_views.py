from django.test import TestCase
from django.urls import reverse
from .forms import CollaborateForm
from .models import About

class TestAboutViews(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About title",
            content="here are some words"
            )
        self.about_content.save()

    def test_about_render_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIn(b"here are some words", response.content)
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)

    def test_succesfull_collab_request_submission(self):
        """Verifies if a collaboration request has been successfully sent"""
        post_data = {'name': 'hello', 'email': 'hello@hello.com', 'message': 'here are some words'}
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Collaboration request received! I endeavour to respond within 2 working days.",
            response.content
        )
