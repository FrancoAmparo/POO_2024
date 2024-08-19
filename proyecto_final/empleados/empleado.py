class Empleado:
    def __init__(self, trabajador_id, nombre, edad, horas_trabajadas, sueldo_dia, prima_dominical, tipo_jornada, dias_trabajados, horas_extra, descanso_semanal):
        self.trabajador_id = trabajador_id
        self.nombre = nombre
        self.edad = edad
        self.horas_trabajadas = horas_trabajadas
        self.sueldo_dia = sueldo_dia
        self.prima_dominical = prima_dominical
        self.tipo_jornada = tipo_jornada
        self.dias_trabajados = dias_trabajados
        self.horas_extra = horas_extra
        self.descanso_semanal = descanso_semanal
        self.salario_base = self.calcular_sueldo_semanal()

    def calcular_sueldo_semanal(self):
        salario_base = (self.sueldo_dia * self.dias_trabajados) + (self.horas_extra * (self.sueldo_dia / 8) * 1.5)

        if self.descanso_semanal and self.prima_dominical:
            salario_base += self.sueldo_dia * 0.25  
        
        return salario_base

    def get_info(self):
        return {
            "trabajador_id": self.trabajador_id,
            "nombre": self.nombre,
            "edad": self.edad,
            "horas_trabajadas": self.horas_trabajadas,
            "sueldo_dia": self.sueldo_dia,
            "prima_dominical": self.prima_dominical,
            "tipo_jornada": self.tipo_jornada,
            "dias_trabajados": self.dias_trabajados,
            "horas_extra": self.horas_extra,
            "descanso_semanal": self.descanso_semanal,
            "salario_base": self.salario_base
        }
