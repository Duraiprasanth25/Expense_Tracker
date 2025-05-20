import streamlit as st
from datetime import datetime
from add_update_ui import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_months import analytics_month_tab
import requests

API_URL = "http://localhost:8000"

st.title("Expense Management System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics by Category", "Analytics by Months"])

with tab1:
    add_update_tab()
with tab2:
    analytics_category_tab()
with tab3:
    analytics_month_tab()