from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    @abstractmethod
    def presentati(self):
        pass

    def nome_completo(self):
        return f"{self.nome} {self.cognome}"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nome_completo()} ({self.eta} anni)"


class Dipendente(Person):
    def __init__(self, nome, cognome, eta, azienda, stipendio):
        super().__init__(nome, cognome, eta)
        self.azienda = azienda
        self.stipendio = stipendio

    def presentati(self):
        print(f"Sono {self.nome_completo()}, lavoro in {self.azienda} "
              f"e guadagno {self.stipendio} euro al mese.")

    def stipendio_annuo(self):
        return self.stipendio * 12


class Studente(Person):
    def __init__(self, nome, cognome, eta, matricola, corso):
        super().__init__(nome, cognome, eta)
        self.matricola = matricola
        self.corso = corso
        self.voti = []

    def presentati(self):
        print(f"Sono {self.nome_completo()}, matricola {self.matricola}, "
              f"studio {self.corso}.")

    def aggiungi_voto(self, voto):
        self.voti.append(voto)

    def media_voti(self):
        if not self.voti:
            return 0
        return sum(self.voti) / len(self.voti)


class Docente(Dipendente):
    def __init__(self, nome, cognome, eta, azienda, stipendio, materia, ore_settimanali):
        super().__init__(nome, cognome, eta, azienda, stipendio)
        self.materia = materia
        self.ore_settimanali = ore_settimanali

    def presentati(self):
        print(f"Sono {self.nome_completo()}, insegno {self.materia} "
              f"per {self.ore_settimanali} ore a settimana presso {self.azienda}.")


class Freelance(Dipendente):
    def __init__(self, nome, cognome, eta, azienda, stipendio, partita_iva, tariffa_oraria):
        super().__init__(nome, cognome, eta, azienda, stipendio)
        self.partita_iva = partita_iva
        self.tariffa_oraria = tariffa_oraria

    def presentati(self):
        print(f"Sono {self.nome_completo()}, freelance con P.IVA {self.partita_iva}, "
              f"tariffa {self.tariffa_oraria} euro/ora.")

    def compenso(self, ore):
        return self.tariffa_oraria * ore


if __name__ == "__main__":
    try:
        p = Person("Mario", "Rossi", 40)
    except TypeError as errore:
        print("Errore previsto:", errore)
    print()

    dip = Dipendente("Luca", "Bianchi", 35, "Acme Spa", 2200)
    stu = Studente("Giulia", "Verdi", 22, "S12345", "Informatica")
    doc = Docente("Anna", "Neri", 45, "Liceo Scientifico", 2500, "Python", 18)
    fre = Freelance("Paolo", "Gialli", 30, "Studio Gialli", 0, "IT01234567890", 50)

    persone = [dip, stu, doc, fre]
    for persona in persone:
        print(persona)
        persona.presentati()
        print()

    stu.aggiungi_voto(28)
    stu.aggiungi_voto(30)
    print("Media di", stu.nome_completo(), ":", stu.media_voti())
    print("Stipendio annuo di", dip.nome_completo(), ":", dip.stipendio_annuo())
    print("Compenso di", fre.nome_completo(), "per 10 ore:", fre.compenso(10))

    assert issubclass(Dipendente, Person) and issubclass(Studente, Person)
    assert issubclass(Docente, Dipendente) and issubclass(Freelance, Dipendente)
    assert isinstance(doc, Person)
    print("\nGerarchia corretta")