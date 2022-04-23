from app.GUI.Elements.Server import ServerWidget
import app.data.basicData as bD


class UpdateServerList:
    def __init__(self):
        self.serverList = bD.server_list
        self.server_list_object_widget = bD.ServerListWidget

        self.update()

    def update(self):
        self.server_list_object_widget.clear_widgets()
        for server in self.serverList:
            server_widget = ServerWidget(self.server_list_object_widget, server)
