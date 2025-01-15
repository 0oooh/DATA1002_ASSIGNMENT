# 필요한 라이브러리 임포트
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
data = pd.read_csv('SDG_goal3_clean.csv')  # 파일 경로를 자신의 파일 경로로 수정하세요

# 종속 변수 설정
y = data['Universal health coverage (UHC) service coverage index']

# 독립 변수 목록에서 종속 변수를 제외
X = data.drop(columns=['Universal health coverage (UHC) service coverage index'])

# 시각화: 각 독립 변수와 종속 변수의 관계 산점도 그리기
for column in X.columns:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data[column], y=y)
    plt.title(f'Relationship between {column} and UHC index')
    plt.xlabel(column)
    plt.ylabel('UHC index')
    plt.show()
