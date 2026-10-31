from question_marks import question_marks


class TestQuestionMarks:
    def test_given_1(self):
        assert question_marks("acc?7??sss?3rr1??????5") == "true"

    def test_given_2(self):
        assert question_marks("arrb6???4xxbl5???eee5") == "true"

    def test_given_3(self):
        assert question_marks("5??aaaaaaaaaaaaaaaaaaa?5?a??5") == "true"

    def test_given_4(self):
        assert question_marks("9???1???9??1???9") == "false"

    def test_given_5(self):
        assert question_marks("5??aaaaaaaaaaaaaaaaaaa?5?5") == "false"
