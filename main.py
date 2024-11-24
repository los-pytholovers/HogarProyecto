import random

from datetime import datetime, timedelta



def persoJuridicaHogar():

    persoJuridicaHogar = ["Hogar de Esperanza del Pacífico", "Centro de Ayuda Costa Serena","Refugio Luz del Amanecer","Refugio Luz del Amanecer","Casa de Solidaridad Bahía Azul",
                         "Fundación Brisas del Mar","Albergue Faro de Vida","Hogar Corazones de Puntarenas","Asociación Manos Unidas del Puerto","Centro de Apoyo Estrella del Pacífico"]

    return random.choice(persoJuridicaHogar)

#def generar_fecha_vigenciaHogar():

    dias_vigencia = random.randint(365, 365 * 4)

    fecha_actual = datetime.now()

    #return fecha_actual + datetime.timedelta(days=dias_vigencia)

def distritoHogar():

    distritoHogar = ["Puntarenas","Barranca","Chacarita","El Roble"]

    return random.choice(distritoHogar)

def ubicacionHogar():

    ubicacionHogar = ["100 mts este del bar la juventud","50 metros norte de la Catedral de Puntarenas","200 metros sur del Parque Marino del Pacífico","75 metros oeste del Mercado Municipal de Puntarenas","150 metros noreste del Hospital Monseñor Sanabria."
                     ,"100 metros suroeste del Paseo de los Turistas","50 metros al este de la Terminal de Buses de Chacarita","200 metros al norte del Estadio Lito Pérez","75 metros al sur del Muelle de Puntarenas","100 metros al oeste del Banco Nacional"]

    return random.choice(ubicacionHogar)

def telefonoHogar():

    telefonoHogar = ["23478569","78451296","96385274","23014539","84607156","98654710","78463109","98014752","89610200","78624593"]

    return random.choice(telefonoHogar)

def correoHogar():
    correoHogar = ["contacto@hogaresperanza.org","info@costaserenaayuda.org","admin@luzdelamanecer.org","bahia.azul@solidaridad.org","contacto@brisasdelmar.org","farodevida@ayuda.org","corazones@hogarespuntarenas.org","manosunidas@puerto.org","estrella@apoyopacifico.org","armonia.esperanza@refugios.org"]

    return random.choice(correoHogar)

def atencionHogar():
    atencionHogar = ["Temporal", "Permonante", "Temporal y Permenante"]
    return random.choice(atencionHogar)

def jovenAncianoHogar():
    jovenAncianoHogar = ["Adultos Mayores", "Jovenes"]
    return random.choice(jovenAncianoHogar)

def puntosHogar():
    puntosHogar = ["5","4","3","2","1"]
    return random.choice(puntosHogar)

print("El nombre es:" +persoJuridicaHogar()+" la fecha de vigencia es: "+ " el distrito es en: "+distritoHogar()+" La ubicacion es: "+ubicacionHogar()+" el numero de telefono es: "+telefonoHogar()+" el correo electronico es: "+correoHogar()+" su situacion es: "+atencionHogar()+" atienden a: "+jovenAncianoHogar()+" Sus puntos obtenidos: "+puntosHogar())

