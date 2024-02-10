from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax
import torch

# 모델과 토크나이저 로드
tokenizer = BertTokenizer.from_pretrained('snunlp/KR-BERT-char16424')
model = BertForSequenceClassification.from_pretrained('snunlp/KR-BERT-char16424')

# 분석할 문장
sentences = ["이 영화 정말 재미있어요!", "이 영화 별로예요."]

for sent in sentences:
    inputs = tokenizer(sent, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    probs = softmax(outputs.logits, dim=-1)
    positive_prob = probs[:, 1].item()
    print(f"Sentence: '{sent}' - Positive Probability: {positive_prob:.4f}")
