################################################################################
# Tests for the easy slackwebhook class.
#
# Author: Carl Cortright
# Date: 12/20/2016
#
################################################################################
import unittest
from slackwebhook import slackwebhook


class TestSlackWebhook(unittest.TestCase):
    webhook = slackwebhook("https://hooks.slack.com/services/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")

    def test_simple_post(self):
        self.assertEqual(self.webhook.post("Testing simple text post"), 200)

    def test_richformat_post(self):
        self.assertEqual(self.webhook.rich_format_post(text="test with only fallback"), 200)
        self.assertEqual(self.webhook.rich_format_post(fallback="test with fallback", text="test with fallbacks"), 200)
        self.assertEqual(self.webhook.rich_format_post(fallback="Full rich format test", text="Full rich format test", pretext="Checkout this cool thing:", title="Cool Stuff!", value="Here's some more info", short=False, color="#000000"), 200)
        self.assertEqual(self.webhook.rich_format_post(fallback="Full rich format test", text="Full rich format test", pretext="Checkout this cool thing:", title="Cool Stuff!", value="Short is true on this one", short=True, color="#00FF00"), 200)

    def test_link(self):
        self.assertEqual(self.webhook.post("This is to test links: <https://www.google.com|Link to Google>"), 200)

if __name__ == '__main__':
    unittest.main()
