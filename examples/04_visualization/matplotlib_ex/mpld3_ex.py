import matplotlib.pyplot as plt
import mpld3

# 샘플 데이터로 그래프 생성
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], marker='o')

# mpld3를 사용하여 HTML로 변환
mpld3_html = mpld3.fig_to_html(fig)

# HTML 파일로 저장하거나 웹에서 직접 렌더링 할 수 있습니다.
with open("example_graph.html", "w") as f:
    f.write(mpld3_html)
