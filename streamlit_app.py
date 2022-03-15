import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Sharad Tawade, Data Scientist.
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- I am a Data Science and Machine Learning enthusiast. My interest includes Statistics, Machine Learning and Programming. 
- I am keen to work on projects that offer learning opportunities and provide a platform to nurture my skills and knowledge. 
- I am 4+ Years experienced Project Engineer with a demonstrated history of working in the electrical and industrial automation industry. 
- Skilled in PLC, SCADA, HMI, DCS, Database, IoT, IIoT Application.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/sharad-tawade/" target="_blank">Sharad Tawade</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#data-science-project">Data Science Project</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**MBA- Operation** (Operation Management), *Welingkar Instistute of Management*, Mumbai',
'2019-2021')
st.markdown('''
- Percentage: `80%`
- Passed with Distinction
''')

txt('**Bachelors of Engineering** (Electrical Engineering), *Mumbai University*',
'2013-2017')
st.markdown('''
- CGPA: `7.62`
- Graduated with First Class Honors.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Science Trainee**, Almabetter',
'Oct-2021- Present')
st.markdown('''
- Machine Learning, NLP, SQL
''')

txt('**Data science and business analytics**, The Spark Foundation',
'Nov-2021-Dec-2021')
txt('**Automation Engineer**, Mobinext Technologies Pvt. Ltd, Navi Mumbai',
'Feb-2021-Oct-2021')
st.markdown('''
- Node-Red for IoT application
- Node-Red, AWS communication
- AWS-DynamoDB, IoT
- SCADA report generation with SQL database.
- VB Scripting
- Report generation using Visual basic and WAMP server.
''')
txt('**Project Engineer**, Multiquadrant Industrial Controls Pvt. Ltd, Mumbai',
'Oct-2018-Sep-2020')
st.markdown('''
- SCADA- WinCC explorer, WinCC professional, Intouch.
- Siemens PLC(S7-200, 300, 1200, 1500) logic development on simatic manager, TIA portal of process control system.
- Siemens HMI development.
- SCADA report generation with SQL database. 
- Networks- PROFIBUS, PROFINET, ETHERNET, MODBUS
- Report generation using Visual basic and WAMP server.
- Drives- Siemens AC and DC drives.
- On site/Off shore project support. 
- Performing FAT and SAT.
- Project execution.
''')

txt('**Project Engineer**, Unicorn Controls Pvt.Ltd, Mumbai',
'Dec-2017-Sep-2018')
st.markdown('''
- Siemens CNC 828d, 840d commissioning.
- Project Planing ,Project execution 
- Eplan designing.
- CNC 828d screen development.
- Working on turning, milling CNC system.
- CNC machine Field wiring checking.
- Attend service call of Siemens and Ge-fanuc CNC systems
''')
#######################
st.markdown('''
## Data Science Project
''')

txt('**1. EDA - Global Terrorism Analysis**','')
st.markdown('''
*Keywords* - *`EDA`,`GTD`,`terrorist group`,`attack region`*
- The work has been carried out upon the Global Terrorism Database (GTD), which is an open database containing list of terrorist activities from 1970 to 2017.
- In this analysis, analyses the changes in terrorism over the last year and highlights the countries most impacted by terrorism, explores the individual characteristics of terrorists and terrorist groups in order to shed a light on the drivers of terrorism, analyses the major terrorist groups, including a historical analysis of how groups have ended in the past
''')

txt('**2. Regression - Bike Sharing Demand Prediction**','')
st.markdown('''
*Keywords* - *`EDA`,`machine learning`,`regression`,`bike sharing`*
- The objective of this work is to predict the trip duration of rental bikes in the Seoul Bike sharing system. The data used include weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall), the number of bikes rented per hour and date information.
- Feature  engineering  is  done  to  extract additional features from the data. Five statistical models are used to predict the trip duration.
  1. Linear regression
  2. Decision Tree
  3. Random Forest (RF)
  4. Gradient boosting machines
  5. Extreme Gradient Boosting (XGBoost) 
''')

txt('**3. Classification - Mobile Price Range Prediction**','')
st.markdown('''
*Keywords* - *`EDA`,`Classification`,`machine learning`,`mobile price range`*
- The key purpose of this research work is to determine "If the mobile with given features would be under a certain price range." Specific feature selection algorithms are used to recognize and delete features that are less necessary and redundant, and have minimal complexity in computation.
- Feature  engineering  is  done  to  extract additional features from the data. Four statistical models are used to predict the price range 
  1. Logistic regression
  2. Decision Tree
  3. Random Forest (RF).
  4. Gradient boosting machines
  5. Extreme Gradient Boosting (XGBoost) 
  6. Support Vector Classification
  7. Neural Network
''')
txt('**4. Restaurant Review Sentiment Analysis**','')
st.markdown('''
*Keywords* - *`NLP`,`sentiment analysis`,`text preprocessing`,`machine learning`*
- Automate detection of different sentiments from textual comments and feedback, A machine learning model is created to understand the sentiments of the restaurant reviews. The problem is that the review is in a textual form and the model should understand the sentiment of the review and automate a result.
- The main motive behind this project is to classify whether the given feedback or review in textual context is positive or negative. Reviews can be given to the model and it classifies the review as a negative review or a positive
- The restaurant reviews are very related to the project topic as reviews are made on websites and we can apply this model on such data sets to get the sentiments.
- Heroku deployment link - https://sentiment-restaurant-reviews.herokuapp.com/
''')


#####################
# st.markdown('''
# ## Bioinformatics Tools
# ''')
# txt4('ABCpred', 'A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors', 'http://codes.bio/abcpred/')
# txt4('AutoWeka', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
# txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
# txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
# txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
# txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
# txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
# txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
# txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
# txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
# txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
# txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
# txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
# txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
# txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
# txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
# txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `VB Scripting`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', ' `Heroku`,`AWS`, `streamlit`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/sharad-tawade/')
txt2('Twitter', 'https://twitter.com/SharadTawade2')
txt2('GitHub', 'https://github.com/tawadesharad/')
# txt2('', 'https://github.com/chaninlab/')
# txt2('', 'https://github.com/dataprofessor')
# txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
# txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
# txt2('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
# txt2('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
# txt2('Publons', 'https://publons.com/a/303133/')
