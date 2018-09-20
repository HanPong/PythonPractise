class TV:
    def __init__(self):
        self.channel=1
        self.volumeLevel=1
        self.on=False

    def turnOn(self):
        self.on=True

    def turnOff(self):
        self.on=False

    def getChannel(self):
        return self.channel

    def setChannel(self,channel):#更改初始值
        if self.on and 1<=self.channel<=120:
            self.channel=channel#注意这里

    def getVolumeLevel(self):
        return self.volumeLevel

    def setVolume(self,volumnLevel):
        if self.on and\
            1<=self.volumeLevel<=7:
            self.volumeLevel=volumnLevel

    def channelUp(self):
        if self.on and self.channel<120:
            self.channel+=1

    def channelDown(self):
        if self.on and self.channel>1:
            self.channel-=1

    def volumnUp(self):
        if self.on and self.volumeLevel<7:
            self.volumeLevel+=1

    def volumnDown(self):
        if self.on and self.volumeLevel>1:
            self.volumeLevel-=1


