# Android-profile-GPU-rendering

* A Python script listening to port 8000 to serve http requests for `adb shell dumpsys gfxinfo`.
* A HTML page polling `http://localhost:8000/` to get and show the results.

Tested with OnePlus One + CM 12.1 (Android 5.1)

Usage
-----
1. Plug in your Android phone to USB port
2. `python apgr.py`
3. Open apgr.html in your web browser, enter the package name of your app
4. Open the app, use it
