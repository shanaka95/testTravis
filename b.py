import urllib

testfile = urllib.URLopener()
testfile.retrieve("https://wordpress.org/latest.zip", "file.zip")
