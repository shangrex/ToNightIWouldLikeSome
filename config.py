class set_machine():
    def __init__(self):
        pass

    def state(self):
        return ["initial", "save_text", "load_text", "show_image", "find_place_nearby", "sticker", "clear_text", "sentiment", "find_place"]
    
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
            "source": "save_text",
            "dest": "initial",
            "conditions": "is_going_to_initial_from_save_text",
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
            "dest": "find_place_nearby",
            "conditions": "is_going_to_find_place_nearby",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "show_image",
            "conditions": "is_going_to_show_image",
        },
        {
            "trigger": "advance",
            "source": "find_place_nearby",
            "dest": "initial",
            "conditions": "is_going_to_initial_from_find_place_nearby",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "sticker",
            "conditions": "is_going_to_sticker",
        },
        {
            "trigger": "advance",
            "source": "sticker",
            "dest": "initial",
            "conditions": "is_going_to_initial_from_sticker",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "clear_text",
            "conditions": "is_going_to_clear_text",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "sentiment",
            "conditions": "is_going_to_sentiment",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "find_place",
            "conditions": "is_going_to_find_place",
        },
        {
            "trigger": "advance",
            "source": "find_place",
            "dest": "initial",
            "conditions": "is_going_to_initial_from_find_place",
        },
        {"trigger": "go_back", "source": ["save_text", "load_text", "show_image", "sticker", "clear_text", "sentiment"], "dest": "initial"},
        ]
    
    def initial(self):
        return "initial"
    
    def auto_transitions(self):
        return False
    def show_conditions(self):
        return True


def help_message():
    text = "The bot have 7 function \n\
            1. save text \n\
            2. load text \n\
            3. show iamge \n\
            4. find place nearby \n\
            5. sticker \n\
            6. clear text\n\
            7. sentiment\n\
            8. find place\n\
            help\n\
            fsm\n"

    return text