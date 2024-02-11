import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")
df = sns.load_dataset('tips')

# 산점도 그래프
sns.relplot(df, x='total_bill', y='tip',
            hue="day", palette="Set1")

# 분포를 시각화하는 히스토그램
sns.displot(df, x='total_bill', hue="day", palette="pastel")

# 범주형 데이터를 시각화하는 박스 플롯
sns.catplot(df, x='day', y='total_bill', kind='box', hue="day", palette="Set3")

plt.show()
