from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

input_text = "The secret of getting ahead is"
input_ids = tokenizer.encode(input_text, return_tensors='pt')
attention_mask = torch.ones(input_ids.shape)  # 모든 토큰에 주의를 기울이도록 설정

# pad_token_id 설정
model.config.pad_token_id = model.config.eos_token_id

output = model.generate(input_ids,
                        attention_mask=attention_mask,
                        max_length=100,
                        num_return_sequences=1)
text = tokenizer.decode(output[0], skip_special_tokens=True)

print(text)
