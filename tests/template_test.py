from unittest import TestCase
from templates import template


class VariableReplacement(TestCase):
    def setUp(self):
        self.line = '{{ foo }} and {{ bar }} combined make {{ baz }}'
        self.expected = '1 and 2 combined make 3'

    def test_replace_strings(self):
        context = dict([('foo', '1'), ('bar', '2'), ('baz', '3')])
        rendered = template.replace_variables(self.line, context)
        self.assertEqual(rendered, self.expected)

    def test_replace_ints(self):
        context = dict([('foo', 1), ('bar', 2), ('baz', 3)])
        rendered = template.replace_variables(self.line, context)
        self.assertEqual(rendered, self.expected)


class Rendering(TestCase):
    def setUp(self):
        self.template = ['{{ foo }} is {{ bar }}']
        self.context = {
            'foo': 'Thor',
            'bar': 'good',
            'baz': 'Loki',
            'qux': 'bad'
        }

    def test_one_line_template(self):
        rendered = template.render(self.template, self.context)
        self.assertEqual(rendered.strip(), 'Thor is good')

    def test_two_line_template(self):
        tmpl = self.template
        tmpl.append('{{ baz }} is {{ qux }}')
        rendered = template.render(tmpl, self.context)
        self.assertEqual(rendered, 'Thor is good\nLoki is bad\n')
