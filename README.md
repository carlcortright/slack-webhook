# Easy Slack Webhook

> A simple python package for posting messages to slack channels.

### Use cases

Slack webhooks are an easy way to get push notifications on mobile and desktop.

At Foundry Group we are using this package to push news about our portfolio companies to a slack channel dedicated to portfolio company news.

Personally, I am using this package to push notifications about my AI trading algorithms to a personal slack channel (trade/price updates etc.).

### Installing

Install with pip:

`pip install slackwebhook`

### Usage

First, [create a slack webhook ](https://my.slack.com/services/new/incoming-webhook/) to the channel you want, and save the url.

To post a simple update to slack using the url you just generated.

```
import slackwebhook

mywebhook = slackwebhook("<my webhook url>")
mywebhook.post("Testing simple text post")

```

To post rich-text posts:

```
import slackwebhook

mywebhook = slackwebhook("<my webhook url>")
mywebhook.rich_format_post(fallback="Full rich format test", text="Full rich format test", pretext="Checkout this cool thing:", title="Cool Stuff!", value="Here's some more info", short=False, color="#000000")
```


### Credits

Thanks to Peter Downs for his awesome tutorial [about how to publish to pypi](http://peterdowns.com/posts/first-time-with-pypi.html).

&copy; Carl Cortright 2016
