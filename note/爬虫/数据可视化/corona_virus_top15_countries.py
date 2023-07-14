import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 加载各国数据
datas = pd.read_json('./corona_virus.json')

lastest_day_data = datas[datas.dateId == (datas.dateId.max()-1)]
print(lastest_day_data)

confirmedCount_top15_country_names = lastest_day_data.sort_values(by='confirmedCount', ascending=False).head(15)

top15_country_datas = datas[datas.provinceName.isin(confirmedCount_top15_country_names)]

final_data = top15_country_datas.pivot_table(values='currentConfirmedCount', index='dateId', columns='provinceName')

final_data.fillna(0, inplace=True)
print(final_data)


