class Character:
    def __init__(self, name, affiliation, old_name, old_affiliation):
        self.name = name
        self.affiliation = affiliation
        self.old_name = old_name
        self.old_affiliation = old_affiliation

    def __str__(self):
        return f"name = {self.old_name} --> {self.name}\nafiliação = {self.old_affiliation} --> {self.affiliation}"