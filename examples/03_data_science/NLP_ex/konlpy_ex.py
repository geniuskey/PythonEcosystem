from konlpy.tag import Okt

# Okt 형태소 분석기 인스턴스 생성
okt = Okt()

# 텍스트 정의
text = "한국어 분석을 시작합니다. 재미있어요!"

# 형태소 분석
morphs = okt.morphs(text)
print("형태소:", morphs)

# 품사 태깅
pos = okt.pos(text)
print("품사 태깅:", pos)

# 명사 추출
nouns = okt.nouns(text)
print("명사:", nouns)
