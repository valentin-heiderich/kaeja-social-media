import app.GUI.Elements.Server as ServerWidget
import app.data.basicData as bD


class UpdateServerList:
    def __init__(self):
        self.serverList = bD.server_list

    def update(self):
        for server in self.serverList:
            server_widget = ServerWidget.ServerWidget(server)
