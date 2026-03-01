import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ตั้งค่าหน้าเพจ
st.set_page_config(page_title="My Simple Dashboard", layout="wide")
st.title("📊 Sales Dashboard อย่างง่าย")

# 2. สร้างข้อมูลจำลอง (ใช้ข้อมูลอะไรก็ได้)
data = {
    'Category': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Food', 'Food'],
    'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Sales': [1500, 2000, 800, 1200, 500, 900],
    'Profit': [300, 450, 150, 250, 100, 200]
}
df = pd.DataFrame(data)