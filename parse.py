from langchain_ollama import OllamaLLM #ollama AI
from langchain_core.prompts import ChatPromptTemplate # structure the prompts of AI


#This are the default prompts which are feed togther wuth the user prompt to get the desirable output
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model = "llama3.1") # type of the ollama mdel 

def parse_with_ollama(dom_chunk,parse_description): # feeding the chunks of html to the llm 
    prompt = ChatPromptTemplate.from_template(template)  #feeding the prompt to the llm
    chain = prompt | model # calling the prompt and then the model
    
    parsed_result = [] # variable to store result
    
    for i,chunk in enumerate(dom_chunk,start=1): # this will take all the response from llm and return the end result to display
        response = chain.invoke(
            {"dom_content":chunk,"parse_description": parse_description}
        )
        print(f"Parsed batch {i} of {len(dom_chunk)}")
        parsed_result.append(response)
        
        return "\n".join(parsed_result) # all the resopnses returned after seperating them from eachother