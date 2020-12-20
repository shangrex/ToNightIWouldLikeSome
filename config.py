class set_machine():
    def __init__(self):
        pass

    def state(self):
        return ["initial", "save_text", "load_text", "show_image"]
    
    def transition(self):
        return [
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "save_text",
            "conditions": "is_going_to_save_text",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "load_text",
            "conditions": "is_going_to_load_text",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "show_image",
            "conditions": "is_going_to_show_image",
        },
        {"trigger": "go_back", "source": ["save_text", "load_text", "show_image"], "dest": "initial"},
        ]
    
    def initial(self):
        return "initial"
    
    def auto_transitions(self):
        return False
    def show_conditions(self):
        return True