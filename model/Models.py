# 필요모듈 불러오기
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MinMaxScaler
from scipy.sparse import csr_matrix
import pandas as pd
import numpy as np
import implicit
import pickle
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning or RuntimeWarning)

# Class Models
class Models():
    
    def __init__(self):
        pass
    
    # fit 메소드로 결과 출력에 필요한 데이터를을 생성하고 저장합니다.
    def fit(self, DATA_PATH):
        Read_csv(DATA_PATH)
    
    # user_id를 받으면 아직 보지않은 product_id 10개를 list로 반환합니다.
    def recommend(self, user_id):

        # 해당 유저가 로그데이터 안에 있다면
        if user_id in test_pkl("users"):
            print(f"user_id = {user_id} 는 기존고객 입니다.")

            # 해당 유저가 구매 이력이 있을 경우
            if :
                
                return 
            
            # 해당 유저가 조회한 상품이 20개 이상이지만, 구매 이력이 없을 경우
            elif :
            
            # 해당 유저가 조회한 상품의 수가 20개 미만이면
            else :
                # 데이터와 해당 품목에 대한 전처리를 시작합니다.
                def CB_Making(df, division1_value, division2_value):
                b = df
                b = df[df['division1']== division1_value]
                b_model = b[b['division2'] == division2_value]
                b_model['price'] = b_model['price'].apply(lambda x : round(x, 1))
                b_model = b_model.astype({'product_id':'str', 'price':'str'})
                b_model = b_model.drop_duplicates(['product_id'])
                b_model = b_model.reset_index(drop=True)
                b_model['content'] = b_model['event_type'] + '.' + b_model['brand'] + '.' + b_model['price']
                CB2_df = b_model[['event_type','product_id','brand','price','content']]
                CB2_df = CB2_df.reset_index(drop=True)
                return CB2_df

# CB 추출
def CB_Show(CB2_df, product_number):
        count_vect = CountVectorizer(min_df=0, ngram_range=(1,2))
        genre_mat = count_vect.fit_transform(CB2_df['content'])
        genre_sim = cosine_similarity(genre_mat, genre_mat)
        genre_sim_sorted_ind = genre_sim.argsort()[:, ::-1]
        similar_products = find_sim_product(CB2_df, genre_sim_sorted_ind, product_number, 10)
        similar_products = similar_products.reset_index(drop=True)
        return similar_products[['product_id', 'brand']]
                
                
                
        
        #  신규유저일 경우
        else:
            # 대분류별 상위 10개의 product_id

            category = ['electronics', 'unknown', 'appliances', 'computers', 'apparel', 'furniture']
    
            for k in category:
                df_item1 = df_price.loc[df_price['division1']== k ]
                df_item1 = df_item1.groupby('product_id')['event_type'].count()
                df_item1 = df_item1.sort_values(ascending=False)
                df_item1 = df_item1.iloc[:10]
                print(k, ':', list(df_item1.keys()))       