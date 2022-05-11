import django
from FarmAPI.models import Ficha, Medicamento


class FichaRouter():

    def db_for_read(self, model, **hints):
        
        if model == Ficha:
            return 'ficha'
        else:
            return 'default'

    def db_for_write(self, model, **hints):
        if model == Ficha:
            return 'ficha'
        else:
            return 'default'


class MedicamentoRouter():

    def db_for_read(self, model, **hints):
    
        if model == Medicamento:
            return 'default'
        else:
            return 'default'

    def db_for_write(self, model, **hints):
        if model == Medicamento:
            return 'default'
        else:
            return 'default'