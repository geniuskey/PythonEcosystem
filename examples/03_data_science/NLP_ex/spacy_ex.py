import spacy

# 영어 모델 로드
nlp = spacy.load("en_core_web_sm")

# 텍스트 샘플
text = "SpaCy is an excellent tool for NLP in Python."

# 텍스트 처리
doc = nlp(text)

# 토큰화 및 품사 태깅
for token in doc:
    print(token.text, token.pos_)

# 개체명 인식
for ent in doc.ents:
    print(ent.text, ent.label_)
