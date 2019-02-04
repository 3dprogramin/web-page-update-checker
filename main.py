#!/usr/bin/python2.7

# Keep track of updates on a webpage, using a browser and by comparing page text

from view import View
from browser import Browser
from time import sleep, strftime
import os, sys

# Settings
# --------
CHECK_EVERY = 10        # seconds
# end of settings
# ---------------
is_windows = os.name == 'nt'
browser = None

# print update to UI
def print_update(u):
    View.normal('New update: {} - {} chars'.format(strftime('%H:%M:%S'), len(u)))

# main method
def main():

    View.banner()
    global browser
    url = None
    try:
        # check for args
        if len(sys.argv) < 2:
            View.warning('URL must be given as parameter')
            return
        url = sys.argv[-1]
        View.normal('URL: {}'.format(url))
        View.normal('Starting browser...')
        browser = Browser()
        View.normal('Browser up')
        print_update(browser.check(url))     # get initial value
        while True:
            update = browser.check(url)      # check for new update
            if update: print_update(update)  # print update, if any
            sleep(CHECK_EVERY)
    except KeyboardInterrupt:
        View.ctrl_c_pressed()
    except Exception, ex:
        View.error(ex)
    finally:
        if browser: browser.dispose()
        View.normal('Finished !')
        if is_windows: raw_input()      # pause on windows

if __name__ == "__main__":
    main()