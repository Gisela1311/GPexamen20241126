from http.server import HTTPServer , BaseHTTPRequestHandler
import urllib.parse


class GSLPVRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        '''
        Esta función procesa las solicitudes de tipo GET.

        Funcionalidad: 
        1. Envía una respuesta HTTP 200 (OK). 
        2. Añade una cabecera 'Content-Type' con el valor 'text/html'. 
        3. Finaliza las cabeceras de la respuesta. 
        4. Escribe el contenido HTML en el cuerpo de la respuesta.
        '''
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(html_calc_triangulo, 'utf-8'))

    def do_POST(self):
        '''
        Esta función procesa las solicitudes de tipo POST.

        Funcionalidad: 
        1. Lee la longitud del contenido de la solicitud POST. 
        2. Extrae los datos enviados en la solicitud y los decodifica. 
        3. Obtiene la base y la altura del triángulo de los parámetros de la solicitud. 
        4. Calcula el área del triángulo. 
        5. Envía la respuesta con el área calculada en formato HTML, usando la función area_triangulo.
        '''
        content_length = int(self.headers.get('Content-Length'))
        post_data = self.rfile.read(content_length)
        params = urllib.parse.parse_qs(post_data.decode('utf-8'))
        
            # Extraer la base y la altura
        base = float(params['base'][0])
        altura = float(params['altura'][0])
        print("------- Contenido del request -------")

        # Enivar la respuesta
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(area_triangulo(base, altura), 'utf-8'))


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler, puerto=8000):
    """
    Descripción de la función:
    Sirve para configurar y levantar un servidor en un puerto específico.

    Argumetnos:
    - server_class (type): indica la clase del servidor a usar. 
    - handler_class (type): indica que modelo de gestores de peticionesa se va a usar.  
    - puerto (int): Número del puerto en el cual el servidor escucha las solicitudes entrantes. 
    """

    server_address = ('', puerto)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor levantado en http://localhost:{puerto}")
    httpd.serve_forever()

run(handler_class = GSLPVRequestHandler, puerto=8025)

html_calc_triangulo = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculador de Área de Triángulos</title>
</head>
<body>
    <h1>Calculador de Área de Triángulos</h1>

    <form action="/calcular_area" method="POST"> <label for="base">Base:</label>
        <input type="number" id="base" name="base" required>

        <label for="altura">Altura:</label>
        <input type="number" id="altura" name="altura" required>

        <button type="submit">Calcular</button>
    </form>
</body>
</html>
"""

def area_triangulo(base, altura):
    """
    Descripción de la función usada para calcular el área del triángulo: 

    esta función sirve para devolver el resultado del cálculo matemático.     

    Retorna:
    - el html con un texto que explica la operación y el resultado de la misma. 
    """

    resultado = base * altura
    
    html_area= f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculador de Área de Triángulos</title>
    </head>
    <body>
        <h1>Calculador de Área de Triángulos</h1>

        <h3>El área de un triángulo de base {base} y altura {altura} es: {resultado}</h3>
    </body>
    </html>
    """
    return html_area