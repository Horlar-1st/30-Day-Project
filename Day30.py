# Day30: Quiz Game

# Importing necessary libraries
import gradio as gr

# A simple quiz game that asks multiple-choice questions and keeps track of the score.
class Question:
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index

# List of questions
questions = [
        Question("What is the capital of France?", ["London", "Paris", "Rome"], "Paris"),
        Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter"], "Mars"),
        Question("What is the highest mountain in the world?", ["Mount Kilimanjaro", "Mount Everest", "K2"], "Mount Everest"),
        Question("Which country is known as 'The Land of the Rising Sun?'", ["China", "Thailand", "Japan"], "Japan"),
        Question("What is the chemical formula for water", ["H2O2", "CO2", "H2O"], "H2O"),
        Question("Who was the first person to walk on the moon?", ["Buzz Aldrin", "Neil Armstrong", "Michael Collins"], "Neil Armstrong"),
        Question("What is the name of the longest river in the world?", ["Nile River", "Amazon River", "Yangtze River"], "Nile River"),
        Question("Which element has the chemical symbol 'O'?", ["Oxygen", "Gold", "Silver"], "Oxygen"),
        Question("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe"], "Blue Whale"),
        Question("What is the smallest prime number?", ["0", "1", "2"], "2"),
        Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Mark Twain"], "William Shakespeare"),
        Question("What is the hardest natural substance on Earth?", ["Gold", "Iron", "Diamond"], "Diamond"),
        Question("Which planet is closest to the sun?", ["Venus", "Earth", "Mercury"], "Mercury"),
        Question("What is the main ingredient in guacamole?", ["Tomato", "Avocado", "Cucumber"], "Avocado"),
        Question("What is the largest organ in the human body?", ["Liver", "Skin", "Heart"], "Skin"),
        Question("What is the capital city of Australia?", ["Sydney", "Melbourne", "Canberra"], "Canberra"),
        Question("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Carbon Dioxide", "Nitrogen"], "Carbon Dioxide"),
        Question("What is the currency of Japan?", ["Yen", "Dollar", "Euro"], "Yen"),
        Question("Who painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso  ", "Leonardo da Vinci"], "Leonardo da Vinci"),
        Question("What is the largest desert in the world?", ["Sahara", "Gobi", "Antarctic Desert"], "Antarctic Desert")
        # Add more questions
    ]

# Initialize score and question index
current_question_index = 0
score = 0
length_of_quiz = len(questions)

# Function to check the answer, update the score, submit answer and move to the next question
def submit_answer(choice_text):
    global current_question_index, score
    if current_question_index < length_of_quiz:
        correct_answer = questions[current_question_index].correct_index
        if choice_text == correct_answer:
            score += 1
            feedback = "Correct!"
        else:
            feedback = f"Incorrect. Correct answer was: {correct_answer}"
        current_question_index += 1

    if current_question_index < length_of_quiz:
        q = questions[current_question_index]
        return (
            feedback,
            str(score/current_question_index*100) + "%",
            q.text,
            gr.update(choices=q.options, value=None)
        )
    else:
        return (
            f"Quiz Over! Final Score: {score}/{length_of_quiz}",
            str(score/current_question_index*100) + "%",
            "Quiz Finished!",
            gr.update(choices=[], value=None)
        )

# function to reset the game
def reset_game():
    global current_question_index, score
    current_question_index = 0
    score = 0
    q = questions[current_question_index]
    return (
        "", 
        0, 
        q.text, 
        gr.update(choices=q.options, value=None)
    )


# Gradio Interface
with gr.Blocks() as quiz_game:
    gr.Markdown("# Python Quiz Game")
    
    with gr.Row():
        question_text = gr.Textbox(value=questions[current_question_index].text, label="Question", interactive=False)

    with gr.Row():
        options_radio = gr.Radio(choices=questions[current_question_index].options, label="Choose your answer:")

    with gr.Row():
        submit_btn = gr.Button("Submit Answer")

    with gr.Row():
        feedback_output = gr.Markdown()

    with gr.Row():
        score_output = gr.Textbox(value="0%", label="Score", interactive=False)

    with gr.Row():
        reset_btn = gr.Button("Reset Quiz")

    submit_btn.click(
        submit_answer,
        inputs=[options_radio],
        outputs=[feedback_output, score_output, question_text, options_radio]
    )
    reset_btn.click(
        reset_game,
        inputs=[],
        outputs=[feedback_output, score_output, question_text, options_radio]
    )

# Launch the app
quiz_game.launch()          # To create a public link, set `share=True` in `launch()`.


# end of code
