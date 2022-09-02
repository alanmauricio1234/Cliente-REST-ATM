import requests

class Cliente:
    def __init__(self, url_base):
        self.url_base = url_base #http://localhost:5000/
    
    def consulta_tarjeta(self, n_tarjeta):
        url = 'banco/consulta_tarjeta/' + n_tarjeta # http://localhost:5000/tarjeta/n_tarjeta
        response = requests.get(self.url_base + url)
        data = response.json()
        return data['Tarjeta']['esta_tarjeta']
 
        
    def verifica_tarjeta(self, n_tarjeta):
        url = 'banco/verifica_tarjeta/' + n_tarjeta
        response = requests.get(self.url_base + url)
        data = response.json()
        return data['Tarjeta']['es_verificada'] 

    def verifica_tarjeta_bloqueada(self, n_tarjeta):
        url = 'banco/tarjeta_bloqueada/' + n_tarjeta
        response = requests.get(self.url_base + url)
        data = response.json()
        return data['Tarjeta']['es_bloqueada'] 

    def verifica_fecha(self, n_tarjeta):
        url = 'banco/verifica_fecha/' + n_tarjeta
        response = requests.get(self.url_base + url)
        data = response.json()
        return data['Tarjeta']['fecha_verificada']

    def verifica_nip(self, n_tarjeta, nip):
        url = 'banco/verifica_nip/' + n_tarjeta + '/' + nip
        response = requests.get(self.url_base + url)
        data = response.json()
        return data['Tarjeta']['es_correcto_nip']
    
    def consulta_intentos(self, n_tarjeta):
        url = 'banco/consulta_intentos/' + n_tarjeta
        response = requests.get(self.url_base + url)
        data = response.json()
        return data['Tarjeta']['intentos']

    def consulta_limite(self, n_tarjeta):
        url = 'banco/verifica_limite/' + n_tarjeta
        response = requests.get(self.url_base + url)
        data = response.json()
        return data['Tarjeta']['limite']

    def consulta_saldo(self, n_tarjeta):
        url = 'banco/consulta_saldo/' + n_tarjeta
        response = requests.get(self.url_base + url)
        data = response.json()
        return data['Tarjeta']['saldo']

    def realiza_pago(self, n_tarjeta, pago):
        url = 'banco/realiza_pago/' + n_tarjeta
        response = requests.post(self.url_base + url, json={'pago': pago})
        data = response.json()
        return data['Tarjeta']['pago']

        
class ClienteServicio:
    def __init__(self, url):
        self.client = Cliente(url)

    def verifica_tarjeta(self, n_tarjeta):
        mensaje = ''
        if not (self.client.consulta_tarjeta(n_tarjeta)):
            mensaje = 'El número de tarjeta no esta registado :('
        elif not (self.client.verifica_tarjeta(n_tarjeta)):
            mensaje = 'La tarjeta no esta verificada :('
        elif not (self.client.verifica_fecha(n_tarjeta)):
            mensaje = 'La fecha de vencimiento expiro :('

        return mensaje


    def verificar_tarjeta_completa(self, n_tarjeta):
        if not self.client.consulta_tarjeta(n_tarjeta):
            return False
        if not self.client.verifica_tarjeta(n_tarjeta):
            return False
        if not self.client.verifica_fecha(n_tarjeta):
            return False
        if self.client.verifica_tarjeta_bloqueada(n_tarjeta):
            return False
        return True

    def verificar_nip(self, n_tarjeta, nip):
        mensaje = ''
        if not (self.client.verifica_nip(n_tarjeta, nip)):
            mensaje = 'El NIP es incorrecto :('
        return mensaje

    def verificar_tarjeta_bloqueada(self, n_tarjeta):
        return self.client.verifica_tarjeta_bloqueada(n_tarjeta)

    def consultar_intentos(self, n_tarjeta):
        return self.client.consulta_intentos(n_tarjeta)

    def consulta_saldo(self, n_tarjeta):
        return self.client.consulta_saldo(n_tarjeta)
    
    def consulta_limite(self, n_tarjeta):
        return self.client.consulta_limite(n_tarjeta)

    def realiza_pago(self,n_tarjeta, pago):
        return self.client.realiza_pago(n_tarjeta, pago)

    