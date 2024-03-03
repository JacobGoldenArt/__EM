# \_\_EM

App flow:

1. Main() ->
2. Input.cli_in() ->
3. Api.query_chat(user_message, config) ->
4. Chat.chat_api(user_message, config) ->
5. Methods to init chat_history:

   - Memory.set_sys_message(sys_message)
   - Memory.add_message("user", user_message)
   - retrieve Memory.chat_history.copy() and save as session_chat_history

6. Calling the OpenAI api:
   - Pass in our config params and session_chat_history (as the messages array)
   - save AI response as assistant_message
   - ass assistant_response to Memory.add_message
   - Save sys, user and assistant by appending it to chat_history
     and saving to/appending to a json file: Memory.save_to_memory()
   - Output assistant response to Output.cli_out(assistant_message)

Todo:

- Seperate classes into their own files.
- Modify save_to_memory to save chat_history to a simple Database
  rather then a json file. Redis, SQLlite or similar.
- Create a behind the scenes Memory manager using OpenAI API.
  This will have methods like:
  - Summarize Conversation.
  - Extract important details to build Knowledge Graph from so that the assistant can recall these important details in the future.
  - Save knowledge graph as a vecor database that we can do RAG on to retrieve important historical chat details during a current chat.
  - Use the retriever class to allow the assistant to query the memory vector database and return knowledge to add to the context window as needed.
  - Checkout Openai cookbook for creating the RAG/DB class/methods
- Use openAI's function calling ability to provide it with Tools (JSON schemas) to utilize to do things like search/scrape the web, use external apis like: Weather API, Current News etc...
- Build Text to speech and Speech to text methods so that I can speak to the assistant with voice and it can respond with audio.
- Create a file uploading method to allow me to ingest text, photos, pds etc, chunk and vectorize them and store in our vector database, then query those files as context durring chats.
