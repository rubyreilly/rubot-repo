def moveRubot(value):
    print ("received %s" %value)

# def sendRubot(value):
#     print ("received %s" %value)


def processRequest(data):

    rubot_directional = {'forward','backward','CW','CCW','clear','auto'}

    result=""
    result2=""
    result3=""
    result4=""

    if data in rubot_directional:
        if(data=="forward"):
            result = moveRubot("forw")
        elif(data=="backward"):
            result = moveRubot("back")
        elif(data=="CW"):
            result = moveRubot("cloc")
        elif(data=="CCW"):
            resutl = moveRubot("ccws")
        elif(data=="stop"):
            result = moveRubot("stop")
        elif(data=="hold"):
            result = moveRubot("hold")
    else:
        result=moveRubot(data)
