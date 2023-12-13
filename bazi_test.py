import datetime
import sys
sys.path.append(r'./bazi') # 將上一層路徑加入模組搜尋路徑
import bazi

now = datetime.datetime.now()
options = bazi.option()
options.year = 1985
options.month = 9
options.day = 5
options.time = 9
options.n = True
bazi.main(options)