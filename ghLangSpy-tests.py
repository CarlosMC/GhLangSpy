from ghLangS import getLangList

###
# test if langs/bytes list is not empty
###
def test_getLangList():
    langList=getLangList()
    assert len(langList) > 0, "No langs/bytes returned"


