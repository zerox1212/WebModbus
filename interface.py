import cherrypy

import modbus_driver

"""
Basic web page interface to send commands to modbus TCP slave
"""


class ControllerInterface(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

    @cherrypy.expose
    def command_slave1(self, value=0):
        modbus_driver.main(value)  # connect to the modbus slave and write the value

        print("Command sent to slave 1:", value)

        return self.index()  # FIXME instead of just refreshing the main page, should use AJAX instead


if __name__ == '__main__':

    web_app = ControllerInterface()
    # webapp.generator = web_service.ControllerWebService()
    cherrypy.quickstart(web_app)  # , '/', conf)

