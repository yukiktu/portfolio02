import MeCab

class MorphemeAnalyzer:
    def analyze(self, text):
        return MeCab.Tagger("-Owakati").parse(text).rstrip(" \n").split(" ")

    def extract_noun(self, text):
        nouns = []
        for chunk in MeCab.Tagger().parse(text).splitlines()[:-1]:
            (surface, feature) = chunk.split('\t')
            if feature.startswith('名詞'):
                nouns.append(surface)
        return nouns
