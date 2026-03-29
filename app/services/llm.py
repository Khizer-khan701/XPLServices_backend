import asyncio
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.core.config import settings


# ---- Models Setup ----
openai_llm = ChatOpenAI(
    model="gpt-5-turbo",
    api_key=settings.OPENAI_API_KEY,
)

kimi_llm = ChatOpenAI(
    model="moonshotai/kimi-k2.5",
    api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    max_tokens=500,
)

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.GEMINI_API_KEY,
    convert_system_message_to_human=True
)

# ---- Prompt Template ----
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""You are a helpful assistant for Sunmarke School.
Answer the question based ONLY on the provided context.
If the answer is not in the context, say: "I don't have information about that in my knowledge base."

Context:
{context}

Question: {question}

Answer:"""
)

# ---- Chains ----
parser = StrOutputParser()

openai_chain = prompt_template | openai_llm | parser
kimi_chain = prompt_template | kimi_llm | parser
gemini_chain = prompt_template | gemini_llm | parser


# ---- Individual Functions ----
async def ask_openai(context: str, question: str) -> str:
    try:
        response = await openai_chain.ainvoke({
            "context": context,
            "question": question
        })
        return response
    except Exception as e:
        return f"OpenAI Error: {str(e)}"


async def ask_kimi(context: str, question: str) -> str:
    try:
        response = await kimi_chain.ainvoke({
            "context": context,
            "question": question
        })
        return response
    except Exception as e:
        return f"Kimi Error: {str(e)}"


async def ask_gemini(context: str, question: str) -> str:
    try:
        response = await gemini_chain.ainvoke({
            "context": context,
            "question": question
        })
        return response
    except Exception as e:
        return f"Gemini Error: {str(e)}"


# ---- Teeno Simultaneously ----
async def ask_all_llms(context: str, question: str) -> dict:
    openai_res, kimi_res, gemini_res = await asyncio.gather(
        ask_openai(context, question),
        ask_kimi(context, question),
        ask_gemini(context, question)
    )

    return {
        "gpt4o": openai_res,
        "kimi": kimi_res,
        "gemini": gemini_res
    }