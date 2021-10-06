class Audi:
    def __init__(self):
        self.models = ['q7', 'a6', 'a8', 'a3']
    def outModels(self):
        print('These are the available models for Audi')
        for model in self.models:
            print('\t%s ' % model)