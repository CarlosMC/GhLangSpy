# GhLangSpy
BabelFish Repository Reconnaissance


## Prepare your .env file

Before running this python script you need to create an .env file with your own  **Github AUTH_TOKEN**
Like this one:


**cat .env**
```
GH_AUTH_TOKEN=ghp_XXXxXXxXxXXXXxXxXXXXXxxXxXxXxXXXXXXx
```



## Run it Localy


To run this python script you need first to install requirements 

**pip install -r requirements.txt**


Then you can run it with Pyton v3

**python3 ghLangS.py**
```
Ruby with 0.2985219955444336 megabytes of code
Puppet with 0.0965585708618164 megabytes of code
Shell with 0.0008068084716796875 megabytes of code

Total gigabytes of code : 0.0003866087645292282
```

## Test it Localy


There is one test to check if language list is not empty. 

**pytest ghLangSpy-tests.py**
```
============================================= test session starts =============================================
platform darwin -- Python 3.11.4, pytest-7.4.0, pluggy-1.3.0
rootdir: /Users/cmoyano/workspace/lsst-task/GhLangSpy
collected 1 item

ghLangSpy-tests.py .                                                                                    [100%]

============================================== 1 passed in 0.62s ==============================================
```

## Test and Run it from Docker


You can run it directly from DockerHub using latest TAG.
Make sure you pass it the **.env** file with your own **Github AUTH_TOKEN**  

**docker run --rm --env-file .env carlosmc/ghlangspy:latest**
```
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-7.4.0, pluggy-1.3.0
rootdir: /
collected 1 item

ghLangSpy-tests.py .                                                     [100%]

============================== 1 passed in 0.60s ===============================
Ruby with 0.2985219955444336 megabytes of code
Puppet with 0.0965585708618164 megabytes of code
Shell with 0.0008068084716796875 megabytes of code

Total gigabytes of code : 0.0003866087645292282
```
