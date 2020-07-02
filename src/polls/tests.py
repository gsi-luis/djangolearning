from django.test import TestCase
from django.utils import timezone, datetime_safe
from .models import Question
import datetime
from django.urls import reverse


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        future_question = create_question(question_text="Question test future", days=30)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        old_question = create_question(question_text="Question test old", days=-30)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        recent_question = create_question(question_text="Question test now", days=0)
        self.assertEqual(recent_question.was_published_recently(), True)


class QuestionIndexTests(TestCase):
    def test_index_view_with_no_questions(self):
        response = self.client.get(reverse('polls:generic_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_index_view_with_a_past_question(self):
        create_question(question_text="Question test old", days=-30)
        response = self.client.get(reverse('polls:generic_index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['question_list'], ['<Question: Question test old>'])

    def test_index_view_with_a_future_question(self):
        create_question(question_text="Question test future", days=30)
        create_question(question_text="Question test old", days=-30)
        response = self.client.get(reverse('polls:generic_index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['question_list'], ['<Question: Question test old>'])

    def test_index_view_with_two_past_questions(self):
        create_question(question_text="Question test old 10 days", days=-10)
        create_question(question_text="Question test old 5 days", days=-5)
        response = self.client.get(reverse('polls:generic_index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['question_list'], [
            '<Question: Question test old 5 days>',
            '<Question: Question test old 10 days>'
        ])


class QuestionDetailsView(TestCase):
    def test_detail_with_a_past_question(self):
        question = create_question(question_text="Question old", days=-10)
        response = self.client.get(reverse('polls:generic_detail', args=(question.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question.question_text)

    def test_detail_with_a_future_question(self):
        question = create_question(question_text="Question old", days=10)
        response = self.client.get(reverse('polls:generic_detail', args=(question.id,)))
        self.assertEqual(response.status_code, 404)
