import pyupbit
import numpy as np

# 변동성 돌파전략에서 매수가를 구하기 위함
# 어제의 고가와 저가의 차이인 '변동폭'
# 에 k배만큼 상승이 일어났을때 매수를 진행함
#  매수가를 구해줌+ 오늘의 시가를 더함 기본값 k -0.5 설정

# OHLCV open(시가)high(고가)low(저가)close(종가)vol(거래량)에 대한 데이터

df = pyupbit.get_ohlcv("KRW-BTC", count=7)
print(df)

# 변동성 돌파 기준 범위 계산 (고가 - 저가 ) * k값
df['range'] = (df['high'] - df['low']) * 0.5

#  range 컬럼은 한칸씩 밑으로 내림 (.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.005

#  np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

#  누적 곱 계산.cumprod() => 누적 수익률
df['hpr'] = df['ror'].cumprod()

#  Draw Down 계산 ( 누적 최대 값과 현제 hpr 차이 / 누적 최대값 *100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# Mdd 계산
print("MDD(%): ", df['dd'].max())

# 엑셀로 출력
df.to_excel("dd.xlsx")

# # /////////////////////////////////////////

# import pyupbit
# import numpy as np

# # OHLCV(open, high, low, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
# df = pyupbit.get_ohlcv("KRW-BTC", count=7)

# # 변동폭 * k 계산, (고가 - 저가) * k값
# df['range'] = (df['high'] - df['low']) * 0.5

# # target(매수가), range 컬럼을 한칸씩 밑으로 내림(.shift(1))
# df['target'] = df['open'] + df['range'].shift(1)

# # ror(수익률), np.where(조건문, 참일때 값, 거짓일때 값)
# df['ror'] = np.where(df['high'] > df['target'],
#                      df['close'] / df['target'],
#                      1)

# # 누적 곱 계산(cumprod) => 누적 수익률
# df['hpr'] = df['ror'].cumprod()

# # Draw Down 계산 (누적 최대 값과 현재 hpr 차이 / 누적 최대값 * 100)
# df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# #MDD 계산
# print("MDD(%): ", df['dd'].max())

# #엑셀로 출력
# df.to_excel("dd.xlsx")