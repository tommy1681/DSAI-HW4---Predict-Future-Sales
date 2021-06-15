# DSAI-HW4---Predict-Future-Sales

* 預處理過後之資料由於檔案過大，所以上傳至google雲端，連結附在最後，請助教直接下載train_pre_another.csv、test_pre_another.csv，就可以執行模型訓練與產生預測資料，請放在與lightgbm_train.py同階層資料夾
* 執行方法
  * python lightgbm_train.py --train train_pre_another.csv --test test_pre_another.csv --output output.csv
  * train_pre_another.csv為預處理過的訓練資料
  * test_pre_another.csv為預處理過的測試資料
  * output output.csv為預測資料之檔名
 
* 檔案說明
  * 本作業分成兩個檔案
  * 一個是模型訓練與預測的檔案  lightgbm_train.py
  * 一個是產生欲處理過後之資料的檔案  another.py
  * 說明
	  * lightgbm_train.py需讀取已處理過後之訓練檔案與測試檔案，會依照路徑訓練完成後，直接輸出預測檔案
	  
	  * another.py為前處理之檔案，在執行前，需先執行第6行之prepare_train_data()函數，產生出train_pre_another_17_33.csv，這個檔案為所有的item_id(所有商品)X shop_id(所有商店)X (17~33)(第17到第33個月)之資料，無其他特徵
	  * 在資料夾中擁有train_pre_another_17_33.csv後，就可以直接執行another.py，他會讀取所有需要之原始資料檔案，以及train_pre_another_17_33.csv、test.csv，依序將特徵填入，最後將訓練資料儲存為train_pre_another.csv，測試資料儲存為test_pre_another.csv，讀檔位置在程式碼中第36與60行，而輸出檔案之檔名在程式碼中第409、410行
	  * another.py這個檔案程式碼較為凌亂，是因為特徵都是想到一個就加一個，最後整理完就變很多行
	  * another.py 由於再添加特徵的時候，是使用train_pre_another_17_33.csv，此檔會有700多萬筆資料，所有特徵添加完成時間會花費2小時，請助教留意，git已附上預處理結束後之檔案train_pre_another.csv、test_pre_another.csv
* report link:
	* https://docs.google.com/presentation/d/1FvJoXt_a4zGjopO-QqKH4dQCxEPMh99vhgFjN1sMKsM/edit?usp=sharing
	
* 預處理資料下載連結:
	* train_pre_another.csv : https://drive.google.com/file/d/1RwwJ6UEmOgHvyW4YUPqUFeF4gBQ8hdCX/view?usp=sharing
	* test_pre_another.csv : https://drive.google.com/file/d/1tsmoJ9vc7hyfC3rLybqf_PYxF02sDPvx/view?usp=sharing
	* train_pre_another_17_33.csv : https://drive.google.com/file/d/1944zOduu1NOuBTP42R38rgNBM97fQzv0/view?usp=sharing