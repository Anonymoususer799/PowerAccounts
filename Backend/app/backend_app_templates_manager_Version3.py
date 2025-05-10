from jinja2 import Environment, FileSystemLoader
import os

class TemplateManager:
    def __init__(self, templates_path='templates'):
        self.env = Environment(loader=FileSystemLoader(templates_path))

    def render_template(self, template_name, context):
        template = self.env.get_template(template_name)
        return template.render(context)

    def list_templates(self):
        return os.listdir(self.env.loader.searchpath[0])