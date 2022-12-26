import openai
from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.post("/openai_completion")
def openai_completion(request: Request):
    # Extract the "prompt" parameter from the POST request
    prompt = request.query_params.get("prompt")

    # Use the OpenAI API to generate a completion for the prompt
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Return the completion as a response
    return Response(completion.text, status_code=200)
