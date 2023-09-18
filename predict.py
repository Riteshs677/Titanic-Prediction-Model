import pickle
import numpy as np
pipe = pickle.load(open('pipe.pkl','rb'))
import os
print("""Pridiction model""")
Pclass = int(input("Enter the Passenger class_"))
Sex = input("Enter the Gender of that person_")
age = float(input("Age of that person_"))
Ss = input("Number of Souse with them_")
Par = input("Number of Parants with them_")
Fare = float(input("What was the Fare_"))
Emberked = input("Place of that person (S,Q,C)_").upper()

test_input2 = np.array([Pclass,Sex,age,Ss,Par,Fare,Emberked],dtype=object).reshape(1,7)
# test_input2 = np.array([2, 'male', 31.0, 0, 0, 10.5, 'S'],dtype=object).reshape(1,7)
os.system('cls' if os.name == 'nt' else 'clear')
print(f"person has -> {pipe.predict(test_input2)[0]}")