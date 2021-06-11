from lightgbm import LGBMRegressor,plot_importance
import pandas as pd
from matplotlib import pyplot

class train_modle:
        def loadData(self,train_path='train_pre_another.csv',test_path ='test_pre_another.csv' ):
                self.train = pd.read_csv(train_path)
                self.test = pd.read_csv(test_path)
                
                print(self.train.shape)

                self.features = ['shop_id',
                        'item_id',
                        'date_block_num',
                        'cat_id',
                        'prev_1_month_sales',
                        'prev_2_month_sales',
                        'prev_3_month_sales',
                        'prev_4_month_sales',
                        'prev_5_month_sales',
                        'prev_6_month_sales',
                        'prev_7_month_sales',
                        'prev_8_month_sales',
                        'prev_9_month_sales',
                        'prev1_2_avg_month_sales',
                        'prev2_3_avg_month_sales',
                        'prev0_3_avg_month_sales',
                        'prev1_4_avg_month_sales',
                        'prev2_5_avg_month_sales',
                        'prev3_6_avg_month_sales',
                        'prev_1_month_item_total_sales',
                        'prev_2_month_item_total_sales',
                        'prev_3_month_item_total_sales',
                        'prev_month_cat_sales',
                        'prev_month_2_cat_sales',
                        'prev_month_3_cat_sales',
                        'prev_month_cat_total_sales',
                        'prev_month_2_cat_total_sales',
                        'prev_month_3_cat_total_sales',
                        'prev_1_month_item_price',
                        ]

        def train_test(self,path = 'output.csv'):
                t = self.test[self.features]

                X = self.train[self.features]
                S = X.shape[0]
                final_df = pd.concat([X, t]) 
                X_1 = pd.get_dummies(final_df)
                X = X_1[0:S]
                y = self.train['item_cnt_day']


                print(X.shape)
                model=LGBMRegressor(
                        n_estimators=800,
                        learning_rate=0.06,
                        
                        colsample_bytree=0.8,
                        max_depth=6,
                        reg_alpha=0.04,
                        reg_lambda=0.07,
                        min_child_weight=5)
                print("開始訓練")
                model.fit(X, y,
                        verbose=10
                        )

                
                predictions = model.predict(X_1[S:])
                predictions = pd.Series(predictions)
                predictions = predictions.map(lambda x: max(0, min(20, x)))

                        
                self.test['pred'] = predictions
                output = self.test[['ID', 'pred']]
                output.columns = ['ID', 'item_cnt_month']
                output = output.set_index('ID')
                
                output.to_csv(path)

                output.head()

                print(model.feature_importances_)
                
                
                plot_importance(model)
                pyplot.show()
def config():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--train", default="train_pre_another.csv", help="input the train data path")
    parser.add_argument("--test", default="test_pre_another.csv", help="input the test data path")
    parser.add_argument("--output", default="output.csv", help="output the bids path")

    return parser.parse_args()


if __name__ == "__main__":
        args = config()
        print(args.train,args.test,args.output)
        tr = train_modle()
        tr.loadData(args.train,args.test)
        tr.train_test(args.output)