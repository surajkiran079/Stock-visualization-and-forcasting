import streamlit as st
import feedback
import stocks
import virtual_trading

def main_page():
    st.title("Welcome ! Investors")

    st.title("Read the Documentation mentioned below before using the Platform.")

    st.write("""We are not a SEBI registered platform. Please consult your financial adviser before investment or do your own research while investing.""")

    st.write("""
        ### Follow the Guidelines for Investment Purpose :
        ->These values are backtested. However, always ensure to perform your own due diligence.
        """)
    st.write("""
            ->Please Invest in stocks mentioned below and follow the ER Value.NOTE Invest your money after Crossing ER Values.
            """)
    st.write(""" 
            ->Kindly, Always follow 1:4 or 1:5 Risks Reward Ratio (eg: Target = 10% and Stoploss = 2.5%).
            """)
    st.write("""
            ->Please Stick to the Rules to make your Investment Jounery Profitable.
            """)

    st.write("""
        ### List of Stocks -- ER Indicator Buying Value
        - **hdfcbnk.ns** - 20 - 25
        - **sbin.ns** - 21 - 25
        - **kotakbnk.ns** - 20-25
        - **reliance.ns** - 22-25
        - **asianpaint.ns** - 20 - 25
        - **sail.ns** - 20 - 25
        - **coalindia.ns** - 20 - 25
        - **bpcl.ns** - 22 - 25
        - **tcs.ns** - 23 - 25
        - **upl.ns** - 23 - 25
        - **srf.ns** - 23 - 25
        - **TCS.ns** - 22 - 25
        """)

def stocks_page():
    stocks.main()

def virtual_tradings():
    virtual_trading.main()

def feedback_form():
    feedback.main()




# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio('go to',["Main Page", "Stocks Page","virtual Trading", "feedback us"])


# Navigation logic
if page == "Main Page":
    main_page()
elif page == "Stocks Page":
    stocks_page()
elif page == "virtual Trading":
    virtual_tradings()
elif page == "feedback us":
    feedback_form()



