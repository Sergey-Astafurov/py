import model_mult as md_mult
import model_sum as md_sum
import view

def button_click():
    value_a = int(input("value = "))
    value_b = int(input("value = "))
    md_mult.init(value_a, value_b)
    md_sum.init(value_a, value_b)
    result = md_mult.do_it()
    result2 = md_sum.do_it()
    view.view_data(result, "mult")
    view.view_data(result2, "sum")