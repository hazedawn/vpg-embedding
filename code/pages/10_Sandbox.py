import streamlit as st
import traceback
from utilities.helper import LLMHelper

def clear_summary():
    st.session_state['summary'] = ""

def get_custom_prompt():
    customtext = st.session_state['customtext']
    customprompt = "{}".format(customtext)
    return customprompt

def customcompletion():
    response = llm_helper.get_completion(get_custom_prompt(), max_tokens=500)
    st.session_state['result'] = response.encode().decode()

try:
    # Set page layout to wide screen and menu item
    menu_items = {
    'Get help': None,
    'Report a bug': None,
    'About': '''
     ## Embeddings App
     Embedding testing application.
    '''
    }
    st.set_page_config(layout="wide", menu_items=menu_items)

    st.markdown("## Bring your own prompt")

    llm_helper = LLMHelper()

    # displaying a box for a custom prompt
    st.session_state['customtext'] = st.text_area(label="Prompt",value='You are an assistant of Value Partners Group, which is an investment holding company that specializes in long-biased funds, long-short hedge funds, fixed income products, exchange-traded funds, as well as quantitative products. It was founded in 1993 and is located in Hong Kong. Value Partners is one of Asia’s largest independent asset management firms offering world-class investment services and products for institutional and individual clients globally. In addition to the Hong Kong headquarters, they operate in Shanghai, Shenzhen, Beijing, Kuala Lumpur, Singapore and London. Your job is to provide financial advice from the perspective of Value Partners Group. \n \n The following is a conversation with Value Partners Group assistant. \n \n Human: \n \n Value Partners Group Assistant: ', height=400)
    st.button(label="Test with your own prompt", on_click=customcompletion)
    # displaying the summary
    result = ""
    if 'result' in st.session_state:
        result = st.session_state['result']
    st.text_area(label="OpenAI result", value=result, height=200)

except Exception as e:
    st.error(traceback.format_exc())
