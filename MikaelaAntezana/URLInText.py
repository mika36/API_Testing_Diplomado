def urlInText(text):
    lastPosition = ' '
    counter = 1
    initialPosition = text.find("http://") + 4
    currentPosition = initialPosition
    previousText= 'http'
    while(text[currentPosition] != lastPosition):
        urlText = previousText+text[currentPosition]
        previousText =urlText
        currentPosition += 1
    #else:
    # print("no existe una URL en la cadena")
    print(urlText)

urlInText("12http://hello blabla")