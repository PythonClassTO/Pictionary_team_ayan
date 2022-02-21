from ntpath import join
from pydoc_data.topics import topics
import random
from random import randint
import queue
import threading, time



#animals = ["Dog", "Cat", "Tiger", "Lion",  "Giraffe", "Elephant", "Fish", "Bear", "Rabbit", "Kangaroo", "Penguin",   "Rat", "Bird", "Hamster", "Squirrel"]#15 topics
#fruits = ["Apple", "Banana", "Orange", "Strawberry", "Blueberry", "Raspberry", "Blackberry", "Mango", "Avocado", "Kiwi", "Pineapple", "Watermelon", "Pear", "Grapes", "Peach",]#15 topics
#countries = ["Canada", "United States Of America", "Mexico", "Brazil", "Argentina", "Africa", "China", "Japan", "India", "Sri Lanka", "Australia", "Russia", "Iran", "New Zealand", "United Kingdom"]#15 topics
#sports =["Basketball", "Soccer", "Baseball", "Football", "Tennis", "Badminton", "Volleyball", "Hockey", "Cricket", "Golf", "Curling", "Gymnastics", "Polo", "Cycling", "Skiing",] #15 topics

animals = ["Dog", "Cat", "Tiger", "Lion",  "Giraffe", "Elephant", "Fish", "Bear", "Rabbit", "Kangaroo", "Penguin",   "Rat", "Bird", "Hamster", "Squirrel"]
fruits =  ["Apple", "Banana", "Orange", "Strawberry", "Blueberry", "Raspberry", "Blackberry", "Mango", "Avocado", "Kiwi", "Pineapple", "Watermelon", "Pear", "Grapes", "Peach",]
countries =  ["Canada", "United States Of America", "Mexico", "Brazil", "Argentina", "Africa", "China", "Japan", "India", "Sri Lanka", "Australia", "Russia", "Iran", "New Zealand", "United Kingdom"]
sports = ["Basketball", "Soccer", "Baseball", "Football", "Tennis", "Badminton", "Volleyball", "Hockey", "Cricket", "Golf", "Curling", "Gymnastics", "Polo", "Cycling", "Skiing",]
finaltopiclist = []
topic2 = []
finaltopiclist = [animals, fruits, countries, sports]
def randomize():
     random_topic = []
     random_topic = random.choice(finaltopiclist)
     final_word = random.sample(random_topic,1)
     print(final_word)
     topic2.append(final_word)
#randomize()

def askThread(queue):
     question = "The word is" + randomize() + "if you got it correct press anything\n"
     value = input(question)
     queue.put(value)

def main():
    q = queue.Queue()
    while True:
        answer = input("Ask question? \n")
        if answer == 'yes':
            thread = threading.Thread(target=askThread, args=(q,))
            thread.start()
            i = 60
            while i > 0:
                print("Time remaining" + str(i))
                time.sleep(1)
                i=i-1
                if(not q.empty()):
                  val=q.get()
                  print(val)
                  break
            print("user pressed in " + str(i) + 'secs')  
        if answer == 'no':
          print("thanks for playing!")
          break
if __name__ == '__main__':
  main()
