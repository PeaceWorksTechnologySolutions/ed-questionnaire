#!/usr/bin/python

from questionnaire.models import Answer
        
def get_value_for_run_question(runid, questionid):
    runanswer = Answer.objects.filter(runid=runid,question__id=questionid)
    if len(runanswer) > 0:
        return runanswer[0].answer
    else:
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
