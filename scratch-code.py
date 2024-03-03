# from dotenv import load_dotenv
# import openai
# import time
# from math import floor
# import os, csv
# from rich import print as rprint
# from rich.panel import Panel
# import logging

# load_dotenv()

# # Set up logging
# logging.basicConfig(
#     filename="test-models-debug.log",
#     level=logging.DEBUG,
#     format="%(asctime)s:%(levelname)s:%(message)s",
# )


# # system_content = "You are a master riddle solver.I will give you a riddle. Take a deep breath! Now, think through it step by step. Then, briefly share your logic steps and your final answer."
# # user_content = "Three killers are in a room. Another person enters the room and kills one of the killers. Now, how many killers are in the room?"

# # system_content = "You are a poet who is known for mixing dark gallows humor with a deep understanding of human nature. You use ordinary language to create a slight feeling of magical realism. Your readers often go from tears to laughter to contemplation sin a single poem."
# # user_content = "In only five to ten lines write a poem. The poem should be about a person who is trying to find a way to escape from a room."


# models = [
#     "google/gemma-7b-it",
#     x"NousResearch/Nous-Capybara-7B-V1p9",
#     xxx"NousResearch/Nous-Hermes-2-Mistral-7B-DPO",
#     x"NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
#     xx"NousResearch/Nous-Hermes-2-Yi-34B",
#     xx"NousResearch/Nous-Hermes-llama-2-7b",
#     x"mistralai/Mistral-7B-Instruct-v0.2",
#     xx"mistralai/Mixtral-8x7B-Instruct-v0.1",
#     x"Qwen/Qwen1.5-14B-Chat",
#     "Qwen/Qwen1.5-72B-Chat",
#     "Qwen/Qwen1.5-7B-Chat",
#     quen 14 said no
#     quen 72 said no
#     x"snorkelai/Snorkel-Mistral-PairRM-DPO",
#     x"zero-one-ai/Yi-34B-Chat",
#     xx"openchat/openchat-3.5-1210",
#     x"teknium/OpenHermes-2-Mistral-7B",
#     xxx"teknium/OpenHermes-2p5-Mistral-7B",
#     xxx"upstage/SOLAR-10.7B-Instruct-v1.0",
#     x"Open-Orca/Mistral-7B-OpenOrca",
#     nooooo"WizardLM/WizardLM-13B-V1.2",
#     xxvicuna 1.5
#     xx"Austism/chronos-hermes-13b",
#     xxx"garage-bAInd/Platypus2-70B-instruct",
#     x"Gryphe/MythoMax-L2-13b",
# ]

# together_api_key = os.getenv("TOGETHER_API_KEY")
# # loop through the models list

# base_url = "https://api.together.xyz/v1"

# client = openai.OpenAI(
#     api_key=together_api_key,
#     base_url=base_url,
# )


# # Class for testing models
# class TestModels:
#     def __init__(self, model, system_content, user_content):
#         self.model = model
#         self.system_content = system_content
#         self.user_content = user_content

#     def run(self):
#         start_time = time.time()
#         chat_completion = client.chat.completions.create(
#             model=self.model,
#             messages=[
#                 {"role": "system", "content": self.system_content},
#                 {"role": "user", "content": self.user_content},
#             ],
#             temperature=0.8,
#             max_tokens=200,
#             stop="\n \n",
#         )

#         # for chunk in stream:
#         #     stream_response = chunk.choices[0].delta.content
#         #     rprint(stream_response or "", end="", flush=True)

#         response = chat_completion.choices[0].message.content
#         stop_time = time.time()
#         elapsed_time = round(stop_time - start_time, 2)
#         # Assuming response.content captures the response text
#         return self.model, elapsed_time, response


# # Main loop to run tests and write to CSV
# with open("results-poem.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Model", "Time Taken", "Response", "Rating"])

#     for model in models:
#         tester = TestModels(model, system_content, user_content)
#         # add a time delay to avoid rate limiting
#         time.sleep(10)
#         rating = 0
#         model_name, elapsed_time, response = tester.run()
#         writer.writerow([model_name, elapsed_time, response, rating])
#         rprint(
#             Panel(
#                 f"Model Name: {model_name}\nTime taken: {elapsed_time} seconds\nResponse: {response}",
#                 expand=True,
#                 title="Test Results",
#                 style="bold green",
#             )
#         )
