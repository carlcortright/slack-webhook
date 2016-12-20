################################################################################
# Setup file for the slackwebhook package.
#
# Author: Carl Cortright
# Date: 12/20/2016
#
################################################################################
from distutils.core import setup
setup(
  name = 'slackwebhook',
  packages = ['slackwebhook'],
  version = '0.2',
  description = 'Easy interface for posting to a slack webhook',
  author = 'Carl Cortright',
  author_email = 'ckcortright@gmail.com',
  url = 'https://github.com/carlcortright/slack-webhook',
  download_url = 'https://github.com/carlcortright/slack-webhook/tarball/0.2', # I'll explain this in a second
  keywords = ['slack', 'webhook', 'bot', 'easy'],
  classifiers = [],
  install_requires=[
        "requests",
    ],
)
