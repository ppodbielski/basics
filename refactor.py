class Extractor:
    def __init__(self, source):
        self.source = source

    def extract(self):
        results = []
        for token in self.source.split():
            results.append(token.upper())
        self.results = results

data_source = 'unu du\ntri\tkvar'
ex = Extractor(data_source)
ex.extract()
print(ex.results)


class Extractor:
    def __init__(self, source):
        self.source = source

    def extract(self):
        results = []
        for token in self.source.split():
            results.append(token.upper())
        return results

data_source = 'unu du\ntri\tkvar'
print(Extractor(data_source).extract())

class Extractor:
    @staticmethod
    def extract(data_source):
        results = []
        for token in data_source.split():
            results.append(token.upper())
        return results

data_source = 'unu du\ntri\tkvar'
print(Extractor.extract(data_source))

def extract(data_source):
    results = []
    for token in data_source.split():
        results.append(token.upper())
    return results

print(extract(data_source))

def extract(source):
    for token in source.split():
        yield token.upper()

data_source = 'unu du\ntri\tkvar'
print(list(extract(data_source)))