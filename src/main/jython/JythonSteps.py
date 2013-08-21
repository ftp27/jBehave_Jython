class Simple(object):
    @java
    def __init__(self):

    @java(String, String)
    def firstWord(self, param):
        return param.split(' ')[0]