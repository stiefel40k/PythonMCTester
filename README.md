# Requirements #
You need python3 installed (it might run on py2 as well, but I didn't test it)

# What is this #
So basically I needed a tool to learn for an multiple choice test so I wrote one. It shoots you with a question and the possibly answers and waits until you answer the question. After you did, it tells you if your answer was right or wrong, and if wrong, what would have been the right answer.

# How to run it #
`python mc_tester.py <path_to_catalog>`

# The catalog #
The catalog is in JSON format.
```
{"questions":[
    {"q":"<here comes the question>",
    "answers":[
      {"text":"<Answer one text>", "id":1},
      {"text":"<Answer two text>", "id":2},
      {"text":"<Answer three text>", "id":3},
      {"text":"<Answer four text>", "id":4},
      ...
      {"text":"<Answer n text>", "id":n}
    ],
    "rightids":"<id of the right answers as one number>"}
]}
```
Due to the parsing of the userinput a question can only have maximally 9 RIGHT answers.

# Disclaimer #
I don't guarantee that the questions and the answers are correct or complete. So if you would fail the real test because you only learnt with my tool I'm not responsible for that.
