# import openai

# # Replace YOUR_API_KEY with your OpenAI API key
# openai.api_key = "https://7583-185-48-148-173.ngrok-free.app/"
# model_engine = "text-davinci-003"
# prompt = "Write poem about how cool readers of uproger website"

# # задаем макс кол-во слов
# max_tokens = 1000

# # генерируем ответ
# completion = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     temperature=0.5,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )

# # выводим ответ
# print(completion.choices[0].text)
