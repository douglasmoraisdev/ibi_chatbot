import json


class FacebookRichMessages():
    """Generate Facebook Messeger rich messages format"""

    def __init__(self):
        pass

    def button_list(self, title, options=[]):
        """Return a button list rich message

        Loads a template json file containt the facebook list message format
        and render with parameters

        @params:
        - title(string) = The title of the list
        - options(dict list) = A dict list of options of the buttons
            options dict format:
            - type: (default: postback)
            - title: Label of the button
            - payload: Value callback on selected
        """
        # Open the Facebook JSON template
        with open('rich_messages/templates/facebook_base_list.json') as\
                _json_fb_list:
            _button_list = json.loads(_json_fb_list.read())

        # Render the Title
        _button_list["facebook"][
            "attachment"][
            "payload"]["text"] = title

        # Render the buttons list
        _button_list["facebook"][
            "attachment"][
            "payload"]["buttons"] = options

        return _button_list

    def address_link(self, image_url, url, complete_address):
        """Return a button list rich message

        Loads a template json file containt the facebook list message format
        and render with parameters

        @params:
        - title(string) = The title of the list
        - options(dict list) = A dict list of options of the buttons
            options dict format:
            - type: (default: postback)
            - title: Label of the button
            - payload: Value callback on selected
        """
        # Open the Facebook JSON template
        with open('rich_messages/templates/facebook_base_address.json') as\
                _json_fb_add_link:
            _address_link = json.loads(_json_fb_add_link.read())

        # Render the image_url
        _address_link["facebook"][
            "attachment"][
            "payload"]["elements"][0]["image_url"] = image_url

        # Render the Title
        _address_link["facebook"][
            "attachment"][
            "payload"]["elements"][0]["title"] = complete_address

        # Render the url of the map
        _address_link["facebook"][
            "attachment"][
            "payload"]["elements"][0][
                "default_action"]["url"] = url

        return _address_link


