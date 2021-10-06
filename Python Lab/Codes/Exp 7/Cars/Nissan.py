class Nissan:
    def __init__(self):
        self.models = ['altima', '370z', 'cube', 'rogue']
    def outModels(self):
        print('These are the available models for Nissan')
        for model in self.models:
            print('\t%s ' % model)