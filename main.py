def decision():
    global scenenumber
    global 그리핀도르
    global 슬리데린
    global 후플푸프
    global 래번클로
    maxanswer = max(그리핀도르, 슬리데린, 후플푸프, 래번클로)
    answerlist = [그리핀도르, 슬리데린, 후플푸프, 래번클로]
    samecount = 0
    sameindex = 0
    samelist = []
    for answervalue in answerlist:
        if maxanswer - answervalue == 0:
            samecount = samecount + 1
            samelist.append(sameindex)
        sameindex = sameindex + 1

    print(samecount)
    print(samelist)
    if samecount == 1:
        print(str(1))
        if samelist[0] == 0:
            window.after(2000, scene31)
            scene30()
        if samelist[0] == 1:
            window.after(2000, scene32)
            scene30()
        if samelist[0] == 2:
            window.after(2000, scene33)
            scene30()
        if samelist[0] == 3:
            window.after(2000, scene34)
            scene30()

    if samecount == 2:
        if samelist[0] == 0 and samelist[1] == 1:
            window.after(2000, scene20)
            scene30()
            scene20()
        if samelist[0] == 1 and samelist[1] == 2:
            window.after(2000, scene21)
            scene30()
        if samelist[0] == 3 and samelist[1] == 1:
            window.after(2000, scene22)
            scene30()
        if samelist[0] == 0 and samelist[1] == 2:
            window.after(2000, scene23)
            scene30()
        if samelist[0] == 0 and samelist[1] == 3:
            window.after(2000, scene24)
            scene30()
        if samelist[0] == 2 and samelist[1] == 3:
            window.after(2000, scene25)
            scene30()

    if samecount == 3:
        if samelist[0] == 0 and samelist[1] == 2 and samelist[2] == 3:
            window.after(2000, scene26)
            scene30()
        if samelist[0] == 0 and samelist[1] == 1 and samelist[2] == 2:
            window.after(2000, scene27)
            scene30()
        if samelist[0] == 1 and samelist[1] == 2 and samelist[2] == 3:
            window.after(2000, scene28)
            scene30()
        if samelist[0] == 0 and samelist[1] == 1 and samelist[2] == 3:
            window.after(2000, scene29)
            scene30()


def mouseclick(event):
    global inputwindow
    global scenenumber
    global 그리핀도르
    global 슬리데린
    global 후플푸프
    global 래번클로

    def react_click(inputx, inputy, startx, endx, starty, endy, scene, dormitory, dormitory2=None):
        global inputwindow
        global scenenumber
        global scenenumbercheck
        global 그리핀도르
        global 슬리데린
        global 후플푸프
        global 래번클로
        if (inputx > startx and inputx < endx) and (inputy > starty and inputy < endy) and inputwindow == 1:
            if dormitory == "그리핀도르":
                그리핀도르 = 그리핀도르 + 1
            elif dormitory == "슬리데린":
                슬리데린 = 슬리데린 + 1
            elif dormitory == "후플푸프":
                후플푸프 = 후플푸프 + 1
            elif dormitory == "래번클로":
                래번클로 = 래번클로 + 1

            if dormitory2 == "그리핀도르":
                그리핀도르 = 그리핀도르 + 1
            elif dormitory2 == "슬리데린":
                슬리데린 = 슬리데린 + 1
            elif dormitory2 == "후플푸프":
                후플푸프 = 후플푸프 + 1
            elif dormitory2 == "래번클로":
                래번클로 = 래번클로 + 1

            if scenenumber == scenenumbercheck and scenenumber == 2:
                scenenumbercheck = scenenumbercheck + 1
                scene3()

            elif scenenumber == scenenumbercheck and scenenumber == 3:
                scenenumbercheck = scenenumbercheck + 1
                scene4()
            elif scenenumber == scenenumbercheck and scenenumber == 4:
                scenenumbercheck = scenenumbercheck + 1
                scene5()

            elif scenenumber == scenenumbercheck and scenenumber == 5:
                scenenumbercheck = scenenumbercheck + 1
                scene6()

            elif scenenumber == scenenumbercheck and scenenumber == 6:
                scenenumbercheck = scenenumbercheck + 1
                scene7()

            elif scenenumber == scenenumbercheck and scenenumber == 7:
                scenenumbercheck = scenenumbercheck + 1
                scene8()

            elif scenenumber == scenenumbercheck and scenenumber == 8:
                scenenumbercheck = scenenumbercheck + 1
                scene9()

            elif scenenumber == scenenumbercheck and scenenumber == 9:
                scenenumbercheck = scenenumbercheck + 1
                scene10()

            elif scenenumber == scenenumbercheck and scenenumber == 10:
                scenenumbercheck = scenenumbercheck + 1
                scene11()

            elif scenenumber == scenenumbercheck and scenenumber == 11:
                scenenumbercheck = scenenumbercheck + 1
                scene12()

            elif scenenumber == scenenumbercheck and scenenumber == 12:
                scenenumbercheck = scenenumbercheck + 1
                scene13()

            elif scenenumber == scenenumbercheck and scenenumber == 13:
                scenenumbercheck = scenenumbercheck + 1
                scene14()

            elif scenenumber == scenenumbercheck and scenenumber == 14:
                scenenumbercheck = scenenumbercheck + 1
                scene15()

            elif scenenumber == scenenumbercheck and scenenumber == 15:
                scenenumbercheck = scenenumbercheck + 1
                scene16()

            elif scenenumber == scenenumbercheck and scenenumber == 16:
                scenenumbercheck = scenenumbercheck + 1
                scene17()

            elif scenenumber == scenenumbercheck and scenenumber == 17:
                scenenumbercheck = scenenumbercheck + 1
                scene18()

            elif scenenumber == scenenumbercheck and scenenumber == 18:
                scenenumbercheck = scenenumbercheck + 1
                scene19()

            elif scenenumber == scenenumbercheck and scenenumber == 19:
                decision()

            elif scenenumber == 31 or scenenumber == 32 or scenenumber == 33 or scenenumber == 34:

                scenenumber = 0
                scenenumbercheck = 2
                inputwindow = 0
                username = ''
                그리핀도르 = 0
                슬리데린 = 0
                후플푸프 = 0
                래번클로 = 0

                scenegifname = 'main.gif'
                canvas.delete('all')
                canvas.pack(expand=True)
                background_img = PhotoImage(master=canvas, file=scenegifname)
                bg = canvas.create_image(0, 0, anchor="nw", image=background_img)
                img = PhotoImage(file="start1.png")
                image = canvas.create_image(218, 495, anchor=NW, image=img)

                window.update()
                window.mainloop()

    def react_decision(inputx, inputy, startx, endx, starty, endy, scene, dormitory):
        global inputwindow
        global scenenumber
        if scenenumber == scene and scenenumber == 20:
            scene30()
            root.after(1000)
            if dormitory == "그리핀도르":
                scene31()
                scene35()
            if dormitory == "슬리데린":
                scene32()
                scene35()

        if scenenumber == scene and scenenumber == 21:
            scene30()
            root.after(1000)
            if dormitory == "슬리데린":
                scene32()
                scene35()
            if dormitory == "후플푸프":
                scene33()
                scene35()

        if scenenumber == scene and scenenumber == 22:
            scene30()
            root.after(1000)
            if dormitory == "래번클로":
                scene34()
                scene35()
            if dormitory == "슬리데린":
                scene32()
                scene35()

        if scenenumber == scene and scenenumber == 23:
            scene30()
            root.after(1000)
            if dormitory == "그리핀도르":
                scene31()
                scene35()
            if dormitory == "후플푸프":
                scene33()
                scene35()

        if scenenumber == scene and scenenumber == 24:
            scene30()
            root.after(1000)
            if dormitory == "그리핀도르":
                scene31()
                scene35()
            if dormitory == "래번클로":
                scene34()
                scene35()

        if scenenumber == scene and scenenumber == 25:
            scene30()
            root.after(1000)
            if dormitory == "후플푸프":
                scene33()
                scene35()
            if dormitory == "래번클로":
                scene34()
                scene35()

        if scenenumber == scene and scenenumber == 26:
            scene30()
            root.after(1000)
            if dormitory == "래번클로":
                scene34()
                scene35()
            if dormitory == "슬리데린":
                scene32()
                scene35()
            if dormitory == "후플푸프":
                scene33()
                scene35()
            if dormitory == "래번클로":
                scene34()
                scene35()

        if scenenumber == scene and scenenumber == 27:
            scene30()
            root.after(1000)
            if dormitory == "래번클로":
                scene34()
                scene35()
            if dormitory == "슬리데린":
                scene32()
                scene35()
            if dormitory == "후플푸프":
                scene33()
                scene35()
            if dormitory == "래번클로":
                scene34()
                scene35()

        if scenenumber == scene and scenenumber == 28:
            scene30()
            root.after(1000)
            if dormitory == "래번클로":
                scene34()
                scene35()
            if dormitory == "슬리데린":
                scene32()
                scene35()
            if dormitory == "후플푸프":
                scene33()
                scene35()
            if dormitory == "래번클로":
                scene34()
                scene35()

        if scenenumber == scene and scenenumber == 29:
            scene30()
            root.after(1000)
            if dormitory == "래번클로":
                scene34()
                scene35()
            if dormitory == "슬리데린":
                scene32()
                scene35()
            if dormitory == "후플푸프":
                scene33()
                scene35()
            if dormitory == "래번클로":
                scene34()
                scene35()

    clickedXPos = event.x
    clickedYPos = event.y

    # 시작페이지
    if (clickedXPos > 218 and clickedXPos < 421) and (
            clickedYPos > 495 and clickedYPos < 580) and scenenumber == 0 and inputwindow == 0:
        inputname()

    # scene2 선택
    print("---------------------")
    print(str(clickedXPos) + '\t' + str(clickedYPos))
    print("래번클로 : \t" + str(래번클로))
    print("후플푸프 : \t" + str(후플푸프))
    print("그리핀도르 : \t" + str(그리핀도르))
    print("슬리데린 : \t" + str(슬리데린))
    print(scenenumber)
    print(scenenumbercheck)
    # scene2 선택
    if scenenumber == 2:
        print(scenenumber)
        react_click(clickedXPos, clickedYPos, 480, 1140, 490, 535, 2, "래번클로")
        react_click(clickedXPos, clickedYPos, 970, 1550, 580, 630, 2, "후플푸프")
        react_click(clickedXPos, clickedYPos, 480, 1060, 670, 725, 2, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 970, 1500, 780, 830, 2, "슬리데린")

    # scene3 선택
    if scenenumber == 3:
        print(scenenumber)
        react_click(clickedXPos, clickedYPos, 25, 570, 300, 350, 3, "슬리데린")
        react_click(clickedXPos, clickedYPos, 25, 620, 440, 490, 3, "래번클로")
        react_click(clickedXPos, clickedYPos, 25, 430, 580, 630, 3, "후플푸프")
        react_click(clickedXPos, clickedYPos, 25, 230, 720, 770, 3, "그리핀도르")

    # scene4 선택
    if scenenumber == 4:
        react_click(clickedXPos, clickedYPos, 40, 500, 480, 535, 4, "래번클로")
        react_click(clickedXPos, clickedYPos, 40, 375, 740, 790, 4, "슬리데린")
        react_click(clickedXPos, clickedYPos, 40, 375, 995, 1050, 4, "그리핀도르", "후플푸프")

    # scene5 선택
    if scenenumber == 5:
        react_click(clickedXPos, clickedYPos, 705, 1210, 640, 695, 5, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 325, 690, 770, 820, 5, "래번클로")
        react_click(clickedXPos, clickedYPos, 1230, 1680, 770, 820, 5, "후플푸프")
        react_click(clickedXPos, clickedYPos, 588, 1060, 915, 965, 5, "슬리데린")

    # scene6 선택
    if scenenumber == 6:
        react_click(clickedXPos, clickedYPos, 370, 495, 330, 375, 6, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 1450, 1540, 330, 375, 6, "후플푸프")
        react_click(clickedXPos, clickedYPos, 370, 490, 725, 770, 6, "슬리데린")
        react_click(clickedXPos, clickedYPos, 1450, 1540, 725, 770, 6, "래번클로")

    # scene7 선택
    if scenenumber == 7:
        react_click(clickedXPos, clickedYPos, 1420, 1540, 270, 320, 7, "슬리데린")
        react_click(clickedXPos, clickedYPos, 1375, 1590, 390, 440, 7, "후플푸프")
        react_click(clickedXPos, clickedYPos, 1420, 1540, 515, 565, 7, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 1290, 1670, 645, 695, 7, "래번클로")

    # scene8 선택
    if scenenumber == 8:
        react_click(clickedXPos, clickedYPos, 290, 670, 360, 410, 8, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 1175, 1735, 360, 410, 8, "래번클로")
        react_click(clickedXPos, clickedYPos, 275, 685, 730, 780, 8, "후플푸프")
        react_click(clickedXPos, clickedYPos, 1235, 1675, 730, 780, 8, "슬리데린")

    # scene9 선택
    if scenenumber == 9:
        react_click(clickedXPos, clickedYPos, 690, 1260, 345, 390, 9, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 655, 1260, 540, 585, 9, "래번클로")
        react_click(clickedXPos, clickedYPos, 700, 1225, 735, 785, 9, "슬리데린")
        react_click(clickedXPos, clickedYPos, 645, 1285, 925, 980, 9, "후플푸프")

    # scene10 선택
    if scenenumber == 10:
        react_click(clickedXPos, clickedYPos, 1125, 1890, 210, 260, 10, "슬리데린")
        react_click(clickedXPos, clickedYPos, 285, 915, 385, 435, 10, "래번클로")
        react_click(clickedXPos, clickedYPos, 1200, 1885, 645, 695, 10, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 290, 975, 740, 785, 10, "후플푸프")

    # scene11 선택
    if scenenumber == 11:
        react_click(clickedXPos, clickedYPos, 100, 995, 365, 410, 11, "슬리데린")
        react_click(clickedXPos, clickedYPos, 970, 1815, 475, 520, 11, "래번클로")
        react_click(clickedXPos, clickedYPos, 270, 1000, 590, 635, 11, "후플푸프")
        react_click(clickedXPos, clickedYPos, 970, 1870, 740, 785, 11, "그리핀도르")

    # scene12 선택
    if scenenumber == 12:
        react_click(clickedXPos, clickedYPos, 875, 1045, 515, 560, 12, "슬리데린")
        react_click(clickedXPos, clickedYPos, 875, 1045, 630, 680, 12, "래번클로")
        react_click(clickedXPos, clickedYPos, 875, 1045, 750, 800, 12, "후플푸프")
        react_click(clickedXPos, clickedYPos, 835, 1085, 865, 910, 12, "그리핀도르")

    # scene13 선택
    if scenenumber == 13:
        react_click(clickedXPos, clickedYPos, 515, 1380, 290, 335, 13, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 465, 1430, 445, 490, 13, "래번클로")
        react_click(clickedXPos, clickedYPos, 485, 1425, 625, 665, 13, "후플푸프")
        react_click(clickedXPos, clickedYPos, 650, 1270, 740, 785, 13, "슬리데린")

    # scene14 선택
    if scenenumber == 14:
        react_click(clickedXPos, clickedYPos, 195, 510, 382, 685, 14, "래번클로")
        react_click(clickedXPos, clickedYPos, 1345, 1630, 640, 685, 14, "후플푸프")
        react_click(clickedXPos, clickedYPos, 195, 595, 800, 840, 14, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 1290, 1690, 800, 840, 14, "슬리데린")

    # scene15 선택
    if scenenumber == 15:
        react_click(clickedXPos, clickedYPos, 140, 465, 240, 280, 15, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 200, 400, 350, 395, 15, "래번클로")
        react_click(clickedXPos, clickedYPos, 105, 495, 460, 500, 15, "후플푸프")
        react_click(clickedXPos, clickedYPos, 220, 390, 575, 620, 15, "슬리데린")

    # scene16 선택
    if scenenumber == 16:
        react_click(clickedXPos, clickedYPos, 140, 820, 345, 390, 16, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 1145, 1850, 345, 390, 16, "슬리데린")
        react_click(clickedXPos, clickedYPos, 10, 980, 630, 675, 16, "래번클로")
        react_click(clickedXPos, clickedYPos, 1210, 1800, 630, 675, 16, "후플푸프")

    # scene17 선택
    if scenenumber == 17:
        react_click(clickedXPos, clickedYPos, 1150, 1475, 250, 295, 17, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 1440, 1765, 370, 415, 17, "래번클로")
        react_click(clickedXPos, clickedYPos, 1150, 1505, 490, 535, 17, "슬리데린")
        react_click(clickedXPos, clickedYPos, 1445, 1740, 625, 670, 17, "후플푸프")

    # scene18 선택
    if scenenumber == 18:
        react_click(clickedXPos, clickedYPos, 450, 1470, 235, 280, 18, "후플푸프")
        react_click(clickedXPos, clickedYPos, 515, 1410, 445, 490, 18, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 165, 855, 715, 755, 18, "슬리데린")
        react_click(clickedXPos, clickedYPos, 1135, 1850, 715, 755, 18, "래번클로")

    # scene19 선택
    if scenenumber == 19:
        react_click(clickedXPos, clickedYPos, 280, 355, 520, 560, 19, "래번클로", "후플푸프")
        react_click(clickedXPos, clickedYPos, 1560, 1675, 520, 560, 19, "그리핀도르", "슬리데린")

    # scene20 선택
    if scenenumber == 20:
        react_decision(clickedXPos, clickedYPos, 645, 1240, 660, 700, 20, "그리핀도르")
        react_decision(clickedXPos, clickedYPos, 585, 1325, 800, 845, 20, "슬리데린")

    # scene21 선택
    if scenenumber == 21:
        react_click(clickedXPos, clickedYPos, 145, 835, 580, 620, 21, "슬리데린")
        react_click(clickedXPos, clickedYPos, 1085, 1845, 580, 620, 21, "후플푸프")

    # scene22 선택
    if scenenumber == 22:
        react_click(clickedXPos, clickedYPos, 125, 685, 680, 720, 22, "래번클로")
        react_click(clickedXPos, clickedYPos, 1325, 1770, 680, 720, 22, "슬리데린")

    # scene23 선택
    if scenenumber == 23:
        react_click(clickedXPos, clickedYPos, 1200, 1770, 345, 385, 23, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 1350, 1630, 690, 730, 23, "후플푸프")

    # scene24 선택
    if scenenumber == 24:
        react_click(clickedXPos, clickedYPos, 50, 790, 490, 530, 24, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 30, 945, 710, 795, 24, "래번클로")

    # scene25 선택
    if scenenumber == 25:
        react_click(clickedXPos, clickedYPos, 305, 1600, 415, 465, 25, "후플푸프")
        react_click(clickedXPos, clickedYPos, 385, 1555, 650, 690, 25, "래번클로")

    # scene26 선택
    if scenenumber == 26:
        react_click(clickedXPos, clickedYPos, 300, 910, 385, 425, 26, "후플푸프")
        react_click(clickedXPos, clickedYPos, 1160, 1770, 520, 570, 26, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 305, 1115, 660, 700, 26, "래번클로")

    # scene27 선택
    if scenenumber == 27:
        react_click(clickedXPos, clickedYPos, 35, 510, 715, 755, 27, "후플푸프")
        react_click(clickedXPos, clickedYPos, 815, 1090, 715, 755, 27, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 1360, 1675, 715, 755, 27, "슬리데린")

    # scene28 선택
    if scenenumber == 28:
        react_click(clickedXPos, clickedYPos, 145, 430, 345, 385, 28, "후플푸프")
        react_click(clickedXPos, clickedYPos, 145, 430, 525, 565, 28, "래번클로")
        react_click(clickedXPos, clickedYPos, 145, 430, 700, 740, 28, "슬리데린")

    # scene29 선택
    if scenenumber == 29:
        react_click(clickedXPos, clickedYPos, 180, 615, 245, 285, 29, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 70, 715, 400, 440, 29, "래번클로")
        react_click(clickedXPos, clickedYPos, 255, 535, 575, 615, 29, "슬리데린")

    if scenenumber == 31 or scenenumber == 32 or scenenumber == 33 or scenenumber == 34:
        react_click(clickedXPos, clickedYPos, 920, 1000, 980, 1015, 29, "그리핀도르")

    # scene35 선택
    if scenenumber == 35:
        react_click(clickedXPos, clickedYPos, 14, 654, 340, 382, 30, "래번클로")
        react_click(clickedXPos, clickedYPos, 14, 727, 481, 524, 30, "후플푸프")
        react_click(clickedXPos, clickedYPos, 14, 508, 623, 665, 30, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 14, 290, 765, 807, 30, "슬리데린")

    # scene43 선택
    if scenenumber == 43:
        react_click(clickedXPos, clickedYPos, 14, 654, 340, 382, 31, "래번클로")
        react_click(clickedXPos, clickedYPos, 14, 727, 481, 524, 31, "후플푸프")
        react_click(clickedXPos, clickedYPos, 14, 508, 623, 665, 31, "그리핀도르")
        react_click(clickedXPos, clickedYPos, 14, 290, 765, 807, 31, "슬리데린")


def usersign():
    global username
    global inputnameentry
    global subwindow
    global scenenumber
    inputnamevalue = inputnameentry.get()
    username = username + inputnamevalue
    if username != '':
        subwindow.destroy()
        scenenumber = scenenumber + 1
        scene1()


def inputname():
    global username
    global inputnameentry
    global subwindow
    global inputwindow
    inputwindow = 1
    subwindow = Tk()
    subwindow.focus_set()
    canvas1 = Canvas(subwindow, width=400, height=300)
    canvas1.pack()

    label1 = Label(subwindow, text='해리포터 기숙사 배정 시험을 시작합니다', font=('helvetica', 16, 'bold'))
    canvas1.create_window(200, 60, window=label1)

    label2 = Label(subwindow, text='여기에 당신의 이름을 입력해주세요', font=('helvetica', 12))
    canvas1.create_window(200, 130, window=label2)

    inputnameentry = Entry(subwindow)
    canvas1.create_window(200, 160, window=inputnameentry)
    inputnameentry.focus()
    button1 = Button(subwindow, text='시험을 보겠습니다', command=usersign, bg='brown', fg='white',
                     font=('helvetica', 14, 'bold'))
    canvas1.create_window(200, 210, window=button1)


def movetext(textvalue):
    textindex = canvas.create_text(960, 540, text=textvalue, font='맑은고딕 36 bold', fill='white')
    for i in range(60):
        canvas.move(textindex, 0, -3)
        window.update()
        window.after(100)
    canvas.delete(textindex)


def scene1():
    global background_img
    canvas.delete('all')
    canvas.pack(expand=True)
    background_img = PhotoImage(master=canvas, file='scene1.gif')
    bg = canvas.create_image(0, 0, anchor="nw", image=background_img)

    window.update()

    text1 = "호그와트에 입학하신것을 축하드립니다."
    movetext(text1)

    text2 = "지금부터 기숙사 배정을 시작할 예정입니다."
    movetext(text2)

    text3 = "기숙사는 그리핀도르, 레번클로, 슬리데린, 후플푸프 총 4가지가 있습니다."
    movetext(text3)

    text4 = "다음부터 나오는 질문에 대해 솔직하게 대답하여 주세요."
    movetext(text4)

    text5 = "최대한 선지에 나와있는 대답에 충실해 주시기 바랍니다."
    movetext(text5)

    scene2()
    window.mainloop()


def printQuestion(qx, qy, t1x, t1y, t2x, t2y, t3x, t3y, t4x, t4y, question, text1=None, text2=None, text3=None,
                  text4=None):
    global background_img
    global scenenumber
    scenegifname = 'scene' + str(scenenumber) + '.gif'
    canvas.delete('all')
    canvas.pack(expand=True)
    background_img = PhotoImage(master=canvas, file=scenegifname)
    bg = canvas.create_image(0, 0, anchor="nw", image=background_img)

    canvas.create_text(qx, qy, anchor="nw", text=question, font='맑은고딕 24 bold', fill='white')
    canvas.create_text(t1x, t1y, anchor="nw", text=text1, font='맑은고딕 24 bold', fill='white')
    canvas.create_text(t2x, t2y, anchor="nw", text=text2, font='맑은고딕 24 bold', fill='white')
    canvas.create_text(t3x, t3y, anchor="nw", text=text3, font='맑은고딕 24 bold', fill='white')
    canvas.create_text(t4x, t4y, anchor="nw", text=text4, font='맑은고딕 24 bold', fill='white')
    window.update()

    window.mainloop()


def scene2():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q 새학기가 되었다. 당신의 기분은?"
    textAnswer1 = "학교를 가다 길을 잃지 않을까 걱정된다."
    textAnswer2 = "친구들과 잘 지낼 수 있으면 좋겠다"
    textAnswer3 = "뭐든지 열심히 할 준비가 되어있다."
    textAnswer4 = "새로운 관계를 맺기가 피곤하다."

    printQuestion(480, 330, 480, 490, 970, 580, 480, 670, 970, 780, textQuestion, textAnswer1, textAnswer2, textAnswer3,
                  textAnswer4)

    window.update()

    window.mainloop()


def scene3():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q 시험을 볼 때 모르는 문제가 있다면?"
    textAnswer1 = "내가 찍는 답이 정답이 되게 한다"
    textAnswer2 = "논리적으로 그럴듯한 것을 선택한다"
    textAnswer3 = "모르는 문제는 넘어간다"
    textAnswer4 = "그냥 찍는다"

    printQuestion(10, 44, 25, 300, 25, 440, 25, 580, 25, 720, textQuestion, textAnswer1, textAnswer2, textAnswer3,
                  textAnswer4)

    window.update()

    window.mainloop()


def scene4():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q 길을 가다가 맘에 드는 꽃을 본 당신, \n 어떻게 행동할 것인가?"
    textAnswer1 = "꽃의 씨를 사서 집에 심는다"
    textAnswer2 = "꽃을 꺾어 가져간다"
    textAnswer3 = "꽃을 매일 보러 온다"

    printQuestion(50, 105, 40, 480, 40, 740, 40, 995, 0, 0, textQuestion, textAnswer1, textAnswer2, textAnswer3)

    window.update()

    window.mainloop()


def scene5():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q 당신이 적과 맞서는 이유는?"
    textAnswer1 = "내가 할 수 있는 일이기 때문에"
    textAnswer2 = "모두의 이익을 위해서"
    textAnswer3 = "그것이 옳은 일이기 때문에"
    textAnswer4 = "나를 위해서"

    printQuestion(705, 520, 705, 640, 325, 770, 1230, 770, 855, 915, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene6():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q 숲을 지나가던 중 동물을 만난 당신, \n  어떤 동물이었을까?"
    textAnswer1 = "고양이"
    textAnswer2 = "수달"
    textAnswer3 = "거북이"
    textAnswer4 = "참새"

    printQuestion(630, 490, 370, 330, 1450, 330, 370, 725, 1450, 725, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene7():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q 너를 위해"
    textAnswer1 = "죽일게"
    textAnswer2 = "함께 죽을게"
    textAnswer3 = "죽을게"
    textAnswer4 = "아무도 죽지 않게 할게"

    printQuestion(855, 110, 1420, 270, 1375, 390, 1420, 515, 1290, 645, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene8():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q 적과 만난 당신, 어떤 마법을 쓸 것인가?"
    textAnswer1 = "스투페파이 (기절마법)"
    textAnswer2 = "페트리피쿠스토탈루스 (봉인주문)"
    textAnswer3 = "살비오 헥시아(방어마법)"
    textAnswer4 = "아바다케다브라(즉사주문)"

    printQuestion(605, 140, 290, 360, 1175, 360, 275, 730, 1235, 730, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene9():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q. 당신이 가장 좋아하는 시간은?"
    textAnswer1 = "친구들과 함께 바다 여행한 시간"
    textAnswer2 = "자신의 방에서 보내는 혼자만의 시간"
    textAnswer3 = "가족들 옹기종기 모인 식사시간"
    textAnswer4 = "몸이 불편하신 할머니를 도와드리는 시간"

    printQuestion(680, 155, 690, 345, 655, 540, 700, 735, 645, 925, textQuestion, textAnswer1, textAnswer2, textAnswer3,
                  textAnswer4)

    window.update()

    window.mainloop()


def scene10():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q. 교수가 당신에게 어려운 과제를 부탁했다면?"
    textAnswer1 = "교수님에게 잘 보일 수 있다면 일단 하고 본다."
    textAnswer2 = "내 능력 밖인 일이기 때문에 거절한다."
    textAnswer3 = "어려워도 공부해서 어떻게든 해오긴 한다."
    textAnswer4 = "더 잘할 수 있을 것 같은 사람을 추천한다."

    printQuestion(365, 90, 1125, 210, 285, 385, 1200, 645, 290, 740, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene11():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q. 제법 쌀쌀해지는 날씨에 당신은 옷 정리를 하려고 한다. \n  옷장을 열어보니 입지도 않는 옷들이 너저분하게 쌓여있다. \n  당신은?"
    textAnswer1 = "옷장은 깔끔한 게 좋으니까 아깝더라도 버릴 건 버린다."
    textAnswer2 = "언제 또 입게 될 지 모르니 그냥 정리해서 넣어둔다."
    textAnswer3 = "필요할 수 있는 친구나 지인들에게 나눠준다."
    textAnswer4 = "입는 것만 입게 되니, 자주 입을 것 같은 옷만 추려낸다."

    printQuestion(490, 80, 100, 365, 970, 475, 270, 590, 970, 1870, textQuestion, textAnswer1, textAnswer2, textAnswer3,
                  textAnswer4)

    window.update()

    window.mainloop()


# 여기서부터 작업해야함
def scene12():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q. 당신이 호그와트에 입학한 후 가장 배우고 싶은 과목은 무엇인가?"
    textAnswer1 = "약물 수업"
    textAnswer2 = "음악 수업"
    textAnswer3 = "약초 수업"
    textAnswer4 = "변신 마법 수업"

    printQuestion(395, 320, 875, 515, 875, 630, 875, 750, 875, 865, textQuestion, textAnswer1, textAnswer2, textAnswer3,
                  textAnswer4)

    window.update()

    window.mainloop()


def scene13():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q. 당신이 시험 계획을 세운다면?"
    textAnswer1 = "할 수 있는 만큼의 계획만 세워 완수하고자 노력한다."
    textAnswer2 = "계획은 철저하게 세우나 상황에 따라 유동적으로 행동한다."
    textAnswer3 = "평소에 미리 준비하기 때문에 따로 계획을 세우지 않는다."
    textAnswer4 = "시간 단위로 계획을 세운 뒤 완수한다."

    printQuestion(220, 65, 515, 290, 465, 445, 485, 625, 650, 740, textQuestion, textAnswer1, textAnswer2, textAnswer3,
                  textAnswer4)

    window.update()

    window.mainloop()


def scene14():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q. 상대방이 나를 어떻게 바라봤으면 좋겠는가?"
    textAnswer1 = "부러워하면 좋겠다."
    textAnswer2 = "따라하려고 하면 좋겠다."
    textAnswer3 = "높이 평가했으면 좋겠다."
    textAnswer4 = "신뢰하면 좋겠다."

    printQuestion(570, 180, 195, 640, 1345, 640, 195, 800, 1290, 800, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene15():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q. 한 가지 소원을 들어줄 수 있는 지니를 만난다면 어떤 소원을 말할 것인가?"
    textAnswer1 = "원하는 분야의 성취"
    textAnswer2 = "평화로운 삶"
    textAnswer3 = "주변인들의 건강"
    textAnswer4 = "부와 명예"

    printQuestion(140, 85, 140, 240, 200, 350, 105, 460, 220, 575, textQuestion, textAnswer1, textAnswer2, textAnswer3,
                  textAnswer4)

    window.update()

    window.mainloop()


def scene16():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q. 처음 보는 친구에게 다가가는 방법은?"
    textAnswer1 = "친구의 반응 하나하나에 맞서서 반응한다."
    textAnswer2 = "먼저 말을 걸며 그 친구를 이끄는 타입이다."
    textAnswer3 = "이상한 유머를 하거나 질문을 해서 일단 분위기를 풀어준다."
    textAnswer4 = "그 친구가 말을 걸 때까지 기다린다."

    printQuestion(620, 190, 140, 345, 1145, 345, 10, 630, 1210, 630, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene17():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q. 당신이 가장 듣고 싶은 말은?"
    textAnswer1 = "넌 용감한 사람이야"
    textAnswer2 = "넌 똑똑한 사람이야"
    textAnswer3 = "넌 부지런한 사람이야"
    textAnswer4 = "넌 착한 사람이야"

    printQuestion(1190, 105, 1150, 250, 1440, 370, 1150, 490, 1445, 625, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene18():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q. 학교에서 반장들을 뽑는 날이 다가왔다. 반장선거에 대해 당신은 어떤 행동을 취할 것인가?"
    textAnswer1 = " 나가고 싶지만 다른 사람들도 기회를 가질 수 있도록 양보한다."
    textAnswer2 = "안 뽑힐 수도 있지만 자신감을 가지고 선거에 출마한다."
    textAnswer3 = "반장이 될 수 있도록 사람들에게 어필한다."
    textAnswer4 = "누가 나가는지에 따라 결정여부가 달라진다."

    printQuestion(190, 25, 450, 235, 515, 445, 165, 715, 1135, 715, textQuestion, textAnswer1, textAnswer2, textAnswer3,
                  textAnswer4)

    window.update()

    window.mainloop()


def scene19():
    global scenenumber
    scenenumber = scenenumber + 1

    textQuestion = "Q. 정의와 자신감 중 어느 것을 선택할 것인가?"
    textAnswer1 = "정의"
    textAnswer2 = "자신감"

    printQuestion(570, 160, 280, 520, 1560, 520, 0, 0, 0, 0, textQuestion, textAnswer1, textAnswer2)

    window.update()

    window.mainloop()


def scene20():
    global scenenumber
    scenenumber = 20

    textQuestion = "Q. 출입 통제 구역에서 이상한 소리가 들린다. 당신이라면?"
    textAnswer1 = "안으로 들어가서 궁금증을 해결한다."
    textAnswer2 = "나와 관련된 일이 아니므로 신경 쓰지 않는다."

    printQuestion(480, 180, 645, 660, 585, 800, 0, 0, 0, 0, textQuestion, textAnswer1, textAnswer2)

    window.update()

    window.mainloop()


def scene21():
    global scenenumber
    scenenumber = 21

    textQuestion = "Q. 모두가 보는 앞에 나서야 한다면"
    textAnswer1 = "뭔지는 잘 몰라도 자신감을 갖고 나가본다."
    textAnswer2 = "나설 수 없는 이유를 대며 그 상황을 회피한다."

    printQuestion(670, 185, 145, 580, 1085, 580, 0, 0, 0, 0, textQuestion, textAnswer1, textAnswer2)

    window.update()

    window.mainloop()


def scene22():
    global scenenumber
    scenenumber = 22

    textQuestion = "Q 계획을 세울 때"
    textAnswer1 = "다양한 변수를 생각하여 계획한다."
    textAnswer2 = "내가 원하는 바를 추구한다."

    printQuestion(805, 245, 125, 680, 1325, 680, 0, 0, 0, 0, textQuestion, textAnswer1, textAnswer2)

    window.update()

    window.mainloop()


def scene23():
    global scenenumber
    scenenumber = 23

    textQuestion = "Q. 괴롭힘을 당하는 친구가 있다. 당신이라면?"
    textAnswer1 = "발견하는 즉시 나서서 도움을 준다."
    textAnswer2 = "뒤에서 챙겨준다."

    printQuestion(70, 490, 1200, 345, 1350, 690, 0, 0, 0, 0, textQuestion, textAnswer1, textAnswer2)

    window.update()

    window.mainloop()


def scene24():
    global scenenumber
    scenenumber = 24

    textQuestion = "Q. 수업 도중 스네이프 교수가 당신이 잘 아는 것에 대해 공개적으로 질문했다.\n                                                  당신이라면?"
    textAnswer1 = "내가 잘 아는 분야이므로 자신 있게 대답한다."
    textAnswer2 = "잘 알고 있어도 사람이 많으므로 ‘누군가는 대답해주겠지\n 하고 가만히 기다린다."

    printQuestion(50, 85, 50, 490, 50, 710, 0, 0, 0, 0, textQuestion, textAnswer1, textAnswer2)

    window.update()

    window.mainloop()


def scene25():
    global scenenumber
    scenenumber = 25

    textQuestion = "Q. 몇일 째 연락 두절인 연인, 이때 당신의 행동은?"
    textAnswer1 = "무슨 사정이 있을 것이기 때문에 언젠가는 연락이 올 거라고 생각하며 기다린다."
    textAnswer2 = " 어떤 사정이 있는지 수소문 하거나 찾아가는 등 연락할 방법을 모색한다."

    printQuestion(545, 175, 305, 415, 385, 650, 0, 0, 0, 0, textQuestion, textAnswer1, textAnswer2)

    window.update()

    window.mainloop()


def scene26():
    global scenenumber
    scenenumber = 26

    textQuestion = "Q. 당신은 길을 가다가 아는 길과 모르는 길 두 갈래를 발견했다. \n     두 길이 언젠가는 통한다는 것을 아는 당신, \n    당신의 선택은?"
    textAnswer1 = "내가 알고있는 안전한 길을 선택한다."
    textAnswer2 = "모르는 길을 선택하여 모험을 떠난다."
    textAnswer3 = "모르는 길을 선택하여 왔던 길을 표시하면서 간다."

    printQuestion(300, 150, 300, 385, 1160, 520, 305, 660, 0, 0, textQuestion, textAnswer1, textAnswer2, textAnswer3)

    window.update()

    window.mainloop()


def scene27():
    global scenenumber
    scenenumber = 27

    textQuestion = "Q. 당신은 영국에서 이름을 날리는 유명한 사립 탐정 이다.\n    오늘도 어김없이 의뢰가 들어와 새로운 사건을 담당하게 되었다.\n    탐정 활동을 시작해야 하는 당신, 다음 물건 중 활동에 가장 필요한 것은?"
    textAnswer1 = "가발, 안경 등 변장에 필요한 도구"
    textAnswer2 = "수첩과 필기도구"
    textAnswer3 = "목숨을 지켜줄 권총"

    printQuestion(35, 885, 35, 715, 815, 715, 1360, 715, 0, 0, textQuestion, textAnswer1, textAnswer2, textAnswer3)

    window.update()

    window.mainloop()


def scene28():
    global scenenumber
    scenenumber = 28

    textQuestion = "Q. 하루 일과를 마치고 집으로 돌아온 당신. 갑자기 집에 놓인 말을 하기 시작합니다. \n    이 인형은 당신에게 뭐라고 말했을까요?"
    textAnswer1 = "여기가 어디에요?"
    textAnswer2 = "나는 누구인가요?"
    textAnswer3 = "당신은 누구세요?"

    printQuestion(70, 120, 145, 345, 430, 525, 700, 740, 0, 0, textQuestion, textAnswer1, textAnswer2, textAnswer3)

    window.update()

    window.mainloop()


def scene29():
    global scenenumber
    scenenumber = 29

    textQuestion = "Q. 오랫동안 함께해온 당신의 물건이 망가져 버렸다. 이후 당신의 행동은?"
    textAnswer1 = "내가 고치려고 시도해본다."
    textAnswer2 = "물건을 고칠 수 있도록 도움을 요청한다."
    textAnswer3 = "그대로 보관한다."

    printQuestion(35, 35, 180, 615, 70, 400, 255, 535, 0, 0, textQuestion, textAnswer1, textAnswer2, textAnswer3)

    window.update()

    window.mainloop()


def scene30():
    global scenenumber
    scenenumber = 30

    textQuestion = "so difficult....."

    printQuestion(872, 212, 0, 0, 0, 0, 0, 0, 0, 0, textQuestion)

    window.update()

    window.mainloop()


def printdormitory(qx, qy, t1x, t1y, t2x, t2y, t3x, t3y, t4x, t4y, t5x, t5y, t6x, t6y, t7x, t7y, t8x, t8y, question,
                   text1=None, text2=None, text3=None, text4=None, text5=None, text6=None, text7=None, text8=None,
                   font_color=None):
    global background_img
    global scenenumber
    scenegifname = 'scene' + str(scenenumber) + '.gif'
    canvas.delete('all')
    canvas.pack(expand=True)
    background_img = PhotoImage(master=canvas, file=scenegifname)
    bg = canvas.create_image(0, 0, anchor="nw", image=background_img)

    canvas.create_text(qx, qy, anchor="nw", text=question, font='맑은고딕 24 bold', fill='white')
    canvas.create_text(t1x, t1y, anchor="nw", text=text1, font='맑은고딕 24 bold', fill=font_color)
    canvas.create_text(t2x, t2y, anchor="nw", text=text2, font='맑은고딕 24 bold', fill='white')
    canvas.create_text(t3x, t3y, anchor="nw", text=text3, font='맑은고딕 24 bold', fill='white')
    canvas.create_text(t4x, t4y, anchor="nw", text=text4, font='맑은고딕 24 bold', fill='white')
    canvas.create_text(t5x, t5y, anchor="nw", text=text5, font='맑은고딕 24 bold', fill='white')
    canvas.create_text(t6x, t6y, anchor="nw", text=text6, font='맑은고딕 24 bold', fill='white')
    canvas.create_text(t7x, t7y, anchor="nw", text=text7, font='맑은고딕 24 bold', fill='white')
    canvas.create_text(t8x, t8y, anchor="nw", text=text8, font='맑은고딕 24 bold', fill='white')

    window.update()

    window.mainloop()


def scene31():
    global scenenumber
    scenenumber = 31

    textQuestion = "축하드립니다." + username
    textAnswer1 = "당신의 기숙사는 그리핀도르 입니다."
    textAnswer2 = "그리핀도르는 용감하고 대담한 자들을 위한 기숙사 입니다."
    textAnswer3 = "당신의 특기인 그 용기를 올바른 곳에 사용하길 바랍니다."
    textAnswer4 = "기숙사는 동쪽 탑 7층 복도 끝에 있으며, 공지되는 암호를 꼭 기억하여 \n 휴게실에 들어갈 수 있도록 해주세요."
    textAnswer5 = '그리핀도르 기숙사 사감은 미네르바 맥고나걸, 변신술 교수입니다.'
    textAnswer6 = '그리핀도르는 해리 포터, 헤르미온느 그레인저, 론 위즐리, 알버스 덤블도어가 소속된 곳이기도 합니다.'
    textAnswer7 = '당신이 만족스런 학교생활을 하길 바랍니다. 다시 한번 호그와트에 입학하신 것을 환영합니다.'
    textAnswer8 = 'END'
    printdormitory(780, 65, 650, 160, 485, 270, 495, 380, 390, 495, 420, 650, 130, 765, 195, 880, 920, 980,
                   textQuestion, textAnswer1, textAnswer2, textAnswer3, textAnswer4, textAnswer5, textAnswer6,
                   textAnswer7, textAnswer8, 'red')

    window.update()

    window.mainloop()


def scene32():
    global scenenumber
    scenenumber = 32

    textQuestion = "축하드립니다." + username
    textAnswer1 = "당신의 기숙사는 슬리데린 입니다."
    textAnswer2 = "슬리데린은 야망있는 재간꾼들을 위한 기숙사입니다."
    textAnswer3 = "당신의 야망을 이루기 위한 올바른 노력을 기울이기 바랍니다. "
    textAnswer4 = "기숙사는 지하 감옥 옆에 있으며, 공지되는 암호를 꼭 기억하여 \n 휴게실에 들어갈 수 있도록 해주세요. "
    textAnswer5 = '슬리데린 기숙사 사감은 세베루스 스네이프, 약물 교수입니다.'
    textAnswer6 = '슬리데린은 호레이스 슬러그혼, 세베루스 스네이프, 레타 레스트랭이 소속된 곳이기도 합니다.'
    textAnswer7 = '당신이 만족스런 학교생활을 하길 바랍니다. 다시 한번 호그와트에 입학하신 것을 환영합니다.'
    textAnswer8 = 'END'

    printdormitory(780, 65, 650, 160, 535, 270, 455, 390, 445, 505, 460, 665, 200, 775, 195, 880, 920, 980,
                   textQuestion, textAnswer1, textAnswer2, textAnswer3, textAnswer4, textAnswer5, textAnswer6,
                   textAnswer7, textAnswer8, 'green')

    window.update()

    window.mainloop()


def scene33():
    global scenenumber
    scenenumber = 33

    textQuestion = "축하드립니다." + username
    textAnswer1 = "당신의 기숙사는 후플푸프입니다."
    textAnswer2 = "후플푸프는 정의롭고 진실된 자를 위한 기숙사 입니다."
    textAnswer3 = "당신의 올곧음으로 정의와 진실을 추구하세요."
    textAnswer4 = "기숙사는 후플푸프 지하실에 있으며, 공지되는 암호를 꼭 기억하여 \n휴게실에 들어갈 수 있도록 해주세요."
    textAnswer5 = '후플푸프 기숙사 사감은 포모나 스프라우트, 약초학 교수입니다.'
    textAnswer6 = '후플푸프는 케드릭 디고리, 뉴트 스캐맨더, 님파도라 통스가 소속된 곳이기도 합니다.'
    textAnswer7 = '당신이 만족스런 학교생활을 하길 바랍니다. 다시 한번 호그와트에 입학하신 것을 환영합니다.'
    textAnswer8 = 'END'

    printdormitory(780, 65, 650, 160, 495, 270, 590, 385, 385, 505, 445, 655, 280, 770, 195, 880, 920, 980,
                   textQuestion, textAnswer1, textAnswer2, textAnswer3, textAnswer4, textAnswer5, textAnswer6,
                   textAnswer7, textAnswer8, 'yellow')

    window.update()

    window.mainloop()


def scene34():
    global scenenumber
    scenenumber = 34

    textQuestion = "축하드립니다." + username + '님'
    textAnswer1 = "당신의 기숙사는 래번클로 입니다"
    textAnswer2 = "레번클로는 현명하고 사려깊은 자들을 위한 기숙사 입니다."
    textAnswer3 = "당신의 재치와 지식으로 현명함을 보여주세요."
    textAnswer4 = "기숙사는 청동 독수리상 안에 있으며, 당신의 재치와 지혜라면 \n휴게실에 들어갈 수 있습니다."
    textAnswer5 = '래번클로 기숙사 사감은 필리우스 플리트윅, 주문학 교수입니다.'
    textAnswer6 = '래번클로는 게릭 올리벤더, 루나 러브굿, 질데로이 록허트가 소속된 곳이기도 합니다.'
    textAnswer7 = '당신이 만족스런 학교생활을 하길 바랍니다. 다시 한번 호그와트에 입학하신 것을 환영합니다.'
    textAnswer8 = 'END'

    printdormitory(780, 65, 650, 160, 490, 270, 585, 390, 450, 495, 445, 650, 280, 765, 195, 880, 920, 980,
                   textQuestion, textAnswer1, textAnswer2, textAnswer3, textAnswer4, textAnswer5, textAnswer6,
                   textAnswer7, textAnswer8, 'blue')

    window.update()

    window.mainloop()


def scene35():
    global scenenumber
    scenenumber = 35

    textQuestion = "마지막화면"
    textAnswer1 = "ㅁㅁㅁㅁㅁ"
    textAnswer2 = "ㅁㅁㅁㅁ"
    textAnswer3 = "ㅁㅁㅁㅁㅁ"
    textAnswer4 = "ㅁㅁㅁㅁㅁ"

    printQuestion(872, 212, 1454, 382, 1396, 467, 1454, 552, 1265, 637, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene36():
    global scenenumber
    scenenumber = 36

    textQuestion = "편지를 배달해주는 부엉이"
    textAnswer1 = "ㅁㅁㅁㅁㅁ"
    textAnswer2 = "ㅁㅁㅁㅁ"
    textAnswer3 = "ㅁㅁㅁㅁㅁ"
    textAnswer4 = "ㅁㅁㅁㅁㅁ"

    printQuestion(872, 212, 1454, 382, 1396, 467, 1454, 552, 1265, 637, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene37():
    global scenenumber
    scenenumber = 37

    textQuestion = "골든 스니치"
    textAnswer1 = "ㅁㅁㅁㅁㅁ"
    textAnswer2 = "ㅁㅁㅁㅁ"
    textAnswer3 = "ㅁㅁㅁㅁㅁ"
    textAnswer4 = "ㅁㅁㅁㅁㅁ"

    printQuestion(872, 212, 1454, 382, 1396, 467, 1454, 552, 1265, 637, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene38():
    global scenenumber
    scenenumber = 38

    textQuestion = "마법 지팡이"
    textAnswer1 = "ㅁㅁㅁㅁㅁ"
    textAnswer2 = "ㅁㅁㅁㅁ"
    textAnswer3 = "ㅁㅁㅁㅁㅁ"
    textAnswer4 = "ㅁㅁㅁㅁㅁ"

    printQuestion(872, 212, 1454, 382, 1396, 467, 1454, 552, 1265, 637, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene39():
    global scenenumber
    scenenumber = 39

    textQuestion = "그리핀도르의 검"
    textAnswer1 = "ㅁㅁㅁㅁㅁ"
    textAnswer2 = "ㅁㅁㅁㅁ"
    textAnswer3 = "ㅁㅁㅁㅁㅁ"
    textAnswer4 = "ㅁㅁㅁㅁㅁ"

    printQuestion(872, 212, 1454, 382, 1396, 467, 1454, 552, 1265, 637, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene40():
    global scenenumber
    scenenumber = 40

    textQuestion = "투명망토"
    textAnswer1 = "ㅁㅁㅁㅁㅁ"
    textAnswer2 = "ㅁㅁㅁㅁ"
    textAnswer3 = "ㅁㅁㅁㅁㅁ"
    textAnswer4 = "ㅁㅁㅁㅁㅁ"

    printQuestion(872, 212, 1454, 382, 1396, 467, 1454, 552, 1265, 637, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene41():
    global scenenumber
    scenenumber = 41

    textQuestion = "개구리 초콜렛"
    textAnswer1 = "ㅁㅁㅁㅁㅁ"
    textAnswer2 = "ㅁㅁㅁㅁ"
    textAnswer3 = "ㅁㅁㅁㅁㅁ"
    textAnswer4 = "ㅁㅁㅁㅁㅁ"

    printQuestion(872, 212, 1454, 382, 1396, 467, 1454, 552, 1265, 637, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene42():
    global scenenumber
    scenenumber = 42

    textQuestion = "타임터너"
    textAnswer1 = "ㅁㅁㅁㅁㅁ"
    textAnswer2 = "ㅁㅁㅁㅁ"
    textAnswer3 = "ㅁㅁㅁㅁㅁ"
    textAnswer4 = "ㅁㅁㅁㅁㅁ"

    printQuestion(872, 212, 1454, 382, 1396, 467, 1454, 552, 1265, 637, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene43():
    global scenenumber
    scenenumber = 43

    textQuestion = "사진합성선택"
    textAnswer1 = "ㅁㅁㅁㅁㅁ"
    textAnswer2 = "ㅁㅁㅁㅁ"
    textAnswer3 = "ㅁㅁㅁㅁㅁ"
    textAnswer4 = "ㅁㅁㅁㅁㅁ"

    printQuestion(872, 212, 1454, 382, 1396, 467, 1454, 552, 1265, 637, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def scene44():
    global scenenumber
    scenenumber = 44

    textQuestion = "사진합성결과"
    textAnswer1 = "ㅁㅁㅁㅁㅁ"
    textAnswer2 = "ㅁㅁㅁㅁ"
    textAnswer3 = "ㅁㅁㅁㅁㅁ"
    textAnswer4 = "ㅁㅁㅁㅁㅁ"

    printQuestion(872, 212, 1454, 382, 1396, 467, 1454, 552, 1265, 637, textQuestion, textAnswer1, textAnswer2,
                  textAnswer3, textAnswer4)

    window.update()

    window.mainloop()


def exittest():
    pygame.mixer.music.stop()
    print('종료됨')


from tkinter import *
import pygame
import atexit

if __name__ == "__main__":
    # pygame.mixer.init()
    # pygame.mixer.music.load("Harry 배경음악.mp3")
    # pygame.mixer.music.play(-1)
    atexit.register(exittest)

    window = Tk()
    window.geometry("1920x1080")

    new_width = 1920
    new_height = 1080
    canvas = Canvas(window, width=new_width, height=new_height)  # 캔버스 크기 설정
    canvas.pack()
    canvas.bind("<Button-1>", mouseclick)

    background_img = PhotoImage(master=canvas, file='main.gif')

    canvas.create_image(0, 0, anchor="nw", image=background_img, tags='bg')
    img = PhotoImage(file="start1.png")
    image = canvas.create_image(218, 495, anchor=NW, image=img)

    scenenumber = 0
    scenenumbercheck = 2
    inputwindow = 0
    username = ''
    그리핀도르 = 0
    슬리데린 = 0
    후플푸프 = 0
    래번클로 = 0

    window.mainloop()
