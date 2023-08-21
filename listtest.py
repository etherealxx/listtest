import streamlit as st
import os

def list_files_recursive(directory):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        st.write(f"{indent}[{os.path.basename(root)}/]")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            st.write(f"{sub_indent}{file}")

st.title('test')
list_files_recursive('/mount/src/listtest')