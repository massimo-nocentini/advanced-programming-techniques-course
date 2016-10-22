
class WasRun:

    def __init__(self, name):
        self.was_run = False

    def test_method(self):
        self.was_run = True 
    
    def run(self):
        # lots of refactorings has this feel -- separating two parts so you
        # work on them separately. If they go back together when you are finished, fine;
        # if not, you can leave them separate.
        self.test_method()
