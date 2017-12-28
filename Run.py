# -*- coding: utf8 -*-

import getPrice
import data

print data.select_env()
getPrice.get_price(data.ResultFileName)
