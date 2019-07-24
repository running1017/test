# -*- coding: utf-8 -*-

import __future__
import datetime

print("Hello Jenkins")

t = datetime.datetime.now()

log_text = "Hi, Mr.Ogawa.\nIt is great cloudy day!"

with open(t.strftime("%Y%m%d%H%M%S") + ".log", 'w') as f:
    f.write(log_text)