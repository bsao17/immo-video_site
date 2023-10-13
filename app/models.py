from app.blueprints.views import db


class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    # Ajoutez d'autres champs au besoin
