################################################################################
# Easy python interface for posting updates to a slack channel. Usage in README.
#
# Author: Carl Cortright
# Date: 12/20/2016
#
################################################################################
import requests

class slackwebhook:
    webhook_url = ""

    #
    # Default initializer
    #
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    #
    # Post update to slack
    #
    def post(self, text):
        payload = { "text" : text}
        print(payload)
        response = requests.post(self.webhook_url, json=payload)
        if(response.status_code != 200):
            print("ERROR: the url %s returned a %d response code." % (self.webhook_url, response.status_code))
        return response.status_code

    #
    # Posts a richly formatted post to slack
    #
    def rich_format_post(self, text=None, fallback=None, pretext=None, color=None, title=None, value=None, short=None):
        # Create a richly formatted payload
        payload = {
        "attachments":[
                "fallback": fallback,
                "text": text,
                "pretext": pretext,
                "color": color,
                "fields":[
                    {
                        "title": title,
                        "value": value,
                        "short", short
                    }
                ]
            ]
        }
        status = self.__post_payload(payload)
        return status

    #
    # Post the json payload to slack
    #
    def __post_payload(self, payload):
        response = requests.post(self.webhook_url, json=payload)
        if(response.status_code != 200):
            print("ERROR: the url %s returned a %d response code." % (self.webhook_url, response.status_code))
        return response.status_code
