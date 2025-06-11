from wtforms import Form, StringField, SubmitField, validators

class ProductForm(Form):
        product_id = StringField("Identyfikator produktu", 
                                 name='product_id', 
                                 id='product_id',
                                 validators=[
                                     validators.DataRequired(message="Kod produktu jest wymagany"),
                                     validators.Regexp("^[0-9]*$",message="Kod produkt może zawierać jedynie cyfry"),
                                     validators.Length(min=5, max = 10, message="Kod produktu powinien miec od 5 do 10 znaków ")
                                 ])
        submit = SubmitField("Pobierz opinie")