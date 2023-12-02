from dotenv import load_dotenv
import os
from openai import OpenAI
import streamlit as st
import time

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

client = OpenAI(api_key=API_KEY)

# thread_id를 하나로 관리하기 위함
# if 'thread_id' not in st.session_state:
#   thread = client.beta.threads.create()
#   st.session_state.thread_id = thread.id

# thread_id = st.session_state.thread_id

# thread_id, assistant_id 설정
thread_id = "thread_cK5FMO5wkOq1GLpKwND7ovEZ"
assistant_id = "asst_B03hbC1Wuql9LQt4yAo8pd6x"

# thread_massages 불러오기
thread_messages = client.beta.threads.messages.list(thread_id, order="asc")

# Page Title
st.header('ai assistants 대화')

# thread massage를 가져와서 UI에 나타내게 구현
for msg in (thread_messages.data):
  with st.chat_message(msg.role):
    st.write(msg.content[0].text.value)

# 입력창에 프롬프트 입력을 받아서 메세지를 생성
prompt = st.chat_input("질문을 입력해주세요")
if prompt:
  message = client.beta.threads.messages.create(
    thread_id="thread_cK5FMO5wkOq1GLpKwND7ovEZ",
    role="user",
    content=prompt
  )

  # 입력한 메세지를 UI에 표시 
  with st.chat_message(message.role):
    st.write(message.content[0].text.value)

  # run 실행
  run = client.beta.threads.runs.create(
    thread_id="thread_cK5FMO5wkOq1GLpKwND7ovEZ",
    assistant_id=assistant_id
  )

  with st.spinner('Generting response'):
    #Run complete 여부 3초마다 체크
    while run.status != "completed":
      time.sleep(3)
      run = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run.id
      )

  #while문을 빠져나왔다는 것은 완료됐다는 것이니 메세지 불러오기
  messages = client.beta.threads.messages.list(
    thread_id=thread_id
  )

  #마지막 메세지 UI에 추가하기
  with st.chat_message(messages.data[0].role):
    st.write(messages.data[0].content[0].text.value)
