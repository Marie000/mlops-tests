from hello import hello_function


def test_hello():
    assert hello_function() == "hello world"
