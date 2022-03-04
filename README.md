# PythonSeleniumFramework
To setup:
  Download PyCharm and install
  Download Python and install
  Download the framework and open in pycharm
  
  Open Pycharm terminal and run the following:
    pip install pytest
    pip install selenium
    pip install pytest-html
    pip install webdriver manager
    
  To run sample test:
    Click arrow next to each test will run a single test
    
  To run via command line:
    Open terminal
    Run pytest -- will run all test use -v for verbose -s to print console logs
  To run test in a specific file 
    pytest <filename>
  To run test that match a specific tag
    pytest -m <tag>
  To run in specific browser
    pytest --browser_name <browser in all lowercase> this defaults to chrome when not entered
  To run test and generate html reports with screenshots 
    pytest --html=<filepath to framework root>/test/reports.html
  
