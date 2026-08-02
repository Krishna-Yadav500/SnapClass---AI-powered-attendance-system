import streamlit as st



def footer_home():
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center;">
            <p style="font-weight:600; font-size:16px;">
                <span style="color:#E2E8F0;">Created with </span>
                <span style="color:#FF4D6D;">❤️</span>
                <span style="color:#CBD5E1;"> by </span>
                <span style="color:#FACC15; font-weight:700;"> KRISHNA</span>
            </p>
        </div>
        """, unsafe_allow_html=True)

def footer_dashboard():
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center;">
           <p style="font-weight:600; font-size:16px;">
                <span style="color:#475569;">Created with </span>
                <span style="color:#FF4D6D;">❤️</span>
                <span style="color:#64748B;"> by </span>
                <span style="color:#2563EB; font-weight:700;"> KRISHNA</span>
           </p>
        </div>
        """, unsafe_allow_html=True)