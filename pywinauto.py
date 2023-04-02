#*************************This the whole code will open the notepad and Write some text then close it without saving it***************

from pywinauto.application import Application

#phle app ko open krke v connect kr skte hain yaa open aur connect ek saath c kr skte hain
# app = Application(backend='uia').start('notepad.exe')
# app = Application(backend='uia').connect(title='Untitled - Notepad',timeout=5) #actually this timeout giving 5seconde to the application to start

app = Application(backend='uia').start('notepad.exe').connect(title='Untitled - Notepad',timeout=5)
# app.UntitledNotepad.print_control_identifiers()

#accessing textarea and writing on it
textEditor = app.UntitledNotepad.child_window(title="Text Editor", auto_id="15", control_type="Edit").wrapper_object()
textEditor.type_keys("My name is Prince Karn",with_spaces=True)

#accessing file menu
fileMenu = app.UntitledNotepad.child_window(title="File", control_type="MenuItem").wrapper_object()
fileMenu.click_input()
# app.UntitledNotepad.print_control_identifiers() #this line will print control_identifier with this window whicb is currently opened window
# newWindow = app.UntitledNotepad.child_window(title="New Window	Ctrl+Shift+N", auto_id="8", control_type="MenuItem")
# newWindow.click_input()
close = app.UntitledNotepad.child_window(title="Close", control_type="Button").wrapper_object()
close.click_input()
# app.UntitledNotepad.print_control_identifiers()
dontSave = app.UntitledNotepad.child_window(title="Don't Save", auto_id="CommandButton_7", control_type="Button").wrapper_object()
dontSave.click()


