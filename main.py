# import smtplib
# import os
# from email.mime.text import MIMEText
# from fastapi import FastAPI
# from pydantic import BaseModel
# from dotenv import load_dotenv
# import json

# from langchain_openai import ChatOpenAI
# from langchain.schema import SystemMessage, HumanMessage

# load_dotenv()
# app = FastAPI()

# # Config
# EMAIL_HOST = os.getenv("EMAIL_HOST")
# EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
# EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
# EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# # LangChain Chat Model
# chat = ChatOpenAI(temperature=0)

# # Request body model
# class EmailQuery(BaseModel):
#     query: str


# def extract_email_data(query: str):
#     messages = [
#         SystemMessage(content="""
# You are an AI assistant. Extract email information from the user's message.

# Return JSON in the format:
# {
#     "to": "email",
#     "subject": "subject text",
#     "message": "body text"
# }
# """),
#         HumanMessage(content=f"Extract info from: \"{query}\"")
#     ]

#     response = chat(messages)
#     content = response.content

#     try:
#         return json.loads(content)
#     except:
#         return eval(content)  # fallback only if JSON parsing fails


# def send_email(to_email, subject, body):
#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = EMAIL_ADDRESS
#     msg["To"] = to_email

#     with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
#         server.starttls()
#         server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         server.send_message(msg)


# @app.post("/send-mail/")
# def send_mail(email_query: EmailQuery):
#     try:
#         email_data = extract_email_data(email_query.query)
#         send_email(email_data["to"], email_data["subject"], email_data["message"])
#         return {"status": "Email sent", "data": email_data}
#     except Exception as e:
#         return {"status": "Failed", "error": str(e)}
