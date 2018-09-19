class Actions(object):

    def ac_hello(self, request):

        print(request)
        return 'Hello response'