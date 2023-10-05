import g4f


MODEL = "gpt-3.5-turbo"


def get_gpt_mess(req: str) -> str:
    """
    :req: text of request
    :return: response string
    """
    response = g4f.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": req}],
        stream=True
    )
    result_string = ""

    for char in response:
        result_string += char

    return result_string


def get_question_type(q_type: int) -> str:
    """
    :q_type: type of question 0 - easy, 1 - hard
    :return: return string diff
    """
    if q_type:
        return "cложный"

    return "легкий"