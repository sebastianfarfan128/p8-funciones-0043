# Sebastian Farfan NC = 0043
# ==============================================================================
# EJERCICIOS DE FUNCIONES EN PYTHON - ASIGNACIÓN MASCULINA
# Referencia 1: elpythonista.com (Ejemplos 1, 2 y 3 de hombres)
# Referencia 2: pythones.net (Listas 1-30 y 31-60 de hombres)
# ==============================================================================

# ------------------------------------------------------------------------------
# PARTE 1: EJEMPLOS DE ELPYTHONISTA.COM (1 AL 3)
# ------------------------------------------------------------------------------

# Ejemplo 1: Función básica de bienvenida
def dar_bienvenida_hombre():
    print("--- Ejemplo 1 ---")
    print("¡Bienvenido al sistema! Registro de usuario iniciado.")

dar_bienvenida_hombre()
print()


# Ejemplo 2: Función con parámetros de posición (Nombre y Rol)
def registrar_usuario_hombre(nombre, rol="Usuario"):
    print("--- Ejemplo 2 ---")
    print(f"Bienvenido, {nombre}. Tu rol asignado es: {rol}.")

registrar_usuario_hombre("Carlos", "Administrador")
print()


# Ejemplo 3: Función con retorno (Devuelve un perfil de usuario)
def crear_perfil_hombre(nombre, edad):
    print("--- Ejemplo 3 ---")
    perfil = {
        "Nombre": nombre,
        "Edad": edad,
        "Genero": "Masculino"
    }
    return perfil

usuario_actual = crear_perfil_hombre("Santiago", 28)
print(f"Perfil generado correctamente: {usuario_actual}")
print("\n" + "="*50 + "\n")


# ------------------------------------------------------------------------------
# PARTE 2: EJEMPLOS DE PYTHONES.NET (LISTAS DE HOMBRES 1-30 Y 31-60)
# ------------------------------------------------------------------------------

# Ejemplo 4: Función que retorna la lista del 1 al 30 de Hombres
def obtener_hombres_1_30():
    print("--- Ejemplo 4 (Pythones.net: 1 al 30) ---")
    hombres_1_30 = [
        "1. Alejandro", "2. Benjamín", "3. Carlos", "4. Daniel", "5. Eduardo",
        "6. Fernando", "7. Gabriel", "8. Héctor", "9. Ignacio", "10. Javier",
        "11. Kevin", "12. Luis", "13. Manuel", "14. Nicolás", "15. Oscar",
        "16. Pablo", "17. Joaquín", "18. Roberto", "19. Santiago", "20. Tomás",
        "21. Ulises", "22. Vicente", "23. William", "24. Xavier", "25. Yair",
        "26. Zacarías", "27. Adrián", "28. Bruno", "29. Diego", "30. Esteban"
    ]
    return hombres_1_30

lista_hombres_bloque1 = obtener_hombres_1_30()
print(f"Total en primer bloque: {len(lista_hombres_bloque1)} hombres.")
print("Muestra (primeros 5):", lista_hombres_bloque1[:5])
print()


# Ejemplo 5: Función que retorna la lista del 31 al 60 de Hombres
def obtener_hombres_31_60():
    print("--- Ejemplo 5 (Pythones.net: 31 al 60) ---")
    hombres_31_60 = [
        "31. Andrés", "32. Bernardo", "33. Cristian", "34. David", "35. Emilio",
        "36. Felipe", "37. Gustavo", "38. Hernán", "39. Iván", "40. José",
        "41. Leonardo", "42. Mauricio", "43. Néstor", "44. Orlando", "45. Pedro",
        "46. Rodrigo", "47. Sergio", "48. Thiago", "49. Uriel", "50. Víctor",
        "51. Walter", "52. Yago", "53. Alan", "54. Boris", "55. Cesar",
        "56. Dario", "57. Enzo", "58. Fabian", "59. Gonzalo", "60. Hugo"
    ]
    return hombres_31_60

lista_hombres_bloque2 = obtener_hombres_31_60()
print(f"Total en segundo bloque: {len(lista_hombres_bloque2)} hombres.")
print("Muestra (primeros 5 del bloque):", lista_hombres_bloque2[:5])
print()

# Demostración opcional: Unir ambas listas asignadas (1 al 60 completos)
lista_total_hombres = lista_hombres_bloque1 + lista_hombres_bloque2
print(f"Lista total masculina completada con {len(lista_total_hombres)} registros.")

print("Elaborado por Sebastian Farfan NC = 0043")