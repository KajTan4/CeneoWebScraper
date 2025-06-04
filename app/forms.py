from wtforms import Form, StringField, SubmitField, validators

class ProductForm(Form):
    def __init__(self):
        product_id = StringField("Identyfikator produktu", 
                                 name='product_id', 
                                 id='product_id',
                                 validators=[
                                     validators.DataRequired(message="Kod produktu jest wymagany"),
                                     validators.Regexp("^[0-0]*$",message="Kod produkt może zawierać"),
                                     validators.Length(min=5, max = 10, message="Kod produktu powinien ")
                                 ])
        submit = SubmitField("Pobierz opinie")