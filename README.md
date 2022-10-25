# Cryptocurrency-Automated-Trading
基於Binance API虛擬貨幣回測、自動化交易平台

專案中主要分為回測、自動化交易兩個功能。回測中資料使用「Binance API」獲取過往資料，擬定交易策略後使用分佈式計算加速得到結果。在選擇上可以設定BTC、ETH、ADA、SOL幣種，設計不同MA、KD區間條件來調整參數，並根據結果來判斷此策略的好壞，以此作為自動化交易的策略參考基礎。

![Credit by 夏念凱、陳思齊](https://user-images.githubusercontent.com/61962782/197727281-234ae9a9-0cea-402d-b351-301473d754f2.png)
![Credit by 夏念凱、陳思齊](https://user-images.githubusercontent.com/61962782/197727747-a17b5da5-ee6e-404d-9600-33c01d41520c.png)


### 架構
1. 使用HADOOP下HDFS存儲巨量資料
2. 依據使用者規則進行回測
3. Spring Boot 網站 + Boostrap 呈現網站 



## Contributor
劉奕欣 t107590009@ntut.org.tw
謝宗翰 t107590040@ntut.org.tw
