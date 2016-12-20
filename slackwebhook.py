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
    # Post a simple update to slack
    #
    def post(self, text):
        payload = { "text" : text}
        status = self.__post_payload(payload)
        return status

    #
    # Posts a richly formatted post to slack
    #
    def rich_format_post(self, fallback=None, text=None, pretext=None, color=None, title=None, value=None, short=None):
        # Create a richly formatted payload
        payload = {
        "attachments":[
                {
                    "fallback": fallback,
                    "text": text,
                    "pretext": pretext,
                    "color": color,
                    "fields":[
                        {
                            "title": title,
                            "value": value,
                            "short": short
                        }
                    ]
                }
            ]
        }
        status = self.__post_payload(payload)
        return status

    #
    # Post a json payload to slack webhook url
    #
    def __post_payload(self, payload):
        response = requests.post(self.webhook_url, json=payload)
        if(response.status_code != 200):
            print("ERROR: the url %s returned a %d response code." % (self.webhook_url, response.status_code))
        return response.status_code
