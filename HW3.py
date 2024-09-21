# Your name: Jessica Imaz
# Your student id: 24536986
# Your email: jimaz@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# Asked ChatGPT to help correct the code structure and methods according to the assignment requirements.

import random

class DigitalBookofAnswers:
    def __init__(self, answers):
        self.book_answer_list = answers
        self.questions_asked_list = []
        self.answered_list = []

#"""Returns a string with all the answers in book_answer_list separated by dashes"""
    def __str__(self):
        if self.book_answer_list:
            return " - ".join(self.book_answer_list)
        else:
            return ""

    def check_get_answer(self, question):
        if question in self.questions_asked_list:
            index = self.questions_asked_list.index(str(question))
            answer = self.book_answer_list[self.answered_list[index]]
            ans = "I have already answered this question. The answer is: "
            ans += str(answer)
            return ans
        else:
        # Pick a random answer and store its index in answered_list
            random_index = random.randint(0, len(self.book_answer_list) - 1)
            random_answer = self.book_answer_list[random_index]
            self.questions_asked_list.append(str(question))
            self.answered_list.append(random_index)
            return random_answer


    def open_book(self):
        while True:
            turn_number = len(self.questions_asked_list) + 1
            input_str = "Turn "
            input_str += str(turn_number)
            input_str += " - Please enter your question: "
            question = input(input_str)
            if question == "Done":
                print("Goodbye! See you soon.")
                break
            else:
                answer = self.check_get_answer(question)
                print(answer)

    def answer_log(self):
        if not self.answered_list:
            print("Empty")
            return []

        # Create a frequency dictionary for answers
        answer_count = {}
        for index in self.answered_list:
            answer = self.book_answer_list[index].lower()
            if answer in answer_count:
                answer_count[answer] += 1
            else:
                answer_count[answer] = 1

        # Sort the answers by frequency in descending order
        sorted_answers = sorted(
            answer_count.items(), key=lambda x: x[1], reverse=True
        )

        # Format the output list
        answer_log_list = []        
        for answer, count in sorted_answers:
            ans_str = str(count) + " - " + str(answer)
            answer_log_list.append(ans_str)

        return answer_log_list
    
# Main function to run the digital book of answers
def main():
    answers_list = [
        "Follow Your Inner Voice",
        "Stay Positive",
        "Go For It",
        "Believe in Yourself",
        "Stay Open to the Future",
        "Enjoy It",
    ]
    book = DigitalBookofAnswers(answers_list)
    book.open_book()
    print("Answer Log:")
    print(book.answer_log())

# Test cases
def my_test():
    print("Starting my_test() for extra credit...")

    # 1 point: Correct output from answer_log when no questions have been asked.
    book1 = DigitalBookofAnswers(["Stay Positive", "Go For It", "Enjoy It"])
    print("Testing answer_log with no questions asked:")
    res = book1.answer_log()

    print("Expected: [], Actual: " + str(res))
    print(" ")

    # 2 points: Correct behavior from answer_log when answers_list is ['Stay Positive', 'Go For It', 'Enjoy It']
    # and answered_list is [2, 1, 2]
    book2 = DigitalBookofAnswers(["Stay Positive", "Go For It", "Enjoy It"])
    book2.answered_list = [2, 1, 2]
    print("Testing answer_log with answers [2, 1, 2]:")
    expected = ["2 - enjoy it", "1 - go for it"]
    res = book2.answer_log()
    print("Expected: " + str(expected) + ", Actual: " + str(res))
    print(" ")

    # 1 point: Correct prompt from open_book to ask the first question Turn 1 - Please enter your question: 
    print("Testing open_book first prompt (enter 'Done' to finish):")
    book3 = DigitalBookofAnswers(["Follow Your Inner Voice", "Stay Positive", "Go For It"])
    book3.open_book()

    # 1 point: Correct output from check_get_answer when the same question is asked twice.
    print("Testing check_get_answer for repeated questions:")
    book4 = DigitalBookofAnswers(["Follow Your Inner Voice"])
    response1 = book4.check_get_answer("Will I succeed?")
    response2 = book4.check_get_answer("Will I succeed?")
    expected_response2 = "I've already answered this question. The answer is: Follow Your Inner Voice"
    print("First response: " + str(response1))
    print("Second response: " + str(response2))
    print("Expected: " + str(expected_response2) + ", Actual: " + str(response2))
    print(" ")

    print("Testing that check_get_answer adds answer index to answered_list:")
    book4.questions_asked_list = []




# Only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    # main()  # Uncomment this line to run the main function
    my_test()  # Run test cases
