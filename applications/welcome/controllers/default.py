
def index():
    response.flash = T("Hello Newbie!")
    return dict(message=T('Welcome to Online Learnig Platform Learner!'))
