from unittest import TestCase
from templates import template


class TemplateTests(TestCase):
    def setUp(self):
        self.template = '{{ foo }} and {{ bar }} combined make {{ baz }}'
        self.wanted = '1 and 2 combined make 3'

    def test_replace_strings(self):
        context = dict([('foo', '1'), ('bar', '2'), ('baz', '3')])
        rendered = template.replace_variables(self.template, context)
        self.assertEqual(rendered, self.wanted)

    def test_replace_ints(self):
        context = dict([('foo', 1), ('bar', 2), ('baz', 3)])
        rendered = template.replace_variables(self.template, context)
        self.assertEqual(rendered, self.wanted)
