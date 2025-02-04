# Reproduce ie driver crash

A reproduce for ie driver crash.

## Reproduce steps

1. Run `py -3.12 -m venv .env` to create a virtual environment.
2. Open 2 terminals. Run `.\.env\Scripts\Activate.ps1` to activate the environment.
3. In terminal 1, run `python -m http.server -b 127.0.0.1 8080` to start a http server.
4. In terminal 2, run `python main.py` to start selenium driver.
5. Wait for the driver to crash.

## Logs

```txt
PS C:\Users\13721\workspace\github.com\kvii\reproduce_ie_driver_crash> python main.py
Traceback (most recent call last):
  File "C:\Users\13721\workspace\github.com\kvii\reproduce_ie_driver_crash\main.py", line 8, in <module>
    driver.execute_script('window.open("b.html")')
  File "C:\Users\13721\workspace\github.com\kvii\reproduce_ie_driver_crash\.env\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 528, in execute_script
    return self.execute(command, {"script": script, "args": converted_args})["value"]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\13721\workspace\github.com\kvii\reproduce_ie_driver_crash\.env\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 429, in execute
    self.error_handler.check_response(response)
  File "C:\Users\13721\workspace\github.com\kvii\reproduce_ie_driver_crash\.env\Lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 232, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.JavascriptException: Message:
```

## Screenshot:

![screenshot](./screenshot.png)
