# MSA Assessent 1 Project

The simulated device is in the form of a python script at `simulated-devices/Device.py`. It used the connection string to connect to msa-assessment2-project-hub (the project's IoT Hub on Azure). The hub then used a stream analytics job to stream the data to Power BI. I then created a report on Power BI called msaAssessment2Project. This report contains a few visualisations using the data, as well as some text explanations, demonstrating how similar data collected from actual IoT devices could be used (although it is just for demonstartive purposes).

## Note for MSA about report

Although I was able to share the IoT Hub and the stream analytics job the recommended way, I was unable to do the same for the Power BI workspace and report. Instead I have followed the "Alternative Project Submission" for those, adding the report as a pdf file to this github repo as `report.pdf`. However this exported pdf shows different values than the ones shown on the workspace, I have also included `reportScreenshot.png` to show what I see on my screen since it is more demonstrative of the data due to the graphs being less cluttered with datapoints. I have also included a pdf of the report retrieved from Power BI by going File > Print from within the report editor's top toolbar, and choosing Windows 10's "print to pdf" option (this "printed" pdf is `reportPrintout.pdf`). My only guess as to why the exported pdf shows something different than what I see is that it is including more datapoints than when the report was created, however I'm not sure why the printed pdf shows what I see then since its also provided by Power BI.

## Note for MSA about email

This github is attached to my univeristy email jarod.cunningham@students.mq.edu.au (as is my microsoft learn account, Azure account, and Power BI account), while I registered to MSA using a personal email of jarodlc@hotmail.com

I hope this doesn't cause too much confusion or difficulty