from groq import Groq
from app.core.config import settings

class GeneratorService:
    def build_context(self,chunks):
        context_parts=[]
        for chunk in chunks:
            context_parts.append(chunk["content"]) 
        return "\n\n".join(context_parts)
    

    def __init__(self):
        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def generate_answer(self,question,context):
        prompt = f"""
        Answer the question using the provided repository context.

        Question:
        {question}

        Context:
        {context}
        """   

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.choices[0].message.content

        return {
    "answer": answer
}

generator_service= GeneratorService()       