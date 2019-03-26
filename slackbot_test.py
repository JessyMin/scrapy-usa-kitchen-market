from slacker import Slacker


token = "xoxb-390435277542-585956014535-kD2EiZtRs2T6SNg91qG8Nn9t"
slack = Slacker(token)

slack.chat.post_message("#random", "Hi, I am spider.")
#slack.chat.post_message("#random", "Hi, I am spider.", as_user=True)
