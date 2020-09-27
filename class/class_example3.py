class Sample:
    val = 100

    def demo(self):
        self.do_print('call method')

    def do_print(self, msg):
        print("{0}".format(msg))
        print(("{0}".format(self.val)))

sample = Sample()
sample.demo()
