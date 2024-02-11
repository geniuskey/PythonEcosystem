from barcode import EAN13
from barcode.writer import ImageWriter

# 바코드 번호 (EAN-13 포맷은 12자리 숫자 필요. 마지막 체크섬은 자동 계산됨)
number = '590123412345'

# 바코드 생성 및 이미지 파일로 저장
ean = EAN13(number, writer=ImageWriter())
ean.save('ean13_barcode')
