# liveshare-auto-host


Tool for VSCode [LiveShare](https://github.com/MicrosoftDocs/live-share).

Create webpage with LS link, and restart server if link is dead.


> ![Webpage](https://i.imgur.com/R6tPTKI.png)

For use :
- Change shortcuts in VScode
- Search "liveshare", and update
- liveshare.collaboration.link.copy  ```ctrl-*```
- liveshare.start  ```shift-w```
- liveshare.stop  ```shift-q```
- For picture update line 14 in img.py (x, y, h, w)
- Start webserver ```python3 server.py```
- Site ```http://localhost:8888/index.py?code=1``` (you can update the code)
