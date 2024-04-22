def norma(x, y, z):
    """Recibe un vector en R3 y devuelve su norma"""
    return (x**2 + y**2 + z**2) ** 0.5

def diferencia(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    dif_x = x1 - x2
    dif_y = y1 - y2
    dif_z = z1 - z2
    return dif_x, dif_y, dif_z

def producto_vectorial(componente_x_1vector, componente_y_1vector, componente_z_1vector, componente_x_2vector, componente_y_2vector, componente_z_2vector):
    """Recibe las coordenadas de dos vectores en R3 y devuelve el producto vectorial"""
    componente_final_x = componente_y_1vector * componente_z_2vector - componente_z_1vector * componente_y_2vector
    componente_final_y = componente_z_1vector * componente_x_2vector - componente_x_1vector * componente_z_2vector
    componente_final_z = componente_x_1vector * componente_y_2vector - componente_y_1vector * componente_x_2vector
    return componente_final_x, componente_final_y, componente_final_z