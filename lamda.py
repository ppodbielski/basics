def silnia_rek(n):
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

print(silnia_rek(6))

def silnia_it(n):
    r = 1
    for i in range(1,n+1):
        r *= i
    return r
print(silnia_it(6))

f = lambda x: x * f(x-1) if x!=0 else 1

print(f(6))

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