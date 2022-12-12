"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import myxblock.config as config
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope


class MyXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    heading = config.heading

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the MyXBlock, shown to students
        when viewing courses.
        """
        if context is None:
            context = {}

        context['button_text'] = config.button_text

        html = self.resource_string(config.block_content_path)
        frag = Fragment(html.format(self=self, button_text=context['button_text']))
        frag.add_css(self.resource_string(config.block_content_css_path))
        frag.add_javascript(self.resource_string(config.block_content_js_path))
        # frag.initialize_js('MyXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            (f"{MyXBlock.heading}",
             """<myxblock/>
             """),
            (f"Multiple {MyXBlock.heading}",
             """<vertical_demo>
                <myxblock/>
                <myxblock/>
                <myxblock/>
                </vertical_demo>
             """),
        ]
