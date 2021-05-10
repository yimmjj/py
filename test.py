import pyupbit
access = "5bKsXTpcWtSkcE1srpJJdRxxu9oaGJxFjS6yJyhR"          # 본인 값으로 변경
secret = "kJSfVVwhA1v850uBcnGAmRIan9cOZ6qN2mNCuxVa"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)
print(upbit.get_balance("KRW-DOGE"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회