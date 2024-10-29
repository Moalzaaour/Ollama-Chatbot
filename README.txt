How to run ollama chatbot:
-first make sure to install ollama
-make sure to activate your VM to run ollama
-use the following commad to activate your VM:
.\chatbot\Scripts\Activate.ps1
-if that doesn't work, it might be because of security issues with windows and powershell. use the following command to temporally disable powershell security then activate your VM again:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

-use the following command to run the chatbot:
python or python3 main.py