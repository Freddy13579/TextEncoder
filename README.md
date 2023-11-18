# TextEncoder
Simple Text Encoder with output copying into the clipboard automaticly.

To get rid of the text copying into the clipboard simply delete lines 28, 52 .

I advice to change the mysalt string at line 9 with an output from ```os.urandom(16) ``` to make sure that other people cant decrypt your text with your passworld on their computers. 

Compile yourself with: ```pyinstaller --noconfirm --onefile --console  "Encoder.py"```



USAGE: 
```
[Mode e/d] [Text] [Passworld]
```
or
```
No args -> Guided prompts
```

