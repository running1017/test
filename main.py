# -*- coding: utf-8 -*-

import __future__
import datetime

print("Hello Jenkins")

t = datetime.datetime.now()

log_text = "こんにちはJenkinsさん、今日はいい天気ですね。"

with open(t.strftime("%Y%m%d%H%M%S") + ".log", 'w') as f:
    f.write(log_text)