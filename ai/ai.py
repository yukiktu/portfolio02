import re

from ai.import_text import ImportText
from ai.markov import Markov
from ai.morpheme_analyzer import MorphemeAnalyzer
from ai.fixed_phrase import FixedPhrase

class Ai:
    def ai_answer(input_text):
        import_text = ImportText('library/import.txt')
        fixed_phrase = FixedPhrase('library/pattern.csv')
        morpheme_analyzer = MorphemeAnalyzer()
        markov = Markov(morpheme_analyzer.analyze(import_text.read()))
        if (re.match('@|＠', input_text)):
            add_text = re.sub('^@|^＠', '', input_text)
            import_text.add(add_text)
            markov.add(morpheme_analyzer.analyze(add_text))
            output_text = "教えてくれてありがとう"
        else:
            output_text = fixed_phrase.answer(input_text)
        if output_text == "":
            nouns = morpheme_analyzer.extract_noun(input_text)
            output_text = markov.answer(nouns)
        if output_text == "":
            output_text = "理解できませんでした。。。<br />Read Meを参考に新しい情報をインプットしてください。"
        return output_text
