import re
import uuid
import random
import string

from django import template
from datetime import datetime


class FormFieldNode(template.Node):
    """"
    Add the widget type to a BoundField. Until 3.1, Django did not make this available by default.
    Used by `oscar.templatetags.form_tags.annotate_form_field`
    """
    def __init__(self, field_str):
        self.field = template.Variable(field_str)

    def render(self, context):
        field = self.field.resolve(context)
        if not hasattr(field, 'widget_type') and hasattr(field, 'field'):
            field.widget_type = re.sub(r'widget$|input$', '', field.field.widget.__class__.__name__.lower())
        return ''
    
def id_generator(size=8, chars=string.ascii_uppercase 
                    + datetime.now().strftime('%Y%m%d%H%M%S') 
                    + str(uuid.uuid4()).replace("-","")):
    return "DD"+''.join(random.choice(chars) for _ in range(size))