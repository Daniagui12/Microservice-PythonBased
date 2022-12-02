from solicitud.models import Solicitud
from empleado.models import Empleado
from empresaAfiliada.models import EmpresaAfiliada
import os 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Sprint2/static/media/json/keyCredentials.json"

import io

from google.cloud import vision_v1

def detect_text(file_path):
    """Perform batch file annotation."""
    client = vision_v1.ImageAnnotatorClient()

    # Supported mime_type: application/pdf, image/tiff, image/gif
    mime_type = "application/pdf"
    with io.open(file_path, "rb") as f:
        content = f.read()
    input_config = {"mime_type": mime_type, "content": content}
    features = [{"type_": vision_v1.Feature.Type.DOCUMENT_TEXT_DETECTION}]

    # The service can process up to 5 pages per document file. Here we specify
    # the first, second, and last page of the document to be processed.
    pages = [1, 2]
    requests = [{"input_config": input_config, "features": features, "pages": pages}]

    confidence = 0
    cont = 0
    response = client.batch_annotate_files(requests=requests)
    for image_response in response.responses[0].responses:
        print(u"Full text: {}".format(image_response.full_text_annotation.text))
        for page in image_response.full_text_annotation.pages:
            for block in page.blocks:
                print(u"\nBlock confidence: {}".format(block.confidence))
                for par in block.paragraphs:
                    print(u"\tParagraph confidence: {}".format(par.confidence))
                    for word in par.words:
                        confidence += word.confidence
                        cont += 1
                        print(u"\t\tWord confidence: {}".format(word.confidence))
                        for symbol in word.symbols:
                            print(
                                u"\t\t\tSymbol: {}, (confidence: {})".format(
                                    symbol.text, symbol.confidence
                                )
                            )
    return confidence/cont

def get_solicitudes():
    queryset = Solicitud.objects.values()
    return queryset

def filter_solicitudes_by_id_cliente(id_cliente):
    queryset = Solicitud.objects.filter(id_cliente=id_cliente)
    return (queryset)

def create_solicitud(form):
    solicitud = form.save()
    solicitud.save()
    return ()

def get_solicitudes_clientes_empresa(id_empresa):
    querysetEmpresa = EmpresaAfiliada.objects.get(NIT=id_empresa)
    querysetEmpleado = Empleado.objects.filter(empresaAfiliada=querysetEmpresa).values_list('id', flat=True)
    queryset = Solicitud.objects.filter(id_cliente_id__in = querysetEmpleado).values()
    return (queryset)

def update_solicitud(form, id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    solicitud.id_cliente = form.cleaned_data['id_cliente']
    solicitud.fechaCreacion = form.cleaned_data['fechaCreacion']
    solicitud.estado = form.cleaned_data['estado']
    solicitud.documentoCliente = form.cleaned_data['documentoCliente']
    solicitud.save()
    return ()

def delete_solicitud(id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    solicitud.delete()
    return ()

def get_solicitud_by_id(id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    return (solicitud)

def get_solicitud_by_id_cliente(id_cliente):
    solicitud = Solicitud.objects.get(id_cliente=id_cliente)
    return (solicitud)

def get_solicitud_by_fechaCreacion(fechaCreacion):
    solicitud = Solicitud.objects.get(fechaCreacion=fechaCreacion)
    return (solicitud)

def get_solicitud_by_estado(estado):
    solicitud = Solicitud.objects.get(estado=estado)
    return (solicitud)

