import pandas as pd


# url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8'
url = 'http://bike.passo.co.kr/bike/index.php?part=cybershop&path=cybershop&mode=home#HIS_ID:search=%40_maker_idx%3A%40_model_idx%3A%5Emaker_idx%3D11%232315%23&page=0&order_by=&search_mode=country'
dfs = pd.read_html(url)

exchange_rate_df = dfs[1]

# 엑셀파일 경로
folder = '/Users/scottbang/MyProjects/PycharmProjects/webCrawling/excel'
excel_file = folder + "passo_data.xlsx"

exchange_rate_df.to_excel(excel_file, index=False)

print("생성파일: ", excel_file)


