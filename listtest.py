import streamlit as st
import os
import wget

def list_files_recursive(directory):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        st.write(f"{indent}[{os.path.basename(root)}/]")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            st.write(f"{sub_indent}{file}")

st.title('test')
os.makedirs('/mount/src/listtest', exist_ok=True)
chromedriver_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chromedriver-linux64.zip"
zip_path = "/mount/src/listtest/chromedriver.zip"  # Set the desired path on the server
wget.download(chromedriver_url, zip_path)
os.system(f"unzip {zip_path} -d {os.path.dirname('/mount/src/listtest')}")
list_files_recursive('/mount/src/listtest')