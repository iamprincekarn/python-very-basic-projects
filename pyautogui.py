import pyautogui as pg

# #basic
# pos = pg.position()
# print(pos);
#
# sz = pg.size()
# print(sz)
#
# presence_of_point = pg.onScreen(1300,1079)
# print(presence_of_point)



# #pause
# pg.PAUSE = 5
# pg.moveTo(100,200) #for cursor movement automatically
# pg.PAUSE = 5
# pg.moveTo(1000,1000)



# #failsafes (works with moveTo)
# #agr hm kvi top left me apne cursor ko le jaye toh wo apne aap program ko abort kr deta hai, failsafes trigger ho jata simply
# #if we want to disable the failsafe like agr hm chahte ki top left corner pe jane se hmare program abort naa ho toh
# pg.FAILSAFE = False #do this
# pg.PAUSE = 5
# pg.moveTo(100,100)
# pg.PAUSE = 5
# pg.moveTo(1000,1000)

# #constantly printing the position of cursor
# for i in range(5):
#     x,y = pg.position()
#     print(f"X:{x} , Y:{y}")
#     pg.sleep(2)




# #mouse movement  (move and moveTo)
# pg.sleep(2)
# pg.move(-100,0) #current position se relatively move krta
# pg.sleep(2)
# pg.moveTo(0,10) # ye bs uss co-ordinte pr cursor ko le jata irrespective of the current position of cursor




# #Easing function
# #start slow ending fast
# pg.moveTo(100,100,5,pg.easeInQuad) #5 is used to change the position of cursor smoothly in 5second
#
# #start fast end slow
# pg.moveTo(700,500,2,pg.easeOutQuad)
#
# #bs aise hi something difference ke sath hai sare--->>>
# pg.moveTo(10,30,5,pg.easeOutQuad)
# pg.moveTo(600,700,5,pg.easeInBounce)
# pg.moveTo(10,20,5,pg.easeInElastic)



# # drag and dragTo
# # it also move the cursor but with hold clicking the left mouse button
# pg.sleep(4)
# pg.drag(300,0)
# pg.dragTo(700,560)

#by deafult ye left ko hi click krke rkhta hai leking manually hm ise change kr skte hain
# pg.sleep(4)
# pg.drag(400,340, button='right')



# #make a program to change the position of the taskbar shortcuts
# pg.sleep(3)
# # print(pg.position())
# # pg.sleep(3)
# # print(pg.position())
# pg.sleep(1)
# pg.moveTo(835, 1079)
# pg.mouseDown()
# pg.moveTo(760, 1074, 1, pg.easeInQuad)
# pg.mouseUp()



# # make a program to open a software from taskbar
# pg.sleep(3)
# print(pg.position())
# pg.moveTo(683,1067)
# pg.mouseDown()
# pg.mouseUp()



# #mouse click
# pg.sleep(3)
# pg.click() #by default left click krta hai
# pg.sleep(3)
# pg.doubleClick()

# #open file then open this pc
# pg.sleep(3)
# pg.click()
# pg.sleep(3)
# pg.doubleClick(x=312, y=221, button='left')

# #these are multiple types of clicks
# pg.rightClick()
# pg.leftClick();



# #mouse function
# pg.sleep(3)
# pg.mouseDown()
# pg.mouseUp()






