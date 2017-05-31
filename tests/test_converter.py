
def test_convert_money(app):
    app.open_home_page()
    app.convertpage.type_sum_convertation('300')
    app.convertpage.choose_from_currency_value('EUR')

    #Test has money params

    # Выбрать валюту из
    # выбрать валюту в
    # Выбрать источник карта сбербанка
    # Choose get out - card
    # Choose change - internet bank
    # Choose time real
    # Press show
    # Check you have pop up with correct data
#
# def test_check_ui(app):
#     pass
#




