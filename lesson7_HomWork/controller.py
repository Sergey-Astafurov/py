import view
import model


def head_function():
    select = view.start()
    if select == 1 :
        model.exp_csv()
    elif select == 2:
        model.imp_csv()
    elif select == 3:
        model.exp_txt()
    elif select == 4:
        model.imp_txt()
