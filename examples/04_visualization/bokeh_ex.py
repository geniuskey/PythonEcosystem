from bokeh.plotting import figure, show

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# 빈 캔버스 생성
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# 라인 그래프 추가
p.line(x, y, legend_label="Temp.", line_width=2)

# 결과 보여주기
show(p)
