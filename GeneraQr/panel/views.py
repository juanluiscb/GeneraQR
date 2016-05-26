from django.shortcuts import render_to_response
from panel.models import Lista
import qrcode

def CreaQr ( qrData ) :
  # print qrData
  if qrData :
    img = qrcode.make ( "Folio: %s \nNombre: %s - %s" % ( qrData.id,qrData.nombre, qrData.curso ) )
    f = open ( "/var/www/static_files/qr/qr_" + str ( qrData.id ) + ".png" , "wb" )
    img.save ( f )
    f.close ( )

def GeneraQr(request):
  lista = Lista.objects.all()
  title = ':: Generando QR'

  for dato in lista:
    CreaQr(dato)

  contexto = {
    'title': title,
    'lista': lista
  }

  return render_to_response('base.html',contexto)