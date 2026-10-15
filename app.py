from flask import Flask,render_template

app=Flask(__name__)
projects=[
{
"title":"Weather Information App",
"description":"A desktop application that displays weather information.",
"tech_stack":[ 
    "Python",
    "Tkinter (GUI)",
    "Requests",
    "OpenWeatherMap API",
    "Open-Meteo API",
    "Pillow",
    "Threading"
],
"github_url":"https://github.com/haidarshadoud/Weather_Info",
"image":"Weather.jpg"

      },
{
    "title":"News Article Summarizer",
    "description":"A python NLP application that extracts news articles from URLs, generates extractive summarizer using word-frequency scoring,  and identifies named entites.",
    "tech_stack":[
    "Python",
    "Newspaper3k",
    "spaCy",
    "NLTK",
    "Natural Language Processing (NLP)",
    "Extractive Text Summarization",
    "Named Entity Recognition (NER)"

     
 ],
    "github_url":"https://github.com/haidarshadoud/News_Article_Summareizer",
    "image":"News_Summarizer.jpg"

      },
{
    "title":"Calculator",
    "description":"A simple calculator application bulit with python.",
    "tech_stack":[
    "Python",
    "Tkinter (GUI)",
    "Object-Oriented Programming (OOP)"
    ],
    "github_url":"https://github.com/haidarshadoud/Tkinter-Calculator",
    "image":"Calculator.jpg",


      },  
{
    "title":"Sales Data Analysis",
    "description":"A python project for analyzing sales data.",
    "tech_stack":[
    "Python",
    "Pandas",
    "Matplotlib",
    "Data Analysis",
    "Data Visualization"

    ],
    "github_url":"https://github.com/haidarshadoud/Sales_Data_Analaysis",
    "image":"sales_analysis.png"

       },
{
    "title":"File Organizer",
    "description":"A python application that orgnaizes files into folders based on their file types.",
    "tech_stack":[
    "Python",
    "Tkinter (GUI)",
    "OS Module",
    "Pathlib",
    "Shutil",
    "Threading",
    "Pickle",
    "Datetime",
    "Object-Oriented Programming (OOP)"

    ],
    "github_url":"https://github.com/haidarshadoud/Organizing-files-into-folders",
    "image":"file_organizer.jpg"

       },
{
    "title":"YouTube Video Downloader",
    "description":"A python application for downloading videos from YouTube.",
    "tech_stack":[
    "Python",
    "Tkinter (GUI)",
    "yt-dlp",
    "FFmpeg",
    "Threading",
    "Logging",
    "Regular Expressions (Regex)",
    "OS & File Handling"
    ],
    "github_url":"https://github.com/haidarshadoud/Download_From_Youtube",
    "image":"youtube_downloader.jpg"
     },
{
    "title":"Password Generator",
    "description":"A python application that generates random passwords.",
    "tech_stack":[
    "Python",
    "Random Module",
    "String Module",
    "Functions",
    "Exception Handling"

    ],
    "github_url":"https://github.com/haidarshadoud/Password-Generator-main",
    "image":"",

     },

{
    "title":"Number Gussing Game",
    "description":"A python game where the player tries to guess a randomly generated number.",
    "tech_stack":[
    "Python",
    "Random Module",
    "Functions",
    "Loops & Conditional Statements",
    "Exception Handling"

    ],
    "github_url":"https://github.com/haidarshadoud/Number-Guessing-Game",
    "image":"",
     },
{
    "title":"Advanced Face Detection System",
    "description":"An avanced face detection system using multiple detection methods, including Haar Cascade. The system supports real-time webcam detection, image processing, with face counting and visual annotations.",
    "tech_stack":[
    "Python",
    "OpenCV",
    "NumPy",
    "Haar Cascade",
    "Deep Learning (DNN)",
    "HOG (Histogram of Oriented Gradients)",
    "Real-Time Face Detection",
    "Image & Video Processing",
    "Webcam Integration"
    ],
    "github_url":"",
    "image":"face_detection.jpg",

     }     

]




@app.route("/")
def home( ):
    return render_template("index.html",projects=projects)

if __name__=="__main__":
    app.run(debug=True)