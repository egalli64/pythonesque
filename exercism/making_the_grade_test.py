"""
Exercism Python track

Source: https://exercism.org/tracks/python
My solutions: https://github.com/egalli64/pythonesque exercism folder

Making the Grade https://exercism.org/tracks/python/exercises/making-the-grade

Looping
"""
from making_the_grade import *


class TestRoundScores:
    def test_given_1(self):
        actual = round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3])
        expected = [90, 40, 55, 70, 31, 25, 80, 95, 39, 40]
        assert actual == expected


class TestCountFailedStudents:
    def test_given_1(self):
        assert count_failed_students([90, 40, 55, 70, 30, 25, 80, 95, 38, 40]) == 5


class TestAboveThreshold:
    def test_given_1(self):
        assert above_threshold([90, 40, 55, 70, 30, 68, 70, 75, 83, 96], 75) == [90, 75, 83, 96]


class TestLetterGrade:
    def test_given_1(self):
        assert letter_grades(100) == [41, 56, 71, 86]

    def test_given_2(self):
        assert letter_grades(97) == [41, 55, 69, 83]


class TestStudentRanking:
    def test_given_1(self):
        scores = [100, 99, 90, 84, 66, 53, 47]
        names = ['Joci', 'Sara', 'Kora', 'Jan', 'John', 'Bern', 'Fred']
        expected = ['1. Joci: 100', '2. Sara: 99', '3. Kora: 90', '4. Jan: 84', '5. John: 66', '6. Bern: 53',
                    '7. Fred: 47']
        assert student_ranking(scores, names) == expected


class TestPerfectScore:
    def test_given_1(self):
        assert perfect_score([["Charles", 90], ["Tony", 80], ["Alex", 100]]) == ["Alex", 100]

    def test_given_2(self):
        assert perfect_score([["Charles", 90], ["Tony", 80]]) == []
