
from . recipe import Recipe

class CreateInterfaceEthernet(Recipe):
    def __init__(self, session, command_file):
        super().__init__(session, command_file)

    # Define any custom processing of parameters here by overriding
    # configure:
    #
    # def configure(self):
    #     self.data = transform_data(self.data)
    #     super().configure()