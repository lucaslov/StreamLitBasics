import streamlit as st

def main():
    st.title("Lista zakupowa")
    
    if 'shopping_list' not in st.session_state:
        st.session_state.shopping_list = []

    new_item = st.text_input("Dodaj element")

    if st.button("Dodaj"):
        if new_item.strip():
            st.session_state.shopping_list.append(new_item.strip())
        else:
            st.warning("Niepoprawna wartość")

    if st.button("Usuń wszystko"):
        st.session_state.shopping_list.clear()
    
    if st.session_state.shopping_list:
        col1, col2 = st.columns([1,1])
        for i, item in enumerate(st.session_state.shopping_list, start=1):
            with col1:
                st.write(f"{i}. {item}")
            with col2:
                if st.button("Usuń", key=i):
                    del st.session_state.shopping_list[i-1]
                    st.rerun()

if __name__ == "__main__":
    main()
