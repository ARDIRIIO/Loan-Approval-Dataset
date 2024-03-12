import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

# Load dump files
with open('dt_gridcv_best.pkl', 'rb') as file_6:
    dt_gridcv_best = pickle.load(file_6)

    
def run():
    # Membuat form
    with st.form(key='form parameters'):
        loan_id = st.text_input('Loan ID', value='')
        no_of_dependents = st.selectbox('Number of Dependents', (1, 2, 3, 4, 5, 6, 7, 8, 9))
        education = st.selectbox('Education', ('Graduate', 'Not Graduate'))
        self_employed = st.selectbox('Employment Status', ('Yes', 'No'))
        
        st.markdown('---')
        
        income_annum = st.text_input('Pendapatan Tahunan', value='')
        loan_amount = st.text_input('Jumlah Pinjaman', value='')
        loan_term = st.slider('Jumlah pinjaman Tahunan', 0, 50, 0)
        cibil_score = st.slider('Credit Score', 300, 900, 600)
        residential_assets_value = st.text_input('Residential Assets Value', value='')
        commercial_assets_value = st.text_input('Commercial Assets Value', value='')
        luxury_assets_value = st.text_input('Luxury Assets Value', value='')
        bank_asset_value = st.text_input('Bank Asset Value', value='')
        total_assets_value = st.text_input('Total Assets Value', value='')
        condition = st.selectbox('Apakah nilai total aset Anda lebih tinggi dari jumlah pinjaman?', ('Syarat Tidak Terpenuhi', 'Syarat Terpenuhi'))

        st.markdown('---')
        
        submitted = st.form_submit_button('Predict')
        
    data_inf = {
    'loan_id':loan_id, 
    'no_of_dependents':no_of_dependents, 
    'education':education, 
    'self_employed':self_employed,
    'income_annum':income_annum, 
    'loan_amount':loan_amount, 
    'loan_term':loan_term, 
    'cibil_score':cibil_score,
    'residential_assets_value':residential_assets_value, 
    'commercial_assets_value':commercial_assets_value,
    'luxury_assets_value':luxury_assets_value, 
    'bank_asset_value':bank_asset_value, 
    'total_assets_value':total_assets_value, 
    'condition':condition}
    
    data_inf = pd.DataFrame(data_inf)
    st.dataframe(data_inf)
    
    if submitted:
        # Predict using Linear Regression
        y_pred_inf = dt_gridcv_best.predict(data_inf)
        
        # Print result of the prediction
        if int(y_pred_inf) == 0:
            st.write('The prediction for `loan_status` is: 0 (Rejected)')
        elif int(y_pred_inf) == 1:
            st.write('The prediction for `loan_status` is: 1 (Approved)')
        
if __name__== '__main__':
    run()