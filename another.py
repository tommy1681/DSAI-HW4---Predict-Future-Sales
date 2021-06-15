
import pandas as pd 
import time

#製造空白資料，將所有item_id*shop_id*[17,33]的月份
def prepare_train_data():
    train = pd.read_csv('sales_train.csv')
    print(train.shape)
    df = pd.DataFrame(columns = ['shop_id' , 'item_id','date_block_num','item_cnt_day'])
    print(df)
    train_dic = train.groupby(['shop_id', 'item_id'])['item_cnt_day'].sum()
    train_month_item_cnt_day = train.groupby(['shop_id', 'item_id','date_block_num'])['item_cnt_day'].sum()
    for j in range(17,34):
        a=1
        for i in train_dic.keys():
            if (i[0],i[1], j) in train_month_item_cnt_day.index:
                z = train_month_item_cnt_day[i[0]][i[1]][j]
            else:
                z=0
            df.loc[a]=[i[0],i[1],j,z]
            a+=1
    
        path = "train_pre_another"+str(j)+".csv"
        df.to_csv(path,index=False)
    df = df.reset_index()
    df.to_csv("train_pre_another_17_33.csv",index=False)
    df['item_cnt_day'] = df['item_cnt_day'].map(lambda x: max(0, min(20, x)))


    print(train.shape)

    return train
#==============================================================================================================================
start = time.time()
print("開始",start)
sales_train = pd.read_csv('sales_train.csv')
train = pd.read_csv('train_pre_another_17_33.csv')
train['item_cnt_day'] = 0


sales_train = sales_train.groupby(['shop_id', 'item_id','date_block_num'])['item_cnt_day'].sum()
sales_train = sales_train.reset_index()
sales_train['item_cnt_day'] = sales_train['item_cnt_day'].map(lambda x: max(0, min(20, x)))
train_month_item_cnt_day = sales_train.groupby(['shop_id', 'item_id','date_block_num'])['item_cnt_day'].sum()

def make_item_cnt_day(x):
    
    if (x['shop_id'], x['item_id'], x['date_block_num']) in train_month_item_cnt_day.index:
        
        return train_month_item_cnt_day[x['shop_id'], x['item_id'], x['date_block_num']]
    else:
        return 0

train['item_cnt_day'] = train.apply(make_item_cnt_day, axis='columns')
print("將每月銷售填入")



#讀取測試資料
def prepare_test_data():
    test = pd.read_csv('test.csv')

    test['date_block_num'] = 34 
    
    return test

test = prepare_test_data()


def make_prev_month_sales(x):
    
    if (x['shop_id'], x['item_id'], x['date_block_num'] - last_month_num) in train_month_item_cnt_day .index:
        ans = int(train_month_item_cnt_day [(x['shop_id'], x['item_id'], x['date_block_num'] - last_month_num)])
        return ans
    else:
        return 0

def make_prev0_3_avg_month_sales(x):
    totalc =0
    sum = 0
    p3 = 0
    p2 = 0
    p1 = 0
    if  (x['shop_id'], x['item_id'], x['date_block_num'] - last_month_num ) in train_month_item_cnt_day.index:
        totalc+=3
        sum+=int(train_month_item_cnt_day[(x['shop_id'], x['item_id'], x['date_block_num'] - last_month_num )])
        p3 = 1
    if  (x['shop_id'], x['item_id'], x['date_block_num'] - last_month_num-1 ) in train_month_item_cnt_day.index:
        if p3 != 1:
            totalc+=2
        sum+=int(train_month_item_cnt_day[(x['shop_id'], x['item_id'], x['date_block_num'] - last_month_num -1)])
        p2 = 1
    if (x['shop_id'], x['item_id'], x['date_block_num'] - last_month_num-2 ) in train_month_item_cnt_day.index:
        if p3 ==0 and p2 ==0:
            totalc+=1
        sum+=int(train_month_item_cnt_day[(x['shop_id'], x['item_id'], x['date_block_num'] - last_month_num -2)])

    if totalc==0:
        return 0
    else:
        a = sum/totalc
        return a


def make_prev1_2_avg_month_sales(x):
    totalc =0
    sum = 0
    p2 = 0
    p1 = 0
    
    if  (x['shop_id'], x['item_id'], x['date_block_num'] - last_month_num) in train_month_item_cnt_day.index:
        
        totalc+=2
        sum+=int(train_month_item_cnt_day[(x['shop_id'], x['item_id'], x['date_block_num'] - last_month_num)])
        p2 = 1
    if (x['shop_id'], x['item_id'], x['date_block_num'] - last_month_num-1) in train_month_item_cnt_day.index:
        if  p2 ==0:
            totalc+=1
        sum+=int(train_month_item_cnt_day[(x['shop_id'], x['item_id'], x['date_block_num'] - last_month_num-1)])

    if totalc==0:
        return 0
    else:
        a = sum/totalc
        return a





last_month_num = 1
train['prev_1_month_sales'] = train.apply(make_prev_month_sales, axis='columns')
test['prev_1_month_sales'] = test.apply(make_prev_month_sales, axis='columns')
print(train.shape)
print("新增前1個月")

last_month_num = 2
train['prev_2_month_sales'] = train.apply(make_prev_month_sales, axis='columns')
test['prev_2_month_sales'] = test.apply(make_prev_month_sales, axis='columns')
print(train.shape)
print("新增前2個月")


last_month_num = 3
train['prev_3_month_sales'] = train.apply(make_prev_month_sales, axis='columns')
test['prev_3_month_sales'] = test.apply(make_prev_month_sales, axis='columns')
print(train.shape)
print("新增前3個月")


last_month_num = 4
train['prev_4_month_sales'] = train.apply(make_prev_month_sales, axis='columns')
test['prev_4_month_sales'] = test.apply(make_prev_month_sales, axis='columns')
print(train.shape)
print("新增前4個月")


last_month_num = 5
train['prev_5_month_sales'] = train.apply(make_prev_month_sales, axis='columns')
test['prev_5_month_sales'] = test.apply(make_prev_month_sales, axis='columns')
print(train.shape)
print("新增前5個月")


last_month_num = 6
train['prev_6_month_sales'] = train.apply(make_prev_month_sales, axis='columns')
test['prev_6_month_sales'] = test.apply(make_prev_month_sales, axis='columns')
print(train.shape)
print("新增前6個月")


last_month_num = 7
train['prev_7_month_sales'] = train.apply(make_prev_month_sales, axis='columns')
test['prev_7_month_sales'] = test.apply(make_prev_month_sales, axis='columns')
print(train.shape)
print("新增前7個月")


last_month_num = 8
train['prev_8_month_sales'] = train.apply(make_prev_month_sales, axis='columns')
test['prev_8_month_sales'] = test.apply(make_prev_month_sales, axis='columns')
print(train.shape)
print("新增前8個月")

last_month_num = 9
train['prev_9_month_sales'] = train.apply(make_prev_month_sales, axis='columns')
test['prev_9_month_sales'] = test.apply(make_prev_month_sales, axis='columns')
print(train.shape)
print("新增前9個月")




    
last_month_num = 3
train['prev0_3_avg_month_sales'] = train.apply(make_prev0_3_avg_month_sales, axis='columns')
test['prev0_3_avg_month_sales'] = test.apply(make_prev0_3_avg_month_sales, axis='columns')
print(train.shape)
print("新增前0~3個月平均")



    
last_month_num = 4
train['prev1_4_avg_month_sales'] = train.apply(make_prev0_3_avg_month_sales, axis='columns')
test['prev1_4_avg_month_sales'] = test.apply(make_prev0_3_avg_month_sales, axis='columns')
print(train.shape)
print("新增前1~4個月平均")

last_month_num = 5
train['prev2_5_avg_month_sales'] = train.apply(make_prev0_3_avg_month_sales, axis='columns')
test['prev2_5_avg_month_sales'] = test.apply(make_prev0_3_avg_month_sales, axis='columns')
print(train.shape)
print("新增前2~5個月平均")


last_month_num = 6
train['prev3_6_avg_month_sales'] = train.apply(make_prev0_3_avg_month_sales, axis='columns')
test['prev3_6_avg_month_sales'] = test.apply(make_prev0_3_avg_month_sales, axis='columns')
print(train.shape)
print("新增前3~6個月平均")



    
last_month_num = 2
train['prev1_2_avg_month_sales'] = train.apply(make_prev1_2_avg_month_sales, axis='columns')
test['prev1_2_avg_month_sales'] = test.apply(make_prev1_2_avg_month_sales, axis='columns')
print(train.shape)
print("新增前1~2個月平均")


last_month_num = 3
train['prev2_3_avg_month_sales'] = train.apply(make_prev1_2_avg_month_sales, axis='columns')
test['prev2_3_avg_month_sales'] = test.apply(make_prev1_2_avg_month_sales, axis='columns')
print(train.shape)
print("新增前2~3個月平均")


train_month_item_total_cnt_day = sales_train.groupby(['item_id','date_block_num'])['item_cnt_day'].sum()

def make_prev_1_month_item_total_sales(x):
    if ( x['item_id'], x['date_block_num'] - last_month_num) in train_month_item_total_cnt_day .index:
        ans = int(train_month_item_total_cnt_day [( x['item_id'], x['date_block_num'] - last_month_num)])
        return ans
    else:
        return 0

last_month_num = 1
train['prev_1_month_item_total_sales'] = train.apply(make_prev_1_month_item_total_sales, axis='columns')
test['prev_1_month_item_total_sales'] = test.apply(make_prev_1_month_item_total_sales, axis='columns')
print(train.shape)
print("新增前1個月商品總銷售")


last_month_num = 2
train['prev_2_month_item_total_sales'] = train.apply(make_prev_1_month_item_total_sales, axis='columns')
test['prev_2_month_item_total_sales'] = test.apply(make_prev_1_month_item_total_sales, axis='columns')
print(train.shape)
print("新增前2個月商品總銷售")

last_month_num = 3
train['prev_3_month_item_total_sales'] = train.apply(make_prev_1_month_item_total_sales, axis='columns')
test['prev_3_month_item_total_sales'] = test.apply(make_prev_1_month_item_total_sales, axis='columns')
print(train.shape)
print("新增前3個月商品總銷售")


items = pd.read_csv('items.csv')
train['cat_id'] = train['item_id'].map(lambda x: items.loc[x, 'item_category_id'])
test['cat_id'] = test['item_id'].map(lambda x: items.loc[x, 'item_category_id'])
print(train.shape)
print("新增商品類別")


shop_cat_db = train.groupby(['shop_id', 'cat_id', 'date_block_num'])['item_cnt_day'].sum()

def make_prev_month_cat_sales(x):
    if (x['shop_id'], x['cat_id'], x['date_block_num'] - last_month_num) in shop_cat_db.index:
        ans = int(shop_cat_db[(x['shop_id'], x['cat_id'], x['date_block_num'] - last_month_num)])
        return ans
    else:
        return 0
last_month_num = 1
train['prev_month_cat_sales'] = train.apply(make_prev_month_cat_sales, axis='columns')
test['prev_month_cat_sales'] = test.apply(make_prev_month_cat_sales, axis='columns')
print(train.shape)
print("新增前一個月商品類別總銷售")


last_month_num = 2
train['prev_month_2_cat_sales'] = train.apply(make_prev_month_cat_sales, axis='columns')
test['prev_month_2_cat_sales'] = test.apply(make_prev_month_cat_sales, axis='columns')
print("新增前2個月商品類別總銷售")


last_month_num = 3
train['prev_month_3_cat_sales'] = train.apply(make_prev_month_cat_sales, axis='columns')
test['prev_month_3_cat_sales'] = test.apply(make_prev_month_cat_sales, axis='columns')
print("新增前3個月商品類別總銷售")



shop_cat_total_db = train.groupby([ 'cat_id', 'date_block_num'])['item_cnt_day'].sum()

def make_prev_month_cat_total_sales(x):
    if ( x['cat_id'], x['date_block_num'] - last_month_num) in shop_cat_total_db.index:
        ans = int(shop_cat_total_db[( x['cat_id'], x['date_block_num'] - last_month_num)])
        return ans
    else:
        return 0

last_month_num = 1
train['prev_month_cat_total_sales'] = train.apply(make_prev_month_cat_total_sales, axis='columns')
test['prev_month_cat_total_sales'] = test.apply(make_prev_month_cat_total_sales, axis='columns')
print(train.shape)
print("新增前一個月商品類別總銷售")

last_month_num = 2
train['prev_month_2_cat_total_sales'] = train.apply(make_prev_month_cat_total_sales, axis='columns')
test['prev_month_2_cat_total_sales'] = test.apply(make_prev_month_cat_total_sales, axis='columns')
print(train.shape)
print("新增前地2個月商品類別總銷售")


last_month_num = 3
train['prev_month_3_cat_total_sales'] = train.apply(make_prev_month_cat_total_sales, axis='columns')
test['prev_month_3_cat_total_sales'] = test.apply(make_prev_month_cat_total_sales, axis='columns')
print(train.shape)
print("新增前地3個月商品類別總銷售")



sales_train = pd.read_csv('sales_train.csv')
train_month_item_price = sales_train.groupby(['item_id','date_block_num'])['item_price'].mean()

def make_prev_1_month_item_price(x):
    if ( x['item_id'], x['date_block_num'] - 1) in train_month_item_price .index:
        ans = int(train_month_item_price [( x['item_id'], x['date_block_num'] - 1)])
        return ans
    else:
        return 0

train['prev_1_month_item_price'] = train.apply(make_prev_1_month_item_price, axis='columns')
test['prev_1_month_item_price'] = test.apply(make_prev_1_month_item_price, axis='columns')
print(train.shape)
print("新增前1個月商品總銷售")



sales_train = pd.read_csv('sales_train.csv')
last_month = sales_train.groupby(['shop_id', 'item_id','date_block_num'])['item_cnt_day'].sum()
last_month = last_month.reset_index()

def make_last_month(x):

    if (x['shop_id'], x['item_id']) in temp.index:
        ans = int(temp[(x['shop_id'], x['item_id'])])
        
        return ans
    else:
        return 0


for i in range(17,33):
    temp_t = train.drop(train[train['date_block_num']!=i].index)
    m_temp = i
    temp = last_month.drop(last_month[last_month['date_block_num']>=m_temp].index)
    temp = temp.groupby(['shop_id', 'item_id'])['date_block_num'].max()
    temp_t['last_month'] = temp_t.apply(make_last_month, axis='columns')
    if i ==17:
        final_df = temp_t
    else:
        final_df = pd.concat([final_df, temp_t]) 
    print(i)


train = final_df


temp = last_month.drop(last_month[last_month['date_block_num']>=34].index)
temp = temp.groupby(['shop_id', 'item_id'])['date_block_num'].max()
test['last_month'] = test.apply(make_last_month, axis='columns')

print(train.shape)
print("新增最後賣出該物品的時間")



data = sales_train.groupby(['shop_id', 'item_id','date_block_num'])['item_cnt_day'].sum()
data = data.reset_index()
first_month = data.groupby(['shop_id', 'item_id'])['date_block_num'].min()


def make_first_month(x):
   
    if (x['shop_id'], x['item_id']) in first_month.index:
        ans = int(first_month[(x['shop_id'], x['item_id'])])
        #print(ans,x['date_block_num'])
        return ans
    else:
        return 0

train['first_month'] = train.apply(make_first_month, axis='columns')
test['first_month'] = test.apply(make_first_month, axis='columns')
print(train.shape)
print("新增最早賣出該物品的時間")


train.to_csv("train_pre_another.csv",index=False)
test.to_csv("test_pre_another.csv",index=False)



# 結束測量
end = time.time()

# 輸出結果
print("執行時間：%f 秒" % (end - start))