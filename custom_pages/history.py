import streamlit as st
import pandas as pd


def show_history():

    st.subheader("📜 Prediction History")

    if len(st.session_state.history) == 0:

        st.info(
            "No prediction history available."
        )

    else:

        hist_df = pd.DataFrame(
            st.session_state.history
        )

        st.dataframe(
            hist_df,
            use_container_width=True,
            height=500
        )

        csv = hist_df.to_csv(index=False)

        st.download_button(
            "⬇ Download History",
            csv,
            "prediction_history.csv",
            "text/csv"
        )