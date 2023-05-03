

import standby


# print(standby.query("give a short meaning of life"))


def defaultM(name, addy = "1240", temp = 50):
    print(name + " lives at " + addy + " and the temperature is " + str(temp) + " degrees")

defaultM(name = "quang")
defaultM("quang", addy = "holcombe")
defaultM("jack", temp = 100)