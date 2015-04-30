# Android-profile-GPU-rendering

* A Python script listening to port 8002 to serve http requests for `adb shell dumpsys gfxinfo`.
* A HTML page polling `http://localhost:8002/` to get and show the results.

Tested with OnePlus One + CM 12.1 (Android 5.1)

Usage
-----
1. Plug in your Android phone to USB port
2. In Settings - Developer options - Profile GPU rendering, choose `In adb shell dumpsys gfxinfo`
2. `python apgr.py`
3. Open apgr.html in your web browser, enter the package name of your app
4. Open the app, use it, and see results in the html
