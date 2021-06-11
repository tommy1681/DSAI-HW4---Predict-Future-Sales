# DSAI-HW4---Predict-Future-Sales


* 執行方法
  * python lightgbm_train.py --train train_pre_another.csv --test test_pre_another.csv --output output.csv
  * train_pre_another.csv為預處理過的訓練資料
  * test_pre_another.csv為預處理過的測試資料
  * output output.csv為預測資料之檔名
 
* 方法說明
  * 本作業分成兩個檔案
  * 一個是模型訓練與預測的檔案lightgbm_train.py
  * 一個是產生欲處理過後之資料的檔案another.py
  
  * lightgbm_train.py需讀取以處理過後之訓練檔案與測試檔案
  * 
  * another.py為前處理之檔案，在執行前，需先執行第6行之prepare_train_data()函數，產生出train_pre_another_17_33.csv，這個檔案為所有的item_id(所有商品)*shop_id(所有商店)*[17,33](第17到第33個月)之資料，無其他特徵
  * 在資料結擁有train_pre_another_17_33.csv後，就可以直接執行another.py，他會讀取所有需要之原始資料檔案，以及train_pre_another_17_33.csv、test.csv，依序將特徵填入，最後將訓練資料儲存為train_pre_another.csv，測試資料儲存為test_pre_another.csv，讀檔位置在程式碼中第36與60行，而輸出檔案之檔名在程式碼中第352、353行
  * another.py這個檔案程式碼較為凌亂，是因為特徵都是想到一個就加一個，最後整理完就變很多行
