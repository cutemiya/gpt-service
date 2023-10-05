import model.model
import utils.gpt


class GptService:
    @staticmethod
    def generate_message(text: str) -> str:
        return utils.gpt.get_gpt_mess(text)

    @staticmethod
    def generate_test(text: str, description: str):
        questions: list[model.model.Question] = []

        for _ in range(3):
            question = utils.gpt.get_gpt_mess(f"Придумай другой легкий вопрос на тему {text}")
            answers: list[model.model.Answer] = []

            for _ in range(3):
                answer_text = utils.gpt.get_gpt_mess(f"Придумай другой неправильный ответ для вопроса: {question}")
                answers.append(model.model.Answer(text=answer_text, is_right=False))

            answer_text = utils.gpt.get_gpt_mess(f"Придумай правильный ответ для вопроса: {question}")
            answers.append(model.model.Answer(text=answer_text, is_right=True))
            questions.append(model.model.Question(title=question, answers=answers))

        return model.model.Test(title=text, description=description, questions=questions)

    @staticmethod
    def generate_question(text: str, q_type: int) -> model.model.Question:
        answers: list[model.model.Answer] = []
        question = utils.gpt.get_gpt_mess(f"Придумай другой {utils.gpt.get_question_type(q_type)} вопрос на тему {text}")

        for _ in range(3):
            answer_text = utils.gpt.get_gpt_mess(f"Придумай неправильный ответ на вопрос: {question}")
            answers.append(model.model.Answer(text=answer_text, is_right=False))

        answer_text = utils.gpt.get_gpt_mess(f"Придумай правильный ответ на вопрос: {question}")
        answers.append(model.model.Answer(text=answer_text, is_right=True))

        return model.model.Question(title=question, answers=answers)
