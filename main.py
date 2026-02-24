#This is where we will run everyone's MadLibs! 
import chupzi, eli, eve, zoe, sai, emmett, gigi, audrey, tanner, meital, michael

choice = input("Whose Mad Lib do you want to try?")

choice = choice.strip()
choice = choice.lower()


if (choice == "chupzi"):
   chupzi.chupzi_mad_lib()

elif(choice=="Meital"):
   Meital.Meital_mad_lib()
elif (choice == "emmett"):
   emmett.emmett_mad_lib()
elif (choice == "audrey"):
   audrey.audrey_mad_lib()
if (choice == "eve"): 
   eve.eve_mad_lib()

