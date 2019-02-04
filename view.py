class View:
    # banner
    @staticmethod
    def banner():
        View.new_line()
        print '[+] Web-page update checker'
        View.new_line()

    # prints a message
    @staticmethod
    def normal(msg):
        print '[+] {}'.format(msg)
  
    # prints a warning
    @staticmethod
    def warning(warning):
        print '[-] {}'.format(warning)

    # prints an error
    @staticmethod
    def error(error):
        print '[!] Error: {}'.format(error)

    # ctrl+c key combination was pressed
    @staticmethod
    def ctrl_c_pressed():
        View.warning('CTRL+C was pressed, stopping')

    # a pause for windows terminal
    @staticmethod
    def pause():
        raw_input('[+] Press ENTER to continue/close window ...')

    # prints a line with dashes
    @staticmethod
    def new_line():
        print '--------------------------------------------------------------------------------'

