This group project is an implementation of a heart disease prediction system using fuzzy system.


# How to run the project
- To install the requirements and used libraries, first enter the main directory and then install the requirements using the pip install -r requirements.txt command. Then easily run app.py ( it's on port 8448. do not change it)
```
pip install -r requirements.txt
python3 app.py

```
# Inputs for diagnosis

### Chest pain
- This entry specifies the degree of chest pain. This input is crisp value, and It has only four values of 1, 2, 3, or 4, those indicates "typical angina." "atypical angina." "non-anginal pain," and "asymptomatic." chest pains respectively.

It means "asymptomatic".
### Blood pressure
- This input value specifies the blood pressure of the person. The inputs take the form of systolic and diastolic value
### Cholesterol
- This input value specifies the level of cholesterol of the person.
### Blood sugar
- This input value specifies the blood sugar level of the person.
### Exercise
- If it is zero, it means the patient never exercises or rarely exercise (> once per three months). If it is one, it means that the patient exercises often or occasionally exercises.
### Maximum heart rate
- This input shows the maximum heart rate of a person during 24 ours.
### Gender
- If it is zero, it means the patient is a man, and if it is one, it means that the patient is a woman.
### Age
- This entry specifies the age of the person
