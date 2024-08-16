from controller.view_controller.view_controller import ViewController


class Controller:
    def __init__(self) -> None:
        self.view_controller = ViewController()
    
    def update(self):
        self.view_controller.update()