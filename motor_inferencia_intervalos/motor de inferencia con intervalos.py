#representacion de hechos, lista de diccionarios
HECHOS = [
    {
        "id": "H1",
        "descripcion": "La actividad física incrementa el gasto energético de una persona.",
        "categoria": "gasto_energetico"
    },
    {
        "id": "H2",
        "descripcion": "Una alimentación saludable se basa en 4 principios: adecuación, equilibrio, moderación y diversidad.",
        "categoria": "principios_nutricion"
    },
    {
        "id": "H3",
        "descripcion": "Una alimentación saludable no debe tener contaminantes ni químicos dañinos.",
        "categoria": "inocuidad"
    },
    {
        "id": "H4",
        "descripcion": "El exceso de azúcares puede aumentar el riesgo de problemas de salud.",
        "categoria": "riesgo_salud"
    },
    {
        "id": "H5",
        "descripcion": "El consumo adecuado de proteínas contribuye al mantenimiento y desarrollo de la masa muscular.",
        "categoria": "macronutrientes"
    },
    {
        "id": "H6",
        "descripcion": "El consumo de frutas y verduras forma parte de una alimentación saludable.",
        "categoria": "alimentos_recomendados"
    },
    {
        "id": "H7",
        "descripcion": "Una alimentación adecuada debe proporcionar la energía y nutrientes que necesita la persona.",
        "categoria": "requerimiento_diario"
    },
    {
        "id": "H8",
        "descripcion": "Las calorías que el cuerpo gasta en reposo se estiman con edad, peso, estatura y sexo.",
        "categoria": "metabolismo_basal"
    },
    {
        "id": "H9",
        "descripcion": "El IMC clasifica a un adulto en peso bajo, normal, sobrepeso u obesidad.",
        "categoria": "diagnostico_imc"
    },
    {
        "id": "H10",
        "descripcion": "Una alimentación saludable debe tener bajo contenido de grasas no saludables, azúcares libres y sodio.",
        "categoria": "restricciones"
    },
    {
        "id": "H11",
        "descripcion": "Las necesidades de proteína pueden aumentar según el nivel de actividad física y los objetivos relacionados con el desarrollo o mantenimiento muscular.",
        "categoria": "hipertrofia"
    },
    {
        "id": "H12",
        "descripcion": "Un desequilibrio energético sostenido es uno de los factores que puede contribuir al sobrepeso y la obesidad.",
        "categoria": "balance_energetico"
    },
    {
        "id": "H13",
        "descripcion": "Los adultos deben hacer actividad física moderada cada semana y ejercicios de fuerza.",
        "categoria": "actividad_fisica"
    },
    {
        "id": "H14",
        "descripcion": "Cualquier actividad física es mejor que el sedentarismo.",
        "categoria": "actividad_fisica"
    },
    {
        "id": "H15",
     "descripcion": "Se recomienda reducir ultraprocesados, carnes rojas y bebidas azucaradas.",
        "categoria": "restricciones"
    },
    {
        "id": "H16",
      "descripcion": "El gasto energético total considera el gasto en reposo y la energía utilizada durante las actividades físicas.",
        "categoria": "gasto_energetico"
    }
]

#reglas
REGLAS = {
    # R1: objetivo de perdida de peso
    "R1": {
        "si": lambda m: m["objetivo"] == "bajar_peso",
        "entonces": lambda m: {"factor_calorias": -500, "proteina_g_kg": 2.0},
        "hechos_soporte": ["H1", "H7", "H12"]
    },
    # R2: objetivo de ganancia muscular
    "R2": {
        "si": lambda m: m["objetivo"] == "ganar_musculo",
            "entonces": lambda m: {"factor_calorias": 300, "proteina_g_kg": 2.2},
            "hechos_soporte": ["H5", "H7", "H11"]
    },
    # R3: objetivo de mantenimiento
    "R3": {
        "si": lambda m: m["objetivo"] == "mantenimiento",
        "entonces": lambda m: {"factor_calorias": 0, "proteina_g_kg": 1.6},
        "hechos_soporte": ["H2", "H7", "H16"]
    },
    # R4: nivel elevado de actividad fisica
    "R4": {
        "si": lambda m: m["factor_actividad"] >= 1.55,
        "entonces": lambda m: {"gasto_adicional": True},
        "hechos_soporte": ["H1", "H8", "H16"]
    },
    # R5: habitos alimenticios poco saludables
    "R5": {
        "si": lambda m: m.get("habitos_inadecuados", False),
        "entonces": lambda m: {"mejorar_habitos": True},
        "hechos_soporte": ["H2", "H6", "H10", "H15"]
    },
    # R6: consumo elevado de azucar
    "R6": {
        "si": lambda m: m.get("alto_consumo_azucar", False),
        "entonces": lambda m: {"reducir_azucar": True},
        "hechos_soporte": ["H4", "H10", "H15"]
    },
    # R7: preservacion muscular durante la perdida de peso
    "R7": {
        "si": lambda m: m["objetivo"] == "bajar_peso" and m.get("preservar_musculo", True) and "proteina_g_kg" in m,
            "entonces": lambda m: {"proteina_g_kg": 2.2},
            "hechos_soporte": ["H5", "H7", "H11"]
    },
    # R8: recomendaciones generales para el mantenimiento
    "R8": {
        "si": lambda m: m.get("objetivo") == "mantenimiento",
        "entonces": lambda m: {
            "recomendacion_estilo_vida": "Mantener actividad física regular, incluir ejercicios de fortalecimiento muscular y procurar una alimentación equilibrada.",
            "mensaje": "Se busca fomentar hábitos saludables y sostenibles a largo plazo."
        },
        "hechos_soporte": ["H2", "H13", "H14"]
    },
    # R9: distribucion de grasas
    "R9": {
        "si": lambda m: "calorias_objetivo" in m,
        "entonces": lambda m: {
            "grasas_g": m["calorias_objetivo"] * 0.25 / 9
        },
        "hechos_soporte": ["H7", "H10"]
    },
    # R10: distribucion de carbohidratos
    "R10": {
        "si": lambda m: "proteina_g" in m and "grasas_g" in m,
        "entonces": lambda m: {
            "carbos_g": (m["calorias_objetivo"] - 4 * m["proteina_g"] - 9 * m["grasas_g"]) / 4
        },
        "hechos_soporte": ["H7"]
    },
    # R11: calculo de la tasa metabolica basal 
    "R11": {
        "si": lambda m: "peso" in m and "estatura" in m,
        "entonces": lambda m: {
            "tmb": 10*m["peso"] + 6.25*m["estatura"] - 5*m["edad"] + (5 if m["sexo"] == "M" else -161)
        },
        "hechos_soporte": ["H8"]
    },
    # R12: calculo del gasto energetico total 
    "R12": {
        "si": lambda m: "tmb" in m,
        "entonces": lambda m: {
            "get": m["tmb"] * m["factor_actividad"]
        },
        "hechos_soporte": ["H16"]
    },
    # R13: calculo de las calorias objetivo 
    "R13": {
        "si": lambda m: "get" in m and "factor_calorias" in m,
        "entonces": lambda m: {
            "calorias_objetivo": m["get"] + m["factor_calorias"]
        },
        "hechos_soporte": ["H7", "H12"]
    },
    # R14: calculo de los gramos de proteina
    "R14": {
        "si": lambda m: "calorias_objetivo" in m and "proteina_g_kg" in m,
        "entonces": lambda m: {
            "proteina_g": m["proteina_g_kg"] * m["peso"]
        },
        "hechos_soporte": ["H5", "H11"]
    },
    # R15: porcentaje de carbohidratos 
    "R15": {
        "si": lambda m: "carbos_g" in m,
        "entonces": lambda m: {
            "pct_carbos": round(m["carbos_g"] * 4 / m["calorias_objetivo"] * 100, 1),
            "conclusion": "Dieta inicial generada"
        },
        "hechos_soporte": ["H7", "H2"]
    },
}


def motor_inferencia(caso):
    datos = dict(caso) 
    reglas = set() 
    traza = [] 
    ciclo = 0 
    nuevo = True
    
    while nuevo:
        nuevo = False
        ciclo += 1
        for id_r, regla in REGLAS.items():
            if id_r in reglas:
                continue
            if regla["si"](datos): 
                derivados = regla["entonces"](datos) 
                datos.update(derivados) 
                reglas.add(id_r)
                traza.append((ciclo, id_r, derivados, regla["hechos_soporte"])) 
                nuevo = True 
                
    return datos, traza # devuelve el resultado

# intervalos para los datos numericos
INTERVALOS = {
    "edad":     (18, 65, "años"),
    "peso":     (30, 250, "kg"),
    "estatura": (120, 230, "cm"),
}

OPCIONES_SEXO = {
    "1": ("M", "Masculino"),
    "2": ("F", "Femenino"),
}

OPCIONES_OBJETIVO = {
    "1": ("bajar_peso", "Bajar de peso"),
    "2": ("ganar_musculo", "Ganar masa muscular"),
    "3": ("mantenimiento", "Mantener el peso"),
}

OPCIONES_ACTIVIDAD = {
    "1": (1.2,   "Sedentario (poco o nada de ejercicio)"),
    "2": (1.375, "Ligera (1-3 días por semana)"),
    "3": (1.55,  "Moderada (3-5 días por semana)"),
    "4": (1.725, "Intensa (6-7 días por semana)"),
    "5": (1.9,   "Muy intensa (entrenamiento doble o trabajo físico pesado)"),
}


def pedir_numero(nombre):
    """Pide un numero y lo repite hasta que este dentro del intervalo."""
    minimo, maximo, unidad = INTERVALOS[nombre]
    while True:
        texto = input(f"{nombre.capitalize()} ({minimo}-{maximo} {unidad}): ").strip()
        try:
            valor = float(texto)
        except ValueError:
            print("  Escribe un número válido.")
            continue
        if minimo <= valor <= maximo:
            return int(valor) if valor.is_integer() else valor
        print(f"  El valor debe estar entre {minimo} y {maximo} {unidad}.")


def pedir_opcion(titulo, opciones):
    """Muestra un menu y regresa el valor interno de la opcion elegida."""
    print(f"\n{titulo}")
    for clave, (_, texto) in opciones.items():
        print(f"  {clave}) {texto}")
    while True:
        eleccion = input("Elige una opción: ").strip()
        if eleccion in opciones:
            return opciones[eleccion][0]
        print(f"  Opción inválida. Elige entre {', '.join(opciones)}.")


def pedir_si_no(pregunta):
    """Pregunta de si/no. Regresa True o False."""
    while True:
        r = input(f"{pregunta} (s/n): ").strip().lower()
        if r in ("s", "si", "sí"):
            return True
        if r in ("n", "no"):
            return False
        print("  Responde con 's' o 'n'.")


def capturar_caso():
    print("=== Datos del caso ===")
    caso = {
        "edad": pedir_numero("edad"),
        "peso": pedir_numero("peso"),
        "estatura": pedir_numero("estatura"),
    }
    caso["sexo"] = pedir_opcion("Sexo:", OPCIONES_SEXO)
    caso["factor_actividad"] = pedir_opcion("Nivel de actividad física:", OPCIONES_ACTIVIDAD)
    caso["objetivo"] = pedir_opcion("Objetivo:", OPCIONES_OBJETIVO)

    print()
    caso["habitos_inadecuados"] = pedir_si_no("¿Tienes hábitos alimenticios poco saludables?")
    caso["alto_consumo_azucar"] = pedir_si_no("¿Consumes azúcar en exceso?")
    if caso["objetivo"] == "bajar_peso":
        caso["preservar_musculo"] = pedir_si_no("¿Quieres preservar tu masa muscular?")
    return caso


if __name__ == "__main__":
    caso = capturar_caso()
    datos, traza = motor_inferencia(caso)

    print("\n Proceso de inferencia ")
    for ciclo, id_r, derivados, soporte in traza:
        print(f"Ciclo {ciclo} {id_r} = {derivados}\n  Respaldo: {soporte}\n")
    print(datos["conclusion"], round(datos["calorias_objetivo"]), "kcal")