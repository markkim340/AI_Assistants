from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']


client = OpenAI(api_key=API_KEY)

# asst_rtNPXXQNcXMHRplljb3galYp
# assistant = client.beta.assistants.create(
#     name="Math Tutor",
#     instructions="You are a personal math tutor. Write and run code to answer math questions.",
#     tools=[{"type": "code_interpreter"}],
#     model="gpt-4-1106-preview"
# )

# print(assistant)

# thread_ymvVQI57ERfNLCRiAwZPLENf
# thread = client.beta.threads.create()
# print(thread)

# msg_j3tpZIZgYOqDLj0NuBNn2aBm
# message = client.beta.threads.messages.create(
#     thread_id="thread_ymvVQI57ERfNLCRiAwZPLENf",
#     role="user",
#     content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
# )

# print(message)

# run_uRNtM8u4UWPU5ipoI4q1vln9
# run = client.beta.threads.runs.create(
#   thread_id="thread_ymvVQI57ERfNLCRiAwZPLENf",
#   assistant_id="asst_rtNPXXQNcXMHRplljb3galYp",
#   instructions="Please address the user as Jane Doe. The user has a premium account."
# )

# print(run)


# run = client.beta.threads.runs.retrieve(
#   thread_id="thread_ymvVQI57ERfNLCRiAwZPLENf",
#   run_id="run_uRNtM8u4UWPU5ipoI4q1vln9"
# )

# print(run)


messages = client.beta.threads.messages.list(
  thread_id="thread_ymvVQI57ERfNLCRiAwZPLENf"
)

print(messages.data[0].content[0].text.value)