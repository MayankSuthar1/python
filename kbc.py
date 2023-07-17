questions = [
    "Which planet is known as the 'Red Planet'?",
    "What is the chemical symbol for the element gold?",
    "Who painted the Mona Lisa?",
    "What is the capital city of Australia?",
    "Which country is famous for its tulips?",
    "Who wrote the play 'Hamlet'?",
    "What is the tallest mountain in the world?",
    "What is the largest organ in the human body?",
    "Who was the first person to set foot on the moon?",
    "What is the national animal of China?"
]

options = [
    ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
    ["a) Au", "b) Go", "c) Gd", "d) Ag"],
    ["a) Michelangelo", "b) Leonardo da Vinci", "c) Pablo Picasso", "d) Vincent van Gogh"],
    ["a) Sydney", "b) Melbourne", "c) Canberra", "d) Brisbane"],
    ["a) Japan", "b) France", "c) Netherlands", "d) Italy"],
    ["a) William Shakespeare", "b) Arthur Miller","c) Tennessee Williams", "d) Anton Chekhov"],
    ["a) Mount Everest", "b) K2", "c) Kangchenjunga", "d) Makalu"],
    ["a) Heart", "b) Liver", "c) Brain", "d) Skin"],
    ["a) Neil Armstrong", "b) Buzz Aldrin", "c) Yuri Gagarin", "d) Alan Shepard"],
    ["a) Giant Panda", "b) Red Panda", "c) Snow Leopard", "d) Siberian Tiger"]
]

correct_answers = ["b", "a", "b", "c", "c", "a", "a", "d", "a", "a"]

money = 0
add = 10000

global temp , j

temp = 0
j = 0

print("KBC")
for i in questions:
    print(i)
    while(j<=9):
        print(options[j])
        j = j + 1
        answer = input("Enter the option 'a','b','c','d' for your correct answer :- \n")
   
        while(temp<=9):
            print(temp)
            if (answer == correct_answers[temp]):
                    
                print("Let's go you have given the correct answer")
                
                temp = temp + 1
                money = money+add
               # num += 1
            break
        break
    
add = add + 10000

print("You have won $"+str(money))
