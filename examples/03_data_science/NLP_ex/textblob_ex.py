from textblob import TextBlob

text = "TextBlob is amazingly simple to use. What a great tool!"
blob = TextBlob(text)

# 감성 분석
print(blob.sentiment)
