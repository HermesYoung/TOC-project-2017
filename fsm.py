from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return  'hi' in text.lower() or  'hello' in text.lower()

    def is_going_to_state2(self, update):
        text = update.message.text
        return text == 'get code'

    def is_going_back_to_state2(self, update):
        text = update.message.text
        return  'no'  in text.lower()
    
    
    def is_going_to_state3(self, update):
        text = update.message.text
        return '@' in text
   
    def is_going_to_state4(self, update):
        text = update.message.text
        return  'yes' in text.lower()
    
    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == 'resend'

    def on_enter_state1(self, update):
        update.message.reply_text("Hello\n to get  a Verification Code enter : get Code\nto resend enter :resend")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("E-mail please")


    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("Is E-Mail correct ?")
        self.go_back(update)
            
    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        update.message.reply_text("Send to E-mail")
        self.go_back(update)
    
    def on_exit_state4(self, update):
        print('Leaving state4')

    def on_enter_state5(self, update):
        update.message.reply_text("Resnd to E-mail")
        self.go_back(update)
    
    def on_exit_state5(self, update):
        print('Leaving state5')

    

