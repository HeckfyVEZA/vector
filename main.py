import streamlit as st
from info_search_vector import info
from vector_selection import selection
from auto_valve_scheme import valve, scheme
from blank import blank_auto
from order_form import fulfil_temp


st.set_page_config(layout="wide")
st.session_state['developer'] = st.text_input('Введите имя разработчика')
main_tab = st.tabs(['Автоматический режим', 'Полуавтоматический режим', 'Ручной режим'])
i = 0
with main_tab[0]:
    f = st.file_uploader("Перетяните бланки сюда", accept_multiple_files=True)
    for file in f:
        # st.write(info(file).all_data)
        current_info = info(file).all_data
        for cinfo in current_info:
            cvector = selection(scheme(cinfo[0][1]), valve(cinfo[0][1], cinfo[2][1]), cinfo[2][1], cinfo[9][1])
            cblank = (blank_auto(selection(scheme(cinfo[0][1]), valve(cinfo[0][1], cinfo[2][1]), cinfo[2][1], cinfo[9][1]), cinfo, st.session_state['developer']))
            cvector = selection(scheme(cinfo[0][1], cblank["intermediate coolant"]), valve(cinfo[0][1], cinfo[2][1], cblank["intermediate coolant"]), cinfo[2][1], cinfo[9][1])
            cblank = (blank_auto(cvector, cinfo, st.session_state['developer']))
            st.write(cblank)
            st.button('Кнопка', on_click=fulfil_temp(cblank), key=f"{i}")
            i+=1
