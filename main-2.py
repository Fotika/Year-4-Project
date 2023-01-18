from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import tkinter.font as font
import math
import numpy as np
import decision_rules

############################
# GRAPHICAL USER INTERFACE #
############################

#APPLICATION WINDOW CONFIGURATION#
root = Tk()
height = 512
width = 1024
root.geometry("{width}x{height}".format(height=height, width=width))


#FRAMES#
#Header Frame
headerframe = Frame(root)
headerframe.pack(side = TOP, pady=10)

#Bottom Frame
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM ,pady=200)

#CHARACTER FONT
ButtonFont = font.Font(family='Helvetica', size=10)
HeaderFont = font.Font(family="Helvetica", size=25)
SubHeaderFont = font.Font(family="Helvetica", size=15)
TextFont = font.Font(family="Helvetica", size=8)


###########################
#      RECORD HISTORY     #
###########################
counter = 1
history_list = []

def clearHistory(history):
    history.clear()
    return history


##########################
### CREATE MATRIX PAGE ###
##########################

#Input Events and Alternatives to create matrix
def createMatrix():
    topMatrixMenu = Toplevel()
    topMatrixMenu.title("Create Matrix")
    topMatrixMenu.geometry("{width}x{height}".format(height=height, width=width))
    root.withdraw()


    ###############################
    # FRAMES - CREATE MATRIX PAGE #
    ###############################
    #HEADER FRAME
    headerframe_topMatrixMenu = Frame(topMatrixMenu)
    headerframe_topMatrixMenu.pack(side = TOP, pady=20, anchor="center" , padx=50)
    #MID FRAME
    midframe_topMatrixMenu = Frame(topMatrixMenu)
    midframe_topMatrixMenu.pack(side = TOP, anchor="center", padx=50)

    #BOTTOM FRAME
    bottomframe_topMatrixMenu = Frame(topMatrixMenu)
    bottomframe_topMatrixMenu.pack(side = BOTTOM ,pady=50, anchor="center", padx=50)


    ##########################################
    # BUTTON ALLOCATION - CREATE MATRIX PAGE #
    ##########################################
    #CREATE MATRIX BUTTON
    createMatrix = Button(midframe_topMatrixMenu,text="Create Matrix", command=lambda: (specifyMatrix(entry_r.get(), entry_c.get())), bg="#11D84D", fg="#ffffff",bd=2, pady=1, font=ButtonFont)
    createMatrix.pack(side=LEFT, padx=5) 
      
    #RETURN PREVIOUS PAGE BUTTON
    returnRoot = Button(midframe_topMatrixMenu,text="Return Homepage", command=lambda: (root.deiconify(),topMatrixMenu.destroy()),bg="grey", bd=2, pady=1, font=ButtonFont)
    returnRoot.pack(side=LEFT, padx=5)   

    #CREATE MATRIX PAGE EXIT BUTTON
    Exit=Button(midframe_topMatrixMenu,text="Exit",command=Exit_app,bg="#990000",fg="#ffffff",bd=2,pady=1,width=5,font=ButtonFont)
    Exit.pack(side=LEFT, padx=5)
    
    #Enter Number of Alternatives
    rowLabel = Label(headerframe_topMatrixMenu,text= "Enter the number of Alternatives:", font=SubHeaderFont, fg="purple")
    rowLabel.pack(side=TOP, anchor="w")
    entry_r = Entry(headerframe_topMatrixMenu, width=5, bd=2)
    entry_r.pack(side=TOP, anchor="w",padx=20, pady=5)
    global r
    r=entry_r.get()

    #Enter Number of Events
    columnLabel = Label(headerframe_topMatrixMenu,text= "Enter the number of Events:", font=SubHeaderFont, fg="purple")
    columnLabel.pack(side=TOP, anchor="w")
    entry_c = Entry(headerframe_topMatrixMenu, width=5, bd=2)
    entry_c.pack(side=TOP, anchor="w", padx=20, pady=5)
    global c
    c=entry_c.get()


    ##############################
    ### INITIALIZE MATRIX PAGE ###
    ##############################
    def specifyMatrix(r,c):
        specifyMatrixMenu = Toplevel()
        specifyMatrixMenu.title("Matrix Parameters")
        specifyMatrixMenu.geometry("{width}x{height}".format(height=height, width=width))
        topMatrixMenu.withdraw()

        if len(r) < 1 or r.isnumeric() == False:
            #WARNING HEADER
            errorDesc="Error!"
            warningSubject = Label(specifyMatrixMenu,text=errorDesc, font=SubHeaderFont,fg="red")
            warningSubject.grid(row=0, padx=height/2, pady=50)
            
            #WARNING DESCRIPTION
            errorDesc="Your alternative number is not valid, alternative number should be bigger than '0'."
            warningDescription = Label(specifyMatrixMenu,text=errorDesc, font=TextFont)
            warningDescription.grid(row=1, padx=height/2)
            
            #RETURN PREVIOUS PAGE BUTTON
            returnCreation = Button(specifyMatrixMenu,text="Return Matrix Creation", command=lambda: (topMatrixMenu.deiconify(),specifyMatrixMenu.destroy()),bg="grey", bd=2, pady=1, font=ButtonFont)
            returnCreation.grid(row=2, column=0)   

            #EXIT BUTTON
            Exit=Button(specifyMatrixMenu,text="Exit",command=Exit_app,bg="#990000",fg="#ffffff",bd=2,pady=1,width=5,font=ButtonFont)
            Exit.grid(row=3, column=0)

        elif len(c) < 1 or c.isnumeric() == False:
            #WARNING HEADER
            errorDesc="Error!"
            myLabel = Label(specifyMatrixMenu,text=errorDesc, font=SubHeaderFont,fg="red")
            myLabel.grid(row=0,padx=height/2, pady=50)

            #WARNING DESCRIPTION           
            errorDesc="Your event number is not valid, event number should be bigger than '0'."
            myLabel = Label(specifyMatrixMenu,text=errorDesc, font=TextFont)
            myLabel.grid(row=1, padx=width/2)
            
            #RETURN PREVIOUS PAGE BUTTON
            returnCreation = Button(specifyMatrixMenu,text="Return Matrix Creation", command=lambda: (topMatrixMenu.deiconify(),specifyMatrixMenu.destroy()),bg="grey", bd=2, pady=1, font=ButtonFont)
            returnCreation.grid(row=2, padx=height/2)   

            #EXIT BUTTON
            Exit=Button(specifyMatrixMenu,text="Exit",command=Exit_app,bg="#990000",fg="#ffffff",bd=2,pady=1,width=5,font=ButtonFont)
            Exit.grid(row=3, column=0)

        else:


            ##############################
            # HEADERS - INIT MATRIX PAGE #
            ##############################
            #Matrix Header
            matrixDesc="Number of Alternatives: {row}\t\nNumber of Events: {col}\t".format(row=r,col=c)
            matrixHeader = Label(specifyMatrixMenu,text=matrixDesc, font=SubHeaderFont)
            matrixHeader.grid(row=0, column=0)

            #Alternative Header
            alternative_row=4
            alternative_column=0
            alternativeHeader = Label(specifyMatrixMenu,text="Alternatives", font=SubHeaderFont, fg="#006666").grid(row=alternative_row,column=alternative_column)


            ########################################
            # INITIALIZE VALUES - INIT MATRIX PAGE #
            ########################################
            #ALTERNATIVE LABELS
            #Initialize Alternative Labels
            alt_lbl_var = []
            alt_lbl_entries = []
            for i in range(int(r)):
                alt_lbl_entries.append([])
                alt_lbl_var.append(StringVar())           
                alternative_label_entry = Entry(specifyMatrixMenu, textvariable=alt_lbl_var[i], width=15,bg="pink")
                alternative_label_entry.grid(row=alternative_row+1+i,column=alternative_column,pady=5,padx=10) 
           
            #Initialize Likelihood
            likeli_var = []
            likeli_entries = []
            def upLikeli(Rule):
                for j in range(int(c)):
                    if clicked.get()=="Exp_Value":
                        likeli_entries.append([])
                        likeli_var.append(StringVar())
                        likeli_var_entry = Entry(specifyMatrixMenu, textvariable=likeli_var[j], width=15, bg="light green") 
                        likeli_var_entry.grid(row=alternative_row+int(r)+1,column=event_column+j,padx=10)
                    else:
                        likelihood_var = Entry(specifyMatrixMenu, width=15,state=DISABLED)
                        likelihood_var.grid(row=alternative_row+int(r)+1,column=event_column+j,padx=10)
                return likeli_var

            #Event Header
            event_row=3
            event_column=1
            eventHeader = Label(specifyMatrixMenu,text="Events", font=SubHeaderFont, fg="#006666")
            eventHeader.grid(row=event_row,column=event_column)



            #Initialize Event Labels
            event_lbl_var = []
            event_lbl_entries = []

            for j in range(int(c)):
                
                ### Initialize Event Labels
                event_lbl_entries.append([])
                event_lbl_var.append(StringVar())
            
                event_label_entry = Entry(specifyMatrixMenu, textvariable=event_lbl_var[j], width=15,bg="light blue")
                event_label_entry.grid(row=event_row+1,column=event_column+j,padx=10)   


            
            #Initialize Event Values
            event_val_var = []
            event_val_entries = []

            # callback function to get your StringVars
            for i in range(int(r)):
                # append an empty list to your two arrays
                # so you can append to those later
                event_val_var.append([])
                event_val_entries.append([])
                for j in range(int(c)):
                    # append your StringVar and Entry
                    event_val_var[i].append(StringVar())
                    event_val_entries[i].append(Entry(specifyMatrixMenu, textvariable=event_val_var[i][j],width=15))
                    event_val_entries[i][j].grid(row=event_row+2+i,column=event_column+j,padx=10)



            #Initialize Alternative Labels' Matrix
            alt_lbl_matrix=[]
            def get_alt_lbl_var():				 
                for i in range(int(r)):
                    alt_lbl_matrix.append([])
                    alt_lbl_matrix[i].append(alt_lbl_var[i].get())
                return alt_lbl_matrix


            #Initialize Event Labels' Matrix
            event_lbl_matrix=[]
            def get_event_lbl_var():		   
                for i in range(int(r)):
                    event_lbl_matrix.append([])
                    event_lbl_matrix[i].append(event_lbl_var[i].get())
                return event_lbl_matrix

            #Initialize Event Values' Matrix
            event_val_matrix=[]
            def get_event_val_var():
                for i in range(int(r)):
                    event_val_matrix.append([])
                    for j in range(int(c)):
                        event_val_matrix[i].append(float(event_val_var[i][j].get()))
                
                return event_val_matrix

            #Initialize Likelihood Values' Matrix
            event_likeli_matrix=[]
            def get_likeli_val_var():
                event_likeli_matrix.clear()
                for i in range(int(c)):
                    event_likeli_matrix.append([])
                    event_likeli_matrix[i].append(float(likeli_var[i].get()))
                return event_likeli_matrix

            likely_var = BooleanVar(value=False)
            likelyCheck = Label(specifyMatrixMenu, text = "Enter The Likelihood Of The Events", font=TextFont)
            likelyCheck.grid(column=alternative_column,row=alternative_row+int(r)+1)

            #Initialize values
            likelyhood_arr = []
            for i in range(int(c)):
                global likelihood_values
                likelihood_values = IntVar()
                likelihood_var = Entry(specifyMatrixMenu, width=15,bg="light green", textvariable=likelihood_values)
                likelihood_var.grid(row=alternative_row+int(r)+1,column=event_column+i,padx=10)           
            
            def checkRule():   
                if clicked.get() == "Exp_Value":
                    return get_likeli_val_var(), get_event_lbl_var(), get_alt_lbl_var(), get_event_val_var(), reportAnalysis(clicked.get()), specifyMatrixMenu.destroy()
                else:
                    return get_event_lbl_var(), get_alt_lbl_var(), get_event_val_var(), reportAnalysis(clicked.get()), specifyMatrixMenu.destroy()  
        
            # DROPDOWN MENU
            options = [
                "MaxiMin",
                "MaxiMax",
                "MiniMax",
                "Laplace",
                "Exp_Value"
            ]
            clicked = StringVar()
            clicked.set(options[0])



            ######################################
            # BUTTON ALLOCATION - REPORT DISPLAY #
            ######################################

            #EXIT BUTTON
            Exit=Button(specifyMatrixMenu,text="Exit",command=Exit_app,bg="#990000",fg="#ffffff",bd=2,pady=1,width=10,font=ButtonFont)
            Exit.grid(row=alternative_row+int(r)+2, column=alternative_column+3, sticky="w", padx=10)

            #START SIMULATION BUTTON
            checkButton = Button(specifyMatrixMenu, text="Initialize", width=10, command=checkRule, bg="bisque3",font=ButtonFont)
            checkButton.grid(row=alternative_row+int(r)+2, column=alternative_column+1, sticky="w", padx=10) 

            #RETURN PREVIOUS PAGE BUTTON
            returnCreation = Button(specifyMatrixMenu,text="Configure", command=lambda: (topMatrixMenu.deiconify(),specifyMatrixMenu.destroy()),bg="grey", bd=2, pady=1, font=ButtonFont, width=10)
            returnCreation.grid(row=alternative_row+int(r)+2, column=alternative_column+2, sticky="w", padx=10)   
            
            #DECISION RULE BUTTON
            drop = OptionMenu(specifyMatrixMenu, clicked ,*options, command=upLikeli)          
            drop.grid(row=alternative_row+int(r)+2, column=alternative_column)

  
            
            ######################
            ### REPORT DISPLAY ###
            ######################
            
            def reportAnalysis(Rule):
                reportAnalysisMenu = Toplevel()
                reportAnalysisMenu.title("Decision Report")
                reportAnalysisMenu.geometry("{width}x{height}".format(height=height, width=width))
                specifyMatrixMenu.withdraw()
                myResults = Label(reportAnalysisMenu, text= "Decision Results",font=HeaderFont, fg="#990099")
                myResults.grid(row=0, column=1, pady=10, padx = 20, columnspan=int(c))

                master_frame = Frame(reportAnalysisMenu, bg='Light Blue', bd=3, relief=RIDGE)
                master_frame.grid(column=1,row=1,sticky="nsew")
                master_frame.grid_columnconfigure(0, weight=1)
                master_frame.grid_rowconfigure(0,weight=1)




                #################################
                ### FRAME 1 - SELECTION FRAME ###
                #################################

                # Dsiplay Decision Table
                parameterTable = Label(master_frame, text='Selected Parameters',font=SubHeaderFont, bg="light blue", fg="purple", relief=RIDGE)
                parameterTable.grid(row=2, column=0, pady=5, sticky="nw")

                # Create a frame for the canvas and scrollbar(s).
                frame1 = Frame(master_frame, bd=2, relief=FLAT)
                frame1.grid(row=3, column=0, sticky="nw")  
                
                canvas1 = Canvas(frame1)
                canvas1.grid(row=0, column=0)

                buttons_frame1 = Frame(canvas1)         
                # Create canvas window to hold the buttons_frame.
                canvas1.create_window((0,0), window=buttons_frame1, anchor="nw")

                ################################
                ### FRAME 2 - DECISION TABLE ###
                ################################

                # Create a frame for the canvas and scrollbar(s).
                frame2 = Frame(master_frame, bd=2, relief=FLAT)
                frame2.grid(row=5, column=0, sticky="nw")

                # Add a canvas in that frame.
                canvas2 = Canvas(frame2, bg="pink")
                canvas2.grid(row=0, column=0)

                # Create a vertical scrollbar linked to the canvas.
                vsbar = Scrollbar(frame2, orient="vertical", command=canvas2.yview)
                vsbar.grid(row=0, column=1, sticky="ns")
                canvas2.configure(yscrollcommand=vsbar.set)

                # Create a horizontal scrollbar linked to the canvas.
                hsbar = Scrollbar(frame2, orient="horizontal", command=canvas2.xview)
                hsbar.grid(row=1, column=0, sticky="ew")
                canvas2.configure(xscrollcommand=hsbar.set)

                # Create a frame on the canvas to contain the grid of buttons.
                buttons_frame2 = Frame(canvas2)         
                # Create canvas window to hold the buttons_frame.
                canvas2.create_window((0,0), window=buttons_frame2, anchor="nw")

                # RECORD ADD BUTTON
                def add_record():
                    global counter
                    if Rule == "MaxiMax":
                        history_list.append([counter,
                                                decision_rules.MaxiMax(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[0],
                                                "".join(decision_rules.MaxiMax(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[1]),
                                                "".join(decision_rules.MaxiMax(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[2]),
                                                decision_rules.MaxiMax(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[3]])

                    if Rule == "MaxiMin":
                        history_list.append([counter,
                                             decision_rules.MaxiMin(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[0],
                                             "".join(decision_rules.MaxiMin(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[1]),
                                             "".join(decision_rules.MaxiMin(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[2]),
                                             decision_rules.MaxiMin(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[3]])                 
                    
                    if Rule == "Laplace":
                        history_list.append([counter,
                                             decision_rules.Laplace(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[0],
                                             "".join(decision_rules.Laplace(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[1]),
                                             "-",
                                             decision_rules.Laplace(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[2]])                      

                    if Rule == "MiniMax":
                        history_list.append([counter,
                                                decision_rules.MiniMax(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[0],
                                                "".join(decision_rules.MiniMax(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[1]),
                                                "-",
                                                decision_rules.MiniMax(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[2]])                       
                    if Rule == "Exp_Value":
                        history_list.append([counter,
                                             decision_rules.Exp_Value(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix, event_likeli_matrix)[0],
                                             "".join(decision_rules.Exp_Value(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix,event_likeli_matrix)[1]),
                                             "-",
                                             decision_rules.Exp_Value(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix,event_likeli_matrix)[2]])                      

                    counter+=1
                    return history_list

                
                ######################################
                # FRAME ALLOCATION - REPORT DISPLAY #
                ######################################

                #ADD RECORD BUTTON
                addRecordButton = Button(master_frame,text="Add Record>>", bg="#009999", fg="#ffffff", bd=2, pady=1, width=10,command=add_record(), font=ButtonFont)
                addRecordButton.grid(row=3,column=2,padx=20, sticky="nw") 
                
                #VIEW RECORD BUTTON
                viewRecordButton = Button(master_frame,text="View Records", bg="#9933FF", fg="#ffffff", bd=2, pady=1, width=10,command=lambda:[reportTable(Rule),reportAnalysisMenu.withdraw()], font=ButtonFont)
                viewRecordButton.grid(row=3,column=2,padx=20, sticky="nw", pady=30) 

                #RETURN DECISION BUTTON
                ReturnDecision = Button(master_frame,text="Configure", command=lambda: (specifyMatrix(r,c),reportAnalysisMenu.withdraw()),bg="grey", bd=2, pady=1, font=ButtonFont, width=10)
                #ReturnDecision.pack(side=LEFT,padx=5)               
                ReturnDecision.grid(row=3,column=2,padx=20, sticky="nw", pady=60)               

                #EXIT BUTTON
                Exit=Button(master_frame,text="Exit", command=Exit_app,bg="#990000",fg="#ffffff",bd=2,pady=1,width=10,font=ButtonFont)
                #Exit.pack(side=LEFT)
                Exit.grid(row=3, column=2,padx=20, sticky="nw",pady=90)
                
              


                #REPORT MAXIMAX DECISION

                if Rule == "MaxiMax":  
                    #DISPLAY SELECTED PARAMETERS
                    #Diplay Alternative
                    alternativeDescription = Label(buttons_frame1, text="Selected Alternative:", font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    alternativeDescription.grid(row=0,column=0,sticky="nw")
                    alternativeDescriptionValue = Label(buttons_frame1, text=decision_rules.MaxiMax(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[1], font=SubHeaderFont, fg="blue", anchor="w",width=20)
                    alternativeDescriptionValue.grid(row=0,column=1,sticky="nw")

                    #Diplay Event
                    eventDescription = Label(buttons_frame1, text="Under Event:", font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    eventDescription.grid(row=1,column=0,sticky="nw") 
                    eventDescriptionValue = Label(buttons_frame1, text=decision_rules.MaxiMax(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[2], font=SubHeaderFont, fg="blue", anchor="w",width=20)
                    eventDescriptionValue.grid(row=1,column=1,sticky="nw")
                                   
                    #Diplay Output
                    outputDescription = Label(buttons_frame1, text="Expected Outcome:", font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    outputDescription.grid(row=2,column=0,sticky="nw") 
                    outputDescriptionValue = Label(buttons_frame1, text=decision_rules.MaxiMax(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[3], font=SubHeaderFont, fg="blue", anchor="w",width=20)
                    outputDescriptionValue.grid(row=2,column=1,sticky="nw")

                    #Display Decision Table
                    decisionTable  = Label(master_frame, text= "Decision Table", font=SubHeaderFont, bg="light blue", fg="purple", relief=RIDGE)
                    decisionTable.grid(row=4, column=0, columnspan=int(c),sticky="nw")

                    for row_val in range(int(r)):
                        AlternativeLabelGrid = Label(master=buttons_frame2, text=alt_lbl_matrix[row_val], font=TextFont, fg="blue", width=15, bd=2, relief=RIDGE )
                        AlternativeLabelGrid.grid(row=row_val+3,column=1)
                        for col_val in range(int(c)):
                            DecisionGrid = Label(master=buttons_frame2, text=event_val_matrix[row_val][col_val], font=TextFont, width=15, bg="orange", borderwidth=2, relief=GROOVE)
                            DecisionGrid.grid(row=row_val+3,column=col_val+2,sticky="news")
                
                    for col_val in range(int(c)):
                        EventLabelGrid = Label(buttons_frame2, text=event_lbl_matrix[col_val], font=TextFont, fg="blue", width=15,bd=2, relief=RIDGE)
                        EventLabelGrid.grid(row=2, column=col_val+2,sticky="news")
            


                #REPORT EXPECTED VALUE DECISION                           
                elif Rule == "Exp_Value":

                    #DISPLAY SELECTED PARAMETERS
                    #Display Alternative
                    alternativeDescription = Label(buttons_frame1, text="Selected Alternative:", font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    alternativeDescription.grid(row=0,column=0,sticky="nw")
                    alternativeDescriptionValue = Label(buttons_frame1, text=decision_rules.Exp_Value(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix,event_likeli_matrix)[1], font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    alternativeDescriptionValue.grid(row=0,column=1,sticky="nw")

                    #Display Output
                    outputDescription = Label(buttons_frame1, text="Expected Outcome:", font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    outputDescription.grid(row=2,column=0,sticky="nw") 
                    outputDescriptionValue = Label(buttons_frame1, text=decision_rules.Exp_Value(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix,event_likeli_matrix)[2], font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    outputDescriptionValue.grid(row=2,column=1,sticky="nw")

                    #Display Decision Table
                    decisionTable  = Label(master_frame, text= "Decision Table", font=SubHeaderFont, bg="light blue", fg="purple", relief=RIDGE)
                    decisionTable.grid(row=4, column=0, columnspan=int(c),sticky="nw")

                    for row_val in range(int(r)):
                        AlternativeLabelGrid = Label(master=buttons_frame2, text=alt_lbl_matrix[row_val], font=TextFont, fg="blue", width=20, bd=2, relief=RIDGE )
                        AlternativeLabelGrid.grid(row=row_val+2,column=1)
                        for col_val in range(int(c)):
                            DecisionGrid = Label(master=buttons_frame2, text=event_val_matrix[row_val][col_val], font=TextFont, width=9, bg="orange", borderwidth=2, relief=GROOVE)
                            DecisionGrid.grid(row=row_val+2,column=col_val+2,sticky="news")
     
                    for col_val in range(int(c)):
                        EventLabelGrid = Label(buttons_frame2, text=event_lbl_matrix[col_val], font=TextFont, fg="blue", width=20,bd=2, relief=RIDGE)
                        EventLabelGrid.grid(row=1, column=col_val+2,sticky="news")

                    for col_val in range(int(c)):
                        LikeliLabelGrid = Label(buttons_frame2, text=event_likeli_matrix[col_val], font=TextFont, fg="blue", width=20,bd=2, relief=RIDGE)
                        LikeliLabelGrid.grid(row=int(r)+3, column=col_val+2,sticky="news")   

                   

                #REPORT MAXIMIN DECISION
                elif Rule == "MaxiMin":  
                    #DISPLAY SELECTED PARAMETERS
                    #Display Alternative
                    alternativeDescription = Label(buttons_frame1, text="Selected Alternative:", font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    alternativeDescription.grid(row=0,column=0,sticky="nw")
                    alternativeDescriptionValue = Label(buttons_frame1, text=decision_rules.MaxiMin(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[1], font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    alternativeDescriptionValue.grid(row=0,column=1,sticky="nw")

                    #Diplay Event
                    eventDescription = Label(buttons_frame1, text="Under Event:", font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    eventDescription.grid(row=1,column=0,sticky="nw") 
                    eventDescriptionValue = Label(buttons_frame1, text=decision_rules.MaxiMin(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[2], font=SubHeaderFont, fg="blue", anchor="w",width=20)
                    eventDescriptionValue.grid(row=1,column=1,sticky="nw")
                                   
                    #Diplay Output
                    outputDescription = Label(buttons_frame1, text="Expected Outcome:", font=SubHeaderFont, fg="blue", anchor="w",width=20)
                    outputDescription.grid(row=2,column=0,sticky="nw") 
                    outputDescriptionValue = Label(buttons_frame1, text=decision_rules.MaxiMin(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[3], font=SubHeaderFont, fg="blue", anchor="w",width=20)
                    outputDescriptionValue.grid(row=2,column=1,sticky="nw")

                    #Display Decision Table
                    decisionTable  = Label(master_frame, text= "Decision Table", font=SubHeaderFont, bg="light blue", fg="purple", relief=RIDGE)
                    decisionTable.grid(row=4, column=0, columnspan=int(c),sticky="nw")

                    for row_val in range(int(r)):
                        AlternativeLabelGrid = Label(master=buttons_frame2, text=alt_lbl_matrix[row_val], font=TextFont, fg="blue", width=20, bd=2, relief=RIDGE )
                        AlternativeLabelGrid.grid(row=row_val+3,column=1)
                        for col_val in range(int(c)):
                            DecisionGrid = Label(master=buttons_frame2, text=event_val_matrix[row_val][col_val], font=TextFont, width=9, bg="orange", borderwidth=2, relief=GROOVE)
                            DecisionGrid.grid(row=row_val+3,column=col_val+2,sticky="news")
                
                    for col_val in range(int(c)):
                        EventLabelGrid = Label(buttons_frame2, text=event_lbl_matrix[col_val], font=TextFont, fg="blue", width=20,bd=2, relief=RIDGE)
                        EventLabelGrid.grid(row=2, column=col_val+2,sticky="news")








                #REPORT LAPLACE DECISION
                if Rule == "Laplace":  
                    #DISPLAY SELECTED PARAMETERS
                    #Display Alternative
                    alternativeDescription = Label(buttons_frame1, text="Selected Alternative:", font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    alternativeDescription.grid(row=0,column=0,sticky="nw")
                    alternativeDescriptionValue = Label(buttons_frame1, text=decision_rules.Laplace(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[1], font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    alternativeDescriptionValue.grid(row=0,column=1,sticky="nw")
                                   
                    #Diplay Output
                    outputDescription = Label(buttons_frame1, text="Expected Outcome:", font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    outputDescription.grid(row=2,column=0,sticky="nw") 
                    outputDescriptionValue = Label(buttons_frame1, text=decision_rules.Laplace(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[2], font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    outputDescriptionValue.grid(row=2,column=1,sticky="nw")

                    #Display Decision Table
                    decisionTable  = Label(master_frame, text= "Decision Table", font=SubHeaderFont, bg="light blue", fg="purple", relief=RIDGE)
                    decisionTable.grid(row=4, column=0, columnspan=int(c),sticky="nw")

                    for row_val in range(int(r)):
                        AlternativeLabelGrid = Label(master=buttons_frame2, text=alt_lbl_matrix[row_val], font=TextFont, fg="blue", width=15, bd=2, relief=RIDGE )
                        AlternativeLabelGrid.grid(row=row_val+3,column=1)
                        for col_val in range(int(c)):
                            DecisionGrid = Label(master=buttons_frame2, text=event_val_matrix[row_val][col_val], font=TextFont, width=15, bg="orange", borderwidth=2, relief=GROOVE)
                            DecisionGrid.grid(row=row_val+3,column=col_val+2,sticky="news")
                
                    for col_val in range(int(c)):
                        EventLabelGrid = Label(buttons_frame2, text=event_lbl_matrix[col_val], font=TextFont, fg="blue", width=15,bd=2, relief=RIDGE)
                        EventLabelGrid.grid(row=2, column=col_val+2,sticky="news")


                #REPORT MINIMAX DECISION
                if Rule == "MiniMax":  
                    #Display Alternative
                    alternativeDescription = Label(buttons_frame1, text="Selected Alternative:", font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    alternativeDescription.grid(row=0,column=0,sticky="nw")
                    alternativeDescriptionValue = Label(buttons_frame1, text=decision_rules.MiniMax(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[1], font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    alternativeDescriptionValue.grid(row=0,column=1,sticky="nw")
                                   
                    #Diplay Output
                    outputDescription = Label(buttons_frame1, text="Expected Outcome:", font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    outputDescription.grid(row=2,column=0,sticky="nw") 
                    outputDescriptionValue = Label(buttons_frame1, text=decision_rules.MiniMax(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[2], font=SubHeaderFont, fg="blue", anchor="w", width=20)
                    outputDescriptionValue.grid(row=2,column=1,sticky="nw")

                    #Display Decision Table
                    decisionTable  = Label(master_frame, text= "Decision Table", font=SubHeaderFont, bg="light blue", fg="purple", relief=RIDGE)
                    decisionTable.grid(row=4, column=0, columnspan=int(c),sticky="nw")

                    for row_val in range(int(r)):
                        AlternativeLabelGrid = Label(master=buttons_frame2, text=alt_lbl_matrix[row_val], font=TextFont, fg="blue", width=15, bd=2, relief=RIDGE )
                        AlternativeLabelGrid.grid(row=row_val+3,column=1)
                        for col_val in range(int(c)):
                            DecisionGrid = Label(master=buttons_frame2, text=event_val_matrix[row_val][col_val], font=TextFont, width=15, bg="orange", borderwidth=2, relief=GROOVE)
                            DecisionGrid.grid(row=row_val+3,column=col_val+2,sticky="news")
                
                    for col_val in range(int(c)):
                        EventLabelGrid = Label(buttons_frame2, text=event_lbl_matrix[col_val], font=TextFont, fg="blue", width=15,bd=2, relief=RIDGE)
                        EventLabelGrid.grid(row=2, column=col_val+2,sticky="news")


                    ##############################
                    ### FRAME 3 - REGRET TABLE ###
                    ##############################
                    
                    # Dsiplay Decision Table
                    regretTable = Label(master_frame, text='Regret Table',font=SubHeaderFont, bg="light blue", fg="purple", relief=RIDGE)
                    regretTable.grid(row=4, column=2, padx=20 ,sticky="nw")

                    # Create a frame for the canvas and scrollbar(s).
                    frame3 = Frame(master_frame, bd=2, relief=FLAT)
                    frame3.grid(row=5, column=2, sticky="nw",padx=20)

                    # Add a canvas in that frame.
                    regretCanvas = Canvas(frame3, bg='pink')
                    regretCanvas.grid(row=0, column=2)

                    # Create a vertical scrollbar linked to the canvas.
                    r_vsbar = Scrollbar(frame3, orient="vertical", command=regretCanvas.yview)
                    r_vsbar.grid(row=0, column=3, sticky="ns")
                    regretCanvas.configure(yscrollcommand=r_vsbar.set)

                    # Create a horizontal scrollbar linked to the canvas.
                    r_hsbar = Scrollbar(frame3, orient="horizontal", command=regretCanvas.xview)
                    r_hsbar.grid(row=1, column=2, sticky="ew")
                    regretCanvas.configure(xscrollcommand=r_hsbar.set)

                    # Create a frame on the canvas to contain the grid of buttons.
                    regret_buttons_frame = Frame(regretCanvas)              
                    regretCanvas.create_window((0,0), window=regret_buttons_frame, anchor="nw")
                    for row_val in range(int(r)):
                        # Display Alternative Labels
                        AlternativeLabelGrid = Label(master=regret_buttons_frame, text=alt_lbl_matrix[row_val], font=TextFont, fg="blue", width=20, bd=2, relief=RIDGE )
                        AlternativeLabelGrid.grid(row=row_val+3,column=1)
                        
                        # Initialize Inputs
                        for col_val in range(int(c)):
                            DecisionGrid = Label(master=regret_buttons_frame, text=decision_rules.MiniMax(event_val_matrix,alt_lbl_matrix ,event_lbl_matrix)[3][col_val][row_val],font=TextFont, width=20, bg="orange", borderwidth=2, relief=GROOVE)
                            DecisionGrid.grid(row=row_val+3,column=col_val+2)                   
                    
                    # Display Event Labels
                    for col_val in range(int(c)):
                        EventLabelGrid = Label(regret_buttons_frame, text=event_lbl_matrix[col_val], font=TextFont, fg="blue", width=20,bd=2, relief=RIDGE)
                        EventLabelGrid.grid(row=1, column=col_val+2,sticky="news")

                    # Needed to make bbox info available.
                    regret_buttons_frame.update_idletasks()

                    # Get bounding box of canvas with Buttons.
                    r_bbox2 = regretCanvas.bbox(ALL)

                    # Define the scrollable region as entire canvas with only the desired number of rows and columns displayed.
                    r_COLS_DISP=4
                    r_ROWS_DISP=4

                    r_w, r_h = r_bbox2[2]-r_bbox2[1], r_bbox2[3]-r_bbox2[1]
                    r_dw, r_dh = int((r_w/int(c)) * r_COLS_DISP), int((r_h/int(r)) * r_ROWS_DISP)
                    regretCanvas.configure(scrollregion=r_bbox2, width=r_dw, height=r_dh)    


                # Needed to make bbox info available.
                buttons_frame1.update_idletasks()  
                # Needed to make bbox info available.
                buttons_frame2.update_idletasks()  
              
                # Create canvas window to hold the buttons_frame.
                canvas2.create_window((0,0), window=buttons_frame2, anchor="nw")
        
                # Get bounding box of canvas with Buttons.
                bbox2 = canvas2.bbox(ALL)  

                # Define the scrollable region as entire canvas with only the desired number of rows and columns displayed.
                COLS_DISP=4
                ROWS_DISP=4

                w, h = bbox2[2]-bbox2[1], bbox2[3]-bbox2[1]
                dw, dh = int((w/int(c)) * COLS_DISP), int((h/int(r)) * ROWS_DISP)
                canvas1.configure(width=dw, height=dh) 
                canvas2.configure(scrollregion=bbox2, width=dw, height=dh)


                ######################
                ### REPORT DISPLAY ###
                ######################
                
                def reportTable(Rule):
                    reportTableMenu = Toplevel()
                    reportTableMenu.title("Rule Reports")
                    reportTableMenu.geometry("{width}x{height}".format(height=height, width=width))
                    reportAnalysisMenu.withdraw()
                    myResults = Label(reportTableMenu, text= "Decision Results",font=HeaderFont, fg="#990099")
                    myResults.grid(row=0, column=1, pady=10, padx = 20, columnspan=int(c))

                    report_master_frame = Frame(reportTableMenu, bg='Light Blue', bd=3, relief=RIDGE,padx=20,pady=20)
                    report_master_frame.grid(column=1,sticky="nsew")
                    report_master_frame.columnconfigure(0, weight=1)

                    #################################
                    ### FRAME 1 - SELECTION FRAME ###
                    #################################

                    # Dsiplay Decision Table
                    parameterTable = Label(report_master_frame, text='Rule Reports',font=SubHeaderFont, bg="light blue", fg="purple", relief=RIDGE)
                    parameterTable.grid(row=2, column=0, pady=5, sticky="nw")

                    # Create a frame for the canvas and scrollbar(s).
                    report_frame1 = Frame(report_master_frame, bd=2, relief=FLAT)
                    report_frame1.grid(row=3, column=0, sticky="nw")  
                    
                    report_canvas1 = Canvas(report_frame1)
                    report_canvas1.grid(row=0, column=0)
                    
                    # Create a vertical scrollbar linked to the canvas.
                    vsbar = Scrollbar(report_frame1, orient="vertical", command=report_canvas1.yview)
                    vsbar.grid(row=0, column=2, sticky="ns")
                    report_canvas1.configure(yscrollcommand=vsbar.set)
                    
                    # Create a frame on the canvas to contain the grid of buttons.
                    report_buttons_frame1 = Frame(report_canvas1)         
                    
                    # Create canvas window to hold the buttons_frame.
                    report_canvas1.create_window((0,0), window=report_buttons_frame1, anchor="nw")
                    history = ttk.Treeview(report_buttons_frame1, selectmode="browse")
                    history.grid(row=0,column=0,columnspan=int(c))
                    history["columns"]=("1","2","3","4","5")
                    history["show"]="headings"
                    history.column("1",width=30,anchor="c")
                    history.column("2",width=90,anchor="c")
                    history.column("3",width=90,anchor="c")
                    history.column("4",width=90,anchor="c")
                    history.column("5",width=90,anchor="c")
                    history.heading("1",text="id")
                    history.heading("2",text="Rule")
                    history.heading("3",text="Alternative")
                    history.heading("4",text="Event")
                    history.heading("5",text="Outcome")
                    
                    for record in range(len(history_list)):
                        history.insert("",'end',
                                values=(history_list[record][0], history_list[record][1],history_list[record][2],history_list[record][3],history_list[record][4]))


                    #CLEAR RECORD BUTTON
                    clearRecordButton = Button(report_master_frame,text="Clear Records", bg="#FFB266", fg="#ffffff", bd=2, pady=1, width=10,command=lambda: (clearHistory(history_list)), font=ButtonFont)
                    clearRecordButton.grid(row=3,column=2,sticky="nw") 

                    #RETURN DECISION BUTTON
                    ReturnDecision = Button(report_master_frame,text="Configure", command=lambda: [reportAnalysisMenu.deiconify(),reportTableMenu.destroy()],bg="grey", bd=2, pady=1, font=ButtonFont, width=10)
                    ReturnDecision.grid(row=3,column=2, sticky="nw", pady=30)               

                    #EXIT BUTTON
                    Exit=Button(report_master_frame,text="Exit", command=Exit_app,bg="#990000",fg="#ffffff",bd=2,pady=1,width=10,font=ButtonFont)
                    Exit.grid(row=3, column=2, sticky="nw",pady=60)



####################
### WELCOME PAGE ###
####################

#Welcome Page Allocation#
welcomeHeader = Label(root, text= "Please click below to start creating your decision matrix!", font=SubHeaderFont)
welcomeHeader.place(relx=0.5, rely=0.5, anchor=CENTER)
welcomeHeader = Label(root, text= "Welcome to Decision Simulation", font=HeaderFont)
welcomeHeader.place(relx=1,rely=1, anchor=CENTER)
welcomeHeader.pack()

#Exit App
def Exit_app():
    op=tkinter.messagebox.askyesno("Exit","Do you want to exit?")
    if op>0:
        root.destroy()

####################################
# BUTTON ALLOCATION - WELCOME PAGE #
####################################

#MATRIX CONFIGURATION PAGE
matrixButton = Button(bottomframe, text= "Create a decision matrix!",width= 20, command= createMatrix, relief=RAISED, bg="#11D84D", fg="#ffffff",bd=2, pady=1, font=ButtonFont)
matrixButton.pack(side=LEFT, padx=100)

#EXIT BUTTON
Exit=Button(bottomframe,text="Exit",command=Exit_app,bg="#990000",fg="#ffffff",bd=2,pady=1,width=5,font=ButtonFont)
Exit.pack(side=LEFT, padx=100)

#EXECUTION PROGRAM
root.mainloop()