from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='In Progress')
    budget = db.Column(db.Float, nullable=False, default=0.0)  # Novo campo para orçamento
    timeline = db.Column(db.Text, nullable=True)  # Novo campo para cronograma

    def __repr__(self):
        return f'<Project {self.title}>'
