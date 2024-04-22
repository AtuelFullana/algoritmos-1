import vectores

def area_triangulo(punto1_x, punto1_y, punto1_z, punto2_x, punto2_y, punto2_z, punto3_x, punto3_y, punto3_z):
    """Recibe las coordenadas de tres puntos en R3 y devuelve el area del triangulo"""
    vector1_x,vector1_y,vector1_z = vectores.diferencia(punto1_x, punto1_y, punto1_z, punto2_x, punto2_y, punto2_z)
    vector2_x,vector2_y,vector2_z = vectores.diferencia(punto3_x, punto3_y, punto3_z, punto2_x, punto2_y, punto2_z)
    producto_vectorial_en_x, producto_vectorial_en_y, producto_vectorial_en_z = vectores.producto_vectorial(vector1_x,vector1_y,vector1_z, vector2_x,vector2_y,vector2_z)
    resultado_norma = vectores.norma(producto_vectorial_en_x, producto_vectorial_en_y, producto_vectorial_en_z)
    area_final_del_triangulo = resultado_norma / 2
    return area_final_del_triangulo

assert area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0) == 19.45507645834372
assert area_triangulo(-2,0,2,-5,2,0,6,-3,7) == 4.06201920231798
assert area_triangulo(0,0,-3,4,2,0,3,3,1) == 4.636809247747852