import slackweb

webhook_url = "https://"
notice_text = "hogehoge"

slack = slackweb.Slack(url=webhook_url)
slack.notify(text=notice_text)
