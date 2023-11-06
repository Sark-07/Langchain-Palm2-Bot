from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.llms import GooglePalm
from dotenv import load_dotenv
import os
load_dotenv()

def myGpt(query):

    # Prompt template
    template = """Assistant is a large language model.
    Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.
    Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.
    Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.

    {history}
    Human: {human_input}
    Assistant:"""

    prompt = PromptTemplate(input_variables=["history", "human_input"], template=template)


    # creating llm chain

    llm = GooglePalm(google_api_key=os.getenv('GOOGLE_PALM_SECRET_KEY'))

    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=False,
        memory=ConversationBufferWindowMemory(k=2),
        # llm_kwargs={"max_length": 4096}
    )

    # predict
    output = chain.predict(
    human_input=query
    )
    return output

if __name__ == "__main__":
    print(myGpt('Hello Bard.'))