import mplfinance as mpf
import pandas as pd

# 데이터 불러오기
# 데이터는 'Date', 'Open', 'High', 'Low', 'Close', 'Volume' 컬럼을 포함해야 함
df = pd.read_csv('mplfinance_sample.csv', index_col=0, parse_dates=True)

# 캔들스틱 차트 생성
mpf.plot(df, type='candle', style='charles',
         title='Stock Price',
         ylabel='Price ($)',
         volume=True)
