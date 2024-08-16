from project import *


def test_f_name():
    assert (
        f_name(
            "C:\\Users\\user\\Desktop\\vs_code\\afsal_python\\data_sharing\\images\\team1.jpg"
        )
        == "team1.jpg"
    )
    assert f_name("photo.jpg") == "photo.jpg"


def test_input_validation():
    assert input_validation("afsal", "hello") == True
    assert input_validation("afsal-", "hello") == False
    assert input_validation("afsal", "hello-") == False
    assert input_validation("af", "hello") == False
    assert input_validation("afsal", "ho") == False
    assert input_validation("afsal ali", "hello") == False
    assert input_validation("asna", "123") == True


def test_login():
    assert login(1, "afsal") == "afsal"
    assert login(0, "afsal") == None


def test_signup():
    assert signup(1, "afsal", 123) == None
    assert signup(0, "david", 12345) == "david"
