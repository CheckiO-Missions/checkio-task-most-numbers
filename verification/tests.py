"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [1, 2, 3],
            "answer": 2,
            "explanation": "3-1=2"
        },
        {
            "input": [5, -5],
            "answer": 10,
            "explanation": "5-(-5)=10"
        },
        {
            "input": [10.2, -2.2, 0, 1.1, 0.5],
            "answer": 12.4,
            "explanation": "10.2-(-2.2)=12.4"
        }

    ],
    "Extra": [
        {
            "input": [6, 3],
            "answer": 9,
            "explanation": "6+3=?"
        },
        {
            "input": [6, 7],
            "answer": 13,
            "explanation": "6+7=?"
        }
    ]
}
