import tkinter
import tkinter.filedialog
import tkinter.ttk as TTK
import auto_ascii_multiple as ascii_multiple
import auto_ascii_single as ascii_single
import auto_ui_logs as ui_single
import auto_testtime as mainTT

def BrowsePathDatalog():
	pathname = tkinter.filedialog.askdirectory()
	folder_path.set(pathname)

def BrowseFileDatalog():
	filename = tkinter.filedialog.askopenfilename()
	file_path.set(filename)

def ParseDatalog():
	ascii_multiple.parsing(pathEntryASCII.get(),contEntry.get(), outputtextASCII)

def ParseDatalogSingle():
	ascii_single.parsing(pathEntryASCII.get(), outputtextASCII)
	
def ParseUIDatalogSingle():
	ui_single.parsing(pathEntryUI.get(), outputtextUI)
	
def BrowsePathTestTime():
	filespath = tkinter.filedialog.askopenfilenames()
	for path in filespath:
		filepath = path + "\n"
		pathEntryTT.insert(tkinter.END, filepath)


def ParseTestTime():
	pathfilesStr = pathEntryTT.get('1.0', tkinter.END)
	mainTT.converttoexcel(pathfilesStr, outputtextTT)

#FOR ASCII DATALOG PARSER
def ASCIIParserWin():
	#Create window
	asciiwindow = tkinter.Toplevel(mainwindow)
	asciiwindow.title("ASCII Log Parser")
	asciiwindow.geometry("600x700")
	
	bckgcolor = "#FFFFFF"
	asciiwindow.configure(bg=bckgcolor)

	DataToolsFrame = tkinter.Frame(asciiwindow, bg="#FFFFFF")
	DataToolsFrame.grid(columnspan = 2)
	DataToolsLabel = tkinter.Label(DataToolsFrame, text = "DATA TOOLS", font =("DM Sans", 40), bg="#FFFFFF").pack(ipady = 49, ipadx = 128)
	
	#Welcome Label in Main window
	titleASCIIframe = tkinter.Frame(asciiwindow)
	titleASCIIframe.grid(columnspan = 2)
	tkinter.Label(titleASCIIframe, text = "ASCII Log Parser", font=("DM Sans",30), fg="#678596", bg="#FFFFFF").pack()
	
	SpaceBet1 = tkinter.Frame(asciiwindow, height = 50, width = 337, bg="#FFFFFF")
	SpaceBet1.grid()
	
	global folder_path
	global file_path
	global outputtextASCII
	global pathEntryASCII
	global CheckVar1
	global CheckVar2
	
	if ((CheckVar2.get() == 1) and (CheckVar1.get() == 0)):
		#Create path frame and label
		tkinter.Label(asciiwindow, text = "Enter text file path", font=("DM Sans",12), bg="#FFFFFF").grid(column=0, row=20, sticky = "w", padx = 50)
		
		SpaceBet2 = tkinter.Frame(asciiwindow, height = 50, width = 337, bg="#FFFFFF")
		SpaceBet2.grid()
		
		#Create path frame and entry and button for path
		folder_path = tkinter.StringVar()
		pathEntryASCII = tkinter.Entry(asciiwindow, font=("DM Sans",10), bg = "#E5E5E5", width = 70, textvariable = folder_path)
		pathEntryASCII.grid(column=0, columnspan = 2, row=21, sticky = "w", padx = 50)
		pathBt = tkinter.Button(asciiwindow, text="...", font=("DM Sans",10), bg = "#E5E5E5", command = BrowsePathDatalog)
		pathBt.grid(column=1, columnspan = 2, row=21, sticky = "w",)
		
		#Create controller frame and label
		tkinter.Label(asciiwindow, text = "Enter the number of controllers you want to parse", font=("DM Sans",12), bg="#FFFFFF").grid(column=0, row=22, sticky = "w", padx = 50)
	
		#Create input frame and controller entry 
		global contEntry
		contEntry = tkinter.Entry(asciiwindow, font=("DM Sans",10), width = 70, bg = "#E5E5E5")
		contEntry.grid(column=0, columnspan = 2, row=23, sticky = "w", padx = 50)

		#Create parse frame and button
		parseframe = tkinter.Frame(asciiwindow, width = 1, height = 1, bg="#FFFFFF")
		parseframe.grid(columnspan=2, row = 24)
		parseBt = tkinter.Button(parseframe, text = "PARSE DATA", font = ("DM Sans", 15), width = 20, height = 1, bg = '#678596', fg = 'white', command = ParseDatalog)
		parseBt.pack(pady = 10, padx =128)
		
		#Create text widget for output
		outputLabel = tkinter.Label(asciiwindow, text = "Output", font=("DM Sans", 10), fg="#F30D0D", bg="#FFFFFF").grid(sticky = "w", padx=50)
		outputframe = tkinter.Frame(asciiwindow, width = 1, height = 1)
		outputframe.grid(columnspan = 2)
		
		outputtextASCII = tkinter.Text(outputframe, font = ('DM Sans', '10'), bg = "#E5E5E5", width = 70, height = 7)
		outputtextASCII.pack()
		
	elif ((CheckVar1.get() == 1) and (CheckVar2.get() == 0)):
		#Create path frame and label
		tkinter.Label(asciiwindow, text = "Enter text file", font=("DM Sans",12), bg="#FFFFFF").grid(column=0, row=20, sticky = "w", padx = 50)
		
		SpaceBet2 = tkinter.Frame(asciiwindow, height = 50, width = 337, bg="#FFFFFF")
		SpaceBet2.grid()
		
		#Create path frame and entry and button for path
		file_path = tkinter.StringVar()
		pathEntryASCII = tkinter.Entry(asciiwindow, font=("DM Sans",10), bg = "#E5E5E5", width = 60, textvariable = file_path)
		pathEntryASCII.grid(column=0, columnspan = 2, row=21, sticky = "w", padx = 50)
		pathBt = tkinter.Button(asciiwindow, text="...", font=("DM Sans",10), bg = "#E5E5E5", command = BrowseFileDatalog)
		pathBt.grid(column=1, columnspan = 2, row=21, sticky = "w", padx = 5)
	
		#Create parse frame and button
		parseframe = tkinter.Frame(asciiwindow, width = 1, height = 1, bg="#FFFFFF")
		parseframe.grid(columnspan=2, row = 24)
		parseBt = tkinter.Button(parseframe, text = "PARSE DATA", font = ("DM Sans", 15), width = 20, height = 1, bg = '#678596', fg = 'white', command = ParseDatalogSingle)
		parseBt.pack(pady = 10, padx =128)
		
		#Create text widget for output
		outputLabel = tkinter.Label(asciiwindow, text = "Output", font=("DM Sans", 10), fg="#F30D0D", bg="#FFFFFF").grid(sticky = "w", padx=50)
		outputframe = tkinter.Frame(asciiwindow, width = 1, height = 1)
		outputframe.grid(columnspan = 2)
		outputtextASCII = tkinter.Text(outputframe, font = ('DM Sans', '10'), bg = "#E5E5E5", width = 70, height = 7)
		outputtextASCII.pack()
	
		
	
	AuthorFrame = tkinter.Frame(asciiwindow, height = 80, width = 337, bg="#FFFFFF")
	AuthorFrame.grid(columnspan = 2)
	AuthorLabel = tkinter.Label(AuthorFrame, text = "by Sittie Montud", font =("DM Sans", 10), bg="#FFFFFF", fg="#000000").pack(ipady = 49, ipadx = 128)

	asciiwindow.mainloop()


#FOR TEST TIME TO EXCEL
def TestTimeWin():
	#Create window
	ttwindow = tkinter.Toplevel(mainwindow)
	ttwindow.title("J800 Test Time to Excel")
	ttwindow.geometry("600x700")
	bckgcolor = "#FFFFFF"
	ttwindow.configure(bg=bckgcolor)

	DataToolsFrame = tkinter.Frame(ttwindow, bg="#FFFFFF")
	DataToolsFrame.grid(columnspan = 2)
	DataToolsLabel = tkinter.Label(DataToolsFrame, text = "DATA TOOLS", font =("DM Sans", 40), bg="#FFFFFF").pack(ipady = 49, ipadx = 128)
	
	#Welcome Label in Main window
	TestTimeFrame = tkinter.Frame(ttwindow, bg="#FFFFFF")
	TestTimeFrame.grid(columnspan = 2)
	tkinter.Label(TestTimeFrame, text = "Test Time", font=("DMS Sans",30), fg="#678596", bg="#FFFFFF").pack()
	
	SpaceBet1 = tkinter.Frame(ttwindow, height = 50, width = 337, bg="#FFFFFF")
	SpaceBet1.grid()
	
	#Create path frame and label
	tkinter.Label(ttwindow, text = "Select files", font=("DMS Sans", 12), bg="#FFFFFF", fg="#000000").grid(column=0, row=20, sticky = "w", padx = 50)
	
	#Create path frame and text and button for path
	filespath = ()
	global pathEntryTT
	pathEntryTT = tkinter.Text(ttwindow, font = ('DM Sans', '8'), width = 70, height=5, bg = "#E5E5E5")
	pathEntryTT.grid(column = 0, columnspan=2, row=21, padx = 50, sticky = "w")
	pathBtTT = tkinter.Button(ttwindow, text="...", font = ('DM Sans', '28'), bg = "#E5E5E5", command = BrowsePathTestTime)
	pathBtTT.grid(column = 1, columnspan = 3, row=21, sticky = "w", padx = 8)
	
	##Create parse frame and button
	parseframeTT = tkinter.Frame(ttwindow, width = 100, height = 50, bg="#FFFFFF")
	parseframeTT.grid(columnspan = 2)
	parseBtTT = tkinter.Button(parseframeTT, text = "PARSE", font = ("DM Sans", 15), width = 20, height = 1,bg = '#678596', fg = 'white', command = ParseTestTime)
	parseBtTT.pack(pady = 10, padx = 128)
	
	##Create text widget for output
	outputLabel = tkinter.Label(ttwindow, text = "Output", font=("DM Sans", 10), fg="#F30D0D", bg="#FFFFFF").grid(sticky = "w", padx=50)
	outputframe = tkinter.Frame(ttwindow, width = 1, height = 1)
	outputframe.grid(column =0, columnspan = 2)
	global outputtextTT
	outputtextTT = tkinter.Text(outputframe, font = ('DM Sans', '10'), bg = "#E5E5E5",width = 70, height = 7)
	outputtextTT.pack()
	
	AuthorFrame = tkinter.Frame(ttwindow, height = 80, width = 337, bg="#FFFFFF")
	AuthorFrame.grid(columnspan = 2)
	AuthorLabel = tkinter.Label(AuthorFrame, text = "by Sittie Montud", font =("DM Sans", 10), bg="#FFFFFF", fg="#000000").pack(ipady = 49, ipadx = 128)
	
	ttwindow.mainloop()

#FOR UI DATALOG PARSER
def UIParserWin():
	#Create window
	uiwindow = tkinter.Toplevel(mainwindow)
	uiwindow.title("UI Log Parser")
	uiwindow.geometry("600x700")
	
	bckgcolor = "#FFFFFF"
	uiwindow.configure(bg=bckgcolor)

	DataToolsFrame = tkinter.Frame(uiwindow, bg="#FFFFFF")
	DataToolsFrame.grid(columnspan = 2)
	DataToolsLabel = tkinter.Label(DataToolsFrame, text = "DATA TOOLS", font =("DM Sans", 40), bg="#FFFFFF").pack(ipady = 49, ipadx = 128)
	
	#Welcome Label in Main window
	titleUIframe = tkinter.Frame(uiwindow)
	titleUIframe.grid(columnspan = 2)
	tkinter.Label(titleUIframe, text = "UI Log Parser", font=("DM Sans",30), fg="#678596", bg="#FFFFFF").pack()
	
	SpaceBet1 = tkinter.Frame(uiwindow, height = 50, width = 337, bg="#FFFFFF")
	SpaceBet1.grid()
	
	global folder_path
	global file_path
	global outputtextUI
	global pathEntryUI

	
	#Create path frame and label
	tkinter.Label(uiwindow, text = "Enter text file", font=("DM Sans",12), bg="#FFFFFF").grid(column=0, row=20, sticky = "w", padx = 50)
	
	SpaceBet2 = tkinter.Frame(uiwindow, height = 50, width = 337, bg="#FFFFFF")
	SpaceBet2.grid()
	
	#Create path frame and entry and button for path
	file_path = tkinter.StringVar()
	pathEntryUI = tkinter.Entry(uiwindow, font=("DM Sans",10), bg = "#E5E5E5", width = 60, textvariable = file_path)
	pathEntryUI.grid(column=0, columnspan = 2, row=21, sticky = "w", padx = 50)
	pathBt = tkinter.Button(uiwindow, text="...", font=("DM Sans",10), bg = "#E5E5E5", command = BrowseFileDatalog)
	pathBt.grid(column=1, columnspan = 2, row=21, sticky = "w", padx = 5)
	
	#Create parse frame and button
	parseframe = tkinter.Frame(uiwindow, width = 1, height = 1, bg="#FFFFFF")
	parseframe.grid(columnspan=2, row = 24)
	parseBt = tkinter.Button(parseframe, text = "PARSE DATA", font = ("DM Sans", 15), width = 20, height = 1, bg = '#678596', fg = 'white', command = ParseUIDatalogSingle)
	parseBt.pack(pady = 10, padx =128)
	
	#Create text widget for output
	outputLabel = tkinter.Label(uiwindow, text = "Output", font=("DM Sans", 10), fg="#F30D0D", bg="#FFFFFF").grid(sticky = "w", padx=50)
	outputframe = tkinter.Frame(uiwindow, width = 1, height = 1)
	outputframe.grid(columnspan = 2)
	outputtextUI = tkinter.Text(outputframe, font = ('DM Sans', '10'), bg = "#E5E5E5", width = 70, height = 7)
	outputtextUI.pack()
	
		
	
	AuthorFrame = tkinter.Frame(uiwindow, height = 80, width = 337, bg="#FFFFFF")
	AuthorFrame.grid(columnspan = 2)
	AuthorLabel = tkinter.Label(AuthorFrame, text = "by Sittie Montud", font =("DM Sans", 10), bg="#FFFFFF", fg="#000000").pack(ipady = 49, ipadx = 128)

	uiwindow.mainloop()


#MAIN WINDOW
#Reference to mainwindow
mainwindow = tkinter.Tk()

#Rename the title of the window
mainwindow.title("Data Tools")

#set window size
mainwindow.geometry("600x700")
bckgcolor = "#FFFFFF"
mainwindow.configure(bg=bckgcolor)

DataToolsFrame = tkinter.Frame(mainwindow, bg="#FFFFFF")
DataToolsFrame.grid()
DataToolsLabel = tkinter.Label(DataToolsFrame, text = "DATA TOOLS", font =("DM Sans", 40), bg="#FFFFFF").pack(ipady = 49, ipadx = 128)

SpaceBet3 = tkinter.Frame(mainwindow, height = 30, width = 337, bg="#FFFFFF")
SpaceBet3.grid()

#UI Parser
UIParserBt = tkinter.Button(mainwindow, height = 2, width = 20, bg ="#678596", fg = "#FFFFFF", text = "UI Log Parser", font = ("DM Sans", 20), command = UIParserWin)
UIParserBt.grid(column = 0, row = 1)

SpaceBet4 = tkinter.Frame(mainwindow, height = 30, width = 337, bg="#FFFFFF")
SpaceBet4.grid()

#ASCII Parser
ASCIIParserBt = tkinter.Button(mainwindow, height = 2, width = 20, bg ="#678596", fg = "#FFFFFF", text = "ASCII Log Parser", font = ("DM Sans", 20), command = ASCIIParserWin)
ASCIIParserBt.grid(column = 0, row = 4)

global CheckVar1
CheckVar1 = tkinter.IntVar() #make this global
global CheckVar2
CheckVar2 = tkinter.IntVar() #make this global
GenericASCII = tkinter.Checkbutton(mainwindow, text="Single File", variable= CheckVar1, onvalue =1 , offvalue = 0, bg="#FFFFFF")	
GenericASCII.grid(column = 0, row = 5, sticky = "w", padx = 129)
ControllerASCII = tkinter.Checkbutton(mainwindow, text="Multiple Files", variable= CheckVar2, onvalue =1 , offvalue = 0, bg="#FFFFFF")
ControllerASCII.grid(column = 0, row = 5, sticky = "w", padx = 250)

#ASCIILabel1 = tkinter.Label(mainwindow, text = "Parse ASCII Logs to columnar data in Excel",font =("DM Sans", 10), bg = "#FFFFFF", fg = "#000000").grid(column = 0, row = 3)
#ASCIILabel2 = tkinter.Label(mainwindow, text = "Rename text files name to C1, C2, ... and so on", font =("DM Sans", 10),bg = "#FFFFFF", fg = "#000000").grid(column = 0, row = 4)

SpaceBet1 = tkinter.Frame(mainwindow, height = 30, width = 337, bg="#FFFFFF")
SpaceBet1.grid()

#Test Time to Excel
TestTimeBt = tkinter.Button(mainwindow, height = 2, width = 20, bg ="#678596", fg = "#FFFFFF", text = "Test Time to Excel", font = ("DM Sans", 20), command = TestTimeWin)
TestTimeBt.grid(column = 0, row = 8)

TestTimeLabel1 = tkinter.Label(mainwindow, text = "Convert test time logs to Excel", font =("DM Sans", 10),bg = "#FFFFFF", fg = "#000000").grid(column = 0, row = 9)
TestTimeLabel2 = tkinter.Label(mainwindow, text = "Computes the average", font =("DM Sans", 10), bg = "#FFFFFF", fg = "#000000").grid(column = 0, row = 10)

SpaceBet2 = tkinter.Frame(mainwindow, height = 50, width = 337, bg="#FFFFFF")
SpaceBet2.grid()

AuthorFrame = tkinter.Frame(mainwindow, height = 80, width = 337, bg="#FFFFFF")
AuthorFrame.grid()
AuthorLabel = tkinter.Label(AuthorFrame, text = "by Sittie Montud", font =("DM Sans", 10), bg="#FFFFFF", fg="#000000").pack(ipady = 49, ipadx = 128)

mainwindow.mainloop()
