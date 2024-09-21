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


    def __str__(self):
        if len(self.book_answer_list) == 0:
            return ""
        else:
            return " - ".join(self.book_answer_list)

    def check_get_answer(self, question):
        if question in self.questions_asked_list:
            index = self.questions_asked_list.index((question))
            return f"I have already answered this question. The answer is: {self.book_answer_list[self.answered_list[index]]}"
        else:
        # Pick a random answer and store its index in answered_list
            random_index = random.randint(0, len(self.book_answer_list) - 1)
            answer = self.book_answer_list[random_index]
            self.questions_asked_list.append(question)
            self.answered_list.append(random_index)
            return f"{answer}"


    def open_book(self):
        while True:
            turn_number= len(self.questions_asked_list) + 1
            question = input(f"turn {turn_number} - Please enter your question: ")
            if question == "Done":
                print("Goodbye! See you soon.")
                break
            answer = self.check_get_answer(question)
            print(answer)
        if len(self.answered_list)==0:
            print("Empty")
            return []
    

    def answer_log(self):
        turn_number = 1
        answer_count= {}
        for index in self.answered_list:
            answer = self.book_answer_list[index].lower()
            if answer in answer_count:
                answer_count[answer] += 1
            else:
                answer_count[answer] = 1
        frequency_list = []
        for answer, count in answer_count.items():
            frequency_list.append(f"{count}-{answer}")
        for i in range(len(frequency_list)):
            for j in range(i+1, len(frequency_list)):
                count_i = int(frequency_list[i].split(' - ')[0])
                count_j = int(frequency_list[j].split(' - ')[0])
                if count_j > count_i:
                    frequency_list[i], frequency_list[j] = frequency_list[j], frequency_list[i]
        return frequency_list
    
    
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
    book1 = DigitalBookofAnswers(["Stay Positive", "Go For It", "Enjoy It"])
    print("Testing answer_log with no questions asked:")
    res = book1.answer_log()

    print("Expected: [], Actual: " + str(res))
    print(" ")


    book2 = DigitalBookofAnswers(["Stay Positive", "Go For It", "Enjoy It"])
    book2.answered_list = [2, 1, 2]
    print("Testing answer_log with answers [2, 1, 2]:")
    expected = ["2 - enjoy it", "1 - go for it"]
    res = book2.answer_log()
    print("Expected: " + str(expected) + ", Actual: " + str(res))
    print(" ")

 
    print("Testing open_book first prompt (enter 'Done' to finish):")
    book3 = DigitalBookofAnswers(["Follow Your Inner Voice", "Stay Positive", "Go For It"])
    book3.open_book()

    print("Testing check_get_answer for repeated questions:")
    book4 = DigitalBookofAnswers(["Follow Your Inner Voice"])
    response1 = book4.check_get_answer("Will I succeed?")
    response2 = book4.check_get_answer("Will I succeed?")
    expected_response2 = "I've already answered this question. The answer is: Follow Your Inner Voice"
    print("First response: " + (response1))
    print("Second response: " + str(response2))
    print("Expected: " + str(expected_response2) + ", Actual: " + str(response2))
    print(" ")
    print("Testing that check_get_answer adds answer index to answered_list:")
    book4.questions_asked_list = []



# Only run the main function if this file is being run (not imported)
if DigitalBookofAnswers == main():
    print("Starting my_test() for extra credit...")
    book1 = DigitalBookofAnswers(["Stay Positive", "Go For It", "Enjoy It"])
    print("Testing answer_log with no questions asked:")
    res = book1.answer_log()

    print("Expected: [], Actual: " + str(res))
    print(" ")


    book2 = DigitalBookofAnswers(["Stay Positive", "Go For It", "Enjoy It"])
    book2.answered_list = [2, 1, 2]
    print("Testing answer_log with answers [2, 1, 2]:")
    expected = ["2 - enjoy it", "1 - go for it"]
    res = book2.answer_log()
    print("Expected: " + str(expected) + ", Actual: " + str(res))
    print(" ")

 
    print("Testing open_book first prompt (enter 'Done' to finish):")
    book3 = DigitalBookofAnswers(["Follow Your Inner Voice", "Stay Positive", "Go For It"])
    book3.open_book()

    print("Testing check_get_answer for repeated questions:")
    book4 = DigitalBookofAnswers(["Follow Your Inner Voice"])
    response1 = book4.check_get_answer("Will I succeed?")
    response2 = book4.check_get_answer("Will I succeed?")
    expected_response2 = "I've already answered this question. The answer is: Follow Your Inner Voice"
    print("First response: " + (response1))
    print("Second response: " + str(response2))
    print("Expected: " + str(expected_response2) + ", Actual: " + str(response2))
    print(" ")
    print("Testing that check_get_answer adds answer index to answered_list:")
    book4.questions_asked_list = []

