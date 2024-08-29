from gunasoapp.forms import GunasoForm


def __init__(self, *args, **kwargs):
    super(GunasoForm, self).__init__(*args, **kwargs)
    self.fields['incident_location'].choices = self.get_branches()
    print("Choices set for incident_location:", self.fields['incident_location'].choices)
