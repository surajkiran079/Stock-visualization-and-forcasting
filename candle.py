import streamlit as st
import feedback
import stocks
import virtual_trading

def main_page():
    st.title("Welcome ! our website")

    st.title("Read the Documentation mentioned below before using the Platform.")
    st.subheader("Stocks and their ER Indicator Values:")
    st.write("""We are not a SEBI registered platform. Please consult your financial adviser before investment or do your own research while investing and backtest the platform.""")

    st.write("""
        ### Follow the Values for Investment Purpose
        These values are backtested. However, always ensure to perform your own due diligence.
        """)

    st.write("""
        ### List of Stocks and Their Threshold Values
        - **hdfcbnk.ns** - 20
        - **sbin.ns** - 21
        - **kotakbnk.ns** - 20
        - **reliance.ns** - 22
        - **asianpaint.ns** - 20
        - **sail.ns** - 20
        - **coalindia.ns** - 20
        - **bpcl.ns** - 22
        - **tcs.ns** - 23
        - **upl.ns** - 23
        - **srf.ns** - 23
        """)

def stocks_page():
    stocks.main()

def virtual_tradings():
    virtual_trading.main()

def feedback_form():
    feedback.main()




# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio('go to',["Main Page", "Stocks Page","feedback us","virtual Trading"])


# Navigation logic
if page == "Main Page":
    main_page()
elif page == "Stocks Page":
    stocks_page()
elif page == "virtual Trading":
    virtual_trading.main()
elif page == "feedback us":
    feedback.main()



