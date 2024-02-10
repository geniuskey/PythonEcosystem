import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# nltk.download('punkt')  # 문장 토큰화 도구 (에러 발생시 다운로드 필요)
# nltk.download('averaged_perceptron_tagger')  # 자연어 처리 모듈 (에러 발생시 다운로드 필요)
text = "The best and most beautiful things in the world cannot be seen or even touched. They must be felt with the heart."

# 토큰화
tokens = word_tokenize(text)

# 품사 태깅
tagged = pos_tag(tokens)
print(tagged)

# 명사만 추출
nouns = [word for word, pos in tagged if pos.startswith('N')]
print(nouns)
