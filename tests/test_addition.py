from additionpackage import additionmodule

def additionmodule_test():
    """Make sure addition_module works"""

    assert additionmodule.addition(5,2) == 7, "Incorrect"
    assert additionmodule.addition(2,2) == 4, "Incorrect"
    assert additionmodule.addition(7,3) == 10, "Incorrect"
    assert additionmodule.addition(5,5) == 10, "Incorrect"

additionmodule_test()