import streamlit as st
from scraper import scrape_website,split_dom_content,clean_body_content,extract_body_content
from parse import parse_with_ollama 

st.title("AI WebScraper") # title of Website
url = st.text_input("Enter the URL here::") # Normal textBox
if st.button("Scrape Site"):  # button using streamlit which will perform some task if button is clicked 
    st.write("Working in Progress...") 
    result = scrape_website(url)
    
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content
    
    with st.expander("View DOM Content"):  # an area by streamlit which can be scaled dynamically
        st.text_area("DOM Content",cleaned_content,height=300) #  actual scrolldown box
        
        
if "dom_content" in st.session_state: # if dom content is successfully fetched
    parse_description = st.text_area("Describe the Information you want to parse") #User text Area
    
    if st.button("Parsed Content"): #button for ai parsing
        if parse_description:
            st.write("Parsing the Content")
            
            dom_chunks = split_dom_content(st.session_state.dom_content) # splitting the dom contents into chunks
            result = parse_with_ollama(dom_chunks,parse_description) # getting all the responses from the llm 
            st.write(result) # writing all the resposes to the page