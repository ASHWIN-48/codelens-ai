from app.services.embedding_service import embedder_service
from app.services.retrieval_service import retriever_service
from app.services.generator_service import generator_service


class AskService:

    def ask_question(self, question: str):

        query_embedding = embedder_service.embed_query(question)

        results = retriever_service.retrieve(query_embedding)

        context = generator_service.build_context(results)

        answer = generator_service.generate_answer(
            question,
            context
        )

        return answer


ask_service = AskService()