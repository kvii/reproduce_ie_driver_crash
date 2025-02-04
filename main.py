from selenium import webdriver

# run this command first
# python -m http.server -b 127.0.0.1 8080
driver = webdriver.Ie(service=webdriver.IeService("IEDriverServer.exe"))

driver.get("http://127.0.0.1:8080/a.html")
driver.execute_script('window.open("b.html")')
