import json


class GoogleRichMessages():
    """Generate Google Messeger rich messages format"""

    def __init__(self):
        pass

    def button_list(self, title, options=[]):
        """Return a button list rich message

        Loads a template json file containt the google list message format
        and render with parameters

        @params:
        - title(string) = The title of the list
        - options(dict list) = A dict list of options of the buttons
            options dict format:
            - type: (default: postback)
            - title: Label of the button
            - payload: Value callback on selected
        """
        # Open the google JSON template
        with open('rich_messages/templates/google_base_list.json') as\
                _json_fb_list:
            _button_list = json.loads(_json_fb_list.read())

        # Render the Title
        '''
        _button_list["google"][
            "attachment"][
            "payload"]["text"] = title

        # Render the buttons list
        _button_list["google"][
            "attachment"][
            "payload"]["buttons"] = options
        '''

        return _button_list
