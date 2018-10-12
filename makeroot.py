import numpy as np
import ROOT
from array import array
from ROOT import TGraph, TH1F, TFile, TCanvas, TPaveText

filename = "sporcle.txt"

inpscore, inpmaximum, inppercentage, inpaverage, inpdifference, category, inpday, inpplayers, winnipeg = np.loadtxt(filename, dtype = 'string', unpack=True)

score = []
maximum = []
percentage = []
average = []
difference = []
day = []
players = []
fracdifference = []


for i in inpscore:
    score.append(float(i))
for i in inpmaximum:
    maximum.append(float(i))
for i in inppercentage:
    percentage.append(float(i))
for i in inpaverage:
    average.append(float(i))
for i in inpdifference:
    difference.append(float(i))
for i in inpday:
    day.append(int(i))
for i in inpplayers:
    players.append(int(i))

for i in range (0, len(difference)):
    fracdifference.append(difference[i]/average[i])

    
h_difference = TH1F("difference", "Difference between recorded percentage score and average percentage", 50, -101, 101)
for i in difference:
    h_difference.Fill(i)

h_fracdifference = TH1F("fracdifference", "Fractional Difference between recorded percentage score and average percentage", 50, -1, 1)
for i in fracdifference:
    h_fracdifference.Fill(i)
    
h_score = TH1F("score", "Raw score from sporcle quiz", int(max(score)+1)/4, -1, int(max(score)+1))
for i in score:
    h_score.Fill(i)

h_maximum = TH1F("maximum", "Maximum score for sporcle quiz", int(max(maximum)+1)/4, -1, int(max(maximum)+1))
for i in maximum:
    h_maximum.Fill(i)

h_percentage = TH1F("percentage", "Percentage score from sporcle quiz", 50, -1, 101)
for i in percentage:
    h_percentage.Fill(i)

h_average = TH1F("average", "Average public score for sporcle quiz", 50, -1, 101)
for i in average:
    h_average.Fill(i)

h_day = TH1F("day", "Day on which sporcle quiz was attempted", max(day)+1, -1, max(day)+1)
for i in day:
    h_day.Fill(float(i))

h_players = TH1F("players", "Number of players playing the quiz", max(players)+1, -1, max(players)+1)
for i in players:
    h_players.Fill(float(i))

h_difference.SetFillColor(2)
h_fracdifference.SetFillColor(3)
h_score.SetFillColor(4)
h_maximum.SetFillColor(5)
h_percentage.SetFillColor(6)
h_average.SetFillColor(7)
h_day.SetFillColor(8)
h_players.SetFillColor(9)

c_forgov = TCanvas("forgov", "Canvas for Gov. <3", 1000, 1000)
h_fracdifference.GetXaxis().SetTitle("This is the x axis")
h_fracdifference.GetYaxis().SetTitle("This is the y axis")
h_fracdifference.Draw()
text = TPaveText(0.1, 0.7, 0.3, 0.9)
text.AddText("There is no z axis")
text.Draw()
c_forgov.BuildLegend()
c_forgov.Print("canvasforgov.png")


s_file = TFile("SporcleAnalysis.root", "RECREATE")

h_difference.Write("Difference")
h_fracdifference.Write("FractionalDifference")
h_score.Write("Score")
h_maximum.Write("Maximum")
h_percentage.Write("Percentage")
h_average.Write("Average")
h_day.Write("Day")
h_players.Write("Players")
s_file.Close()
