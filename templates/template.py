import io
import re
from typing import Dict, Iterable


VARIABLE_RE = re.compile(r'{{\s[a-zA-Z0-9.]*\s}}')


def render(template: Iterable, context: Dict) -> str:
    """Render a document from template and context.
    """
    with io.StringIO() as output:
        for line in template:
            output.write(replace_variables(line, context))
        result = output.getvalue()
    return result


def replace_variables(text: str, context: Dict) -> str:
    """Replace variables in a string with context data.
    """
    result = text
    for match in VARIABLE_RE.finditer(text):
        element = match.group()
        var = element.strip('{} ')
        result = result.replace(element, str(context[var]))
    return result
