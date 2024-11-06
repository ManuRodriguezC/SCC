from .formatNumber import formatNumber
from reportlab.pdfgen import canvas
import datetime
import io


def createPdf(datos):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    
    # p.drawImage("http://127.0.0.1:6001/static/images/logo_cootratiempo.jpg", 30, 730, width=60, height=80)
    p.setFont("Helvetica-Bold", 25)
    p.setFillColorRGB(0.196, 0.333, 0.627)
    p.drawString(85, 760, "Simulación de Credito Cootratiempo")
        
    p.roundRect(360, 700, width=150, height=30, radius=10)
    p.setFont("Helvetica-Bold", 10)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(380, 718, "Fecha:")
    p.drawString(380, 705, str(datetime.datetime.now()).split(".")[0])
    
    p.setFont("Helvetica-Bold", 18)
    p.setFillColorRGB(0.196, 0.333, 0.627)
    p.drawString(200, 665, "Información Asociado")
    
    p.roundRect(90, 555, width=420, height=105, radius=10)
    p.setFont("Helvetica", 12)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(125, 640, "Nombre Asociado")
    p.drawString(350, 640, datos['datas']['data']['name'])
    p.drawString(125, 625, "Apellido Asociado")
    p.drawString(350, 625, datos['datas']['data']['lastname'])
    p.drawString(125, 610, "Documento Asociado")
    p.drawString(350, 610, datos['datas']['data']['document'])
    p.drawString(125, 595, "Salario")
    p.drawString(350, 595, f"$ {datos['datas']['data']['salario']}")
    p.drawString(125, 580, "Otros Ingresos")
    p.drawString(350, 580, f"$ {datos['datas']['data']['others']}")
    p.drawString(125, 565, "Debitos")
    p.drawString(350, 565, f"$ {datos['datas']['data']['debit']}")

    p.setFont("Helvetica-Bold", 18)
    p.setFillColorRGB(0.196, 0.333, 0.627)
    p.drawString(200, 524, "Datos de la Solicitud")
    
    p.setFont("Helvetica", 12)
    p.setFillColorRGB(0, 0, 0)
    p.roundRect(90, 410, width=420, height=110, radius=10)
    p.drawString(125, 505, "Tipo de Credito")
    p.drawString(350, 505, str(datos['datas']['type']))
    p.drawString(125, 490, "Monto a Solicitar")
    p.drawString(350, 490, f"$ {str(datos['datas']['monto'])}")
    p.drawString(125, 475, "Numero de cuotas")
    p.drawString(350, 475, str(datos['datas']['cuotas']))
    p.drawString(125, 460, "Tasa Nominal Anual")
    p.drawString(350, 460, f"{str(datos['datas']['tasaAnual'])} %")
    p.drawString(125, 445, "Tasa Nominal Mensual")
    p.drawString(350, 445, f"{str(datos['datas']['tasaMensual'])} %")
    p.drawString(125, 430, "Score")
    p.drawString(350, 430, f"{str(datos['datas']['score'])}")
    p.drawString(125, 415, "Score Interno")
    p.drawString(350, 415, f"{str(datos['datas']['scoreInterno'])}")
    
    
    p.setFont("Helvetica-Bold", 18)
    p.setFillColorRGB(0.196, 0.333, 0.627)
    p.drawString(190, 375, "Datos de la Simulación")
    
    p.setFont("Helvetica", 12)
    p.setFillColorRGB(0, 0, 0)
    p.roundRect(90, 290, width=420, height=80, radius=10)
    p.drawString(125, 355, "Aporte seguridad social")
    p.drawString(350, 355, f"$ {formatNumber(str(datos['datas']['seguridad']))}")
    p.drawString(125, 340, "Ingresos Totales")
    p.drawString(350, 340, f"$ {formatNumber(str(datos['datas']['totales']))}")
    p.drawString(125, 325, "Valor de cuota")
    p.drawString(350, 325, f"$ {formatNumber(str(datos['datas']['cuota']))}")
    p.drawString(125, 310, "Descuento Maximo")
    p.drawString(350, 310, f"$ {formatNumber(str(datos['datas']['capacidad']))}")
    p.drawString(125, 295, "Monto Maximos a Solicitar")
    p.drawString(350, 295, f"$ {formatNumber(str(datos['datas']['montomaximo']))}")
    
    p.setFont("Helvetica-Bold", 13)
    p.drawString(70, 270, "Requisitos:")
    p.setFont("Helvetica", 8)
    
    text = datos['datas']['requisitos']
    splitText = text.split(" ")
    numberLetter = 0
    listParagraph = []
    paragraph = ""
    for word in splitText:
        paragraph += word + " "
        numberLetter += len(word)
        if numberLetter > 90:
            listParagraph.append(paragraph)
            paragraph = ""
            numberLetter = 0
    if paragraph != "":
        listParagraph.append(paragraph)
    
    pos = 255
    for parag in listParagraph:
        p.drawString(70, pos, parag)
        pos -= 8

    p.setFont("Helvetica-Bold", 13)
    posTitle = pos - 15
    p.drawString(70, posTitle, "Garantias:")
    p.setFont("Helvetica", 8)
    
    text = datos['datas']['garantias']
    splitText = text.split(" ")
    numberLetter = 0
    listParagraph = []
    paragraph = ""
    for word in splitText:
        paragraph += word + " "
        numberLetter += len(word)
        if numberLetter > 90:
            listParagraph.append(paragraph)
            paragraph = ""
            numberLetter = 0
    if paragraph != "":
        listParagraph.append(paragraph)
    
    pos = posTitle - 15
    for parag in listParagraph:
        p.drawString(70, pos, parag)
        pos -= 8
    
    p.setFont("Helvetica-Bold", 12)
    p.drawString(40, pos - 20, "Puntos para tener en cuenta")
    
    pos -= 20
    
    condiciones = """1. Esta simulación es de carácter informativa. Los valores reales dependerán de las tasas de interés y las políticas establecidas por COOTRATIEMPO al momento del desembolso. 2. El cupo de crédito no sólo se establece por los aportes sociales, ahorros o garantía que nos ofreces, igualmente el estudio del perfil y tu capacidad de pago es definitivo. 3. El estudio de crédito se realizará una vez entregues y diligencies la totalidad de documentos requeridos para el trámite, los cuales te serán informados por tu asesor. 4. Los valores de la simulación no incluyen la cuota de seguro, estos valores pueden tener variaciones en el tiempo."""
    splitText = condiciones.split(" ")
    numberLetter = 0
    listParagraph = []
    paragraph = ""
    for word in splitText:
        paragraph += word + " "
        numberLetter += len(word)
        if numberLetter > 125:
            listParagraph.append(paragraph)
            paragraph = ""
            numberLetter = 0
    if paragraph != "":
        listParagraph.append(paragraph)
    
    pos -= 8
    p.setFont("Helvetica-Oblique", 7)
    for parag in listParagraph:
        p.drawString(40, pos , parag)
        pos -= 8

    p.setFont("Helvetica-Bold", 12)
    p.drawString(40, pos - 14, "Autorización consulta y reportes en Centrales de Riesgo")
    
    pos -= 14
    condiciones = """Autorizo en nombre propio y en mi calidad de representante legal a COOTRATIEMPO Cooperativa Financiera o a quien represente sus derechos, a consultar, reportar y tratar ante centrales de riesgo crediticio lo referente a mi comportamiento financiero y el de la entidad que represento, y en especial reportar el nacimiento, modificación, extinción de obligaciones contraídas o que llegare a contraer con COOTRATIEMPO, los saldos que a su favor resulten de todas las operaciones de crédito, financieras, comercial y/o de servicios, que bajo cualquier modalidad me hubiese otorgado o me otorgue en el futuro; esto implica que mi información financiera, crediticia, comercial y/o de servicios reportada permanecerá en tales centrales de crédito durante el tiempo que la misma ley establezca, de acuerdo con el momento y las condiciones en que se efectúe el pago de las obligaciones."""
    splitText = condiciones.split(" ")
    numberLetter = 0
    listParagraph = []
    paragraph = ""
    for word in splitText:
        paragraph += word + " "
        numberLetter += len(word)
        if numberLetter > 135:
            listParagraph.append(paragraph)
            paragraph = ""
            numberLetter = 0
    if paragraph != "":
        listParagraph.append(paragraph)
    
    pos -= 8
    p.setFont("Helvetica-Oblique", 7)
    for parag in listParagraph:
        p.drawString(40, pos , parag)
        pos -= 8
    
    p.showPage()
    
    # Segunda página (aquí puedes agregar el contenido de la segunda página)
    p.setFont("Helvetica-Bold", 13)
    p.setFillColorRGB(0.196, 0.333, 0.627)
    p.drawString(200, 760, "DECLARACIÓN ORIGEN DE FONDOS")
    
    p.setFont("Helvetica", 11)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(70, 720, "De manera  voluntaria y dando  certeza de  que  todo lo  que está aquí  consignado es cierto")
    p.drawString(70, 707, "y aplicable, frente al origen de fondos y destino a COOTRATIEMPO, con el propósito de que")
    p.drawString(70, 694, "se pueda dar cumplimiento a lo  señalado  en  la Circular Básica Jurídica vigente emitida por ")
    p.drawString(70, 681, "la Superintendencia de la Economía  Solidaria capítulo XI, el Estatuto Orgánico del  Sistema")
    p.drawString(70, 668, "Financiero   (Decreto 663  de  1993),   ley   190    de   1995  ( Estatuto  Anticorrupción )  y de")
    p.drawString(70, 655, "conformidad con las Leyes Colombianas, así como Normas Internacionales, declaro: a. Que")
    p.drawString(70, 642, "el  origen de  los dineros  depositados  como  aportes  y  demás  operaciones  que  tramito a ")
    p.drawString(70, 629, "través de la  Cooperativa, provienen  de las  fuentes indicadas  en el campo  señalado como")
    p.drawString(70, 616, 'como  "Ocupación”   del   presente   formulario.   b.  Declaro  que   los   recursos   que  estoy')
    p.drawString(70, 603, "entregando  no  proviene  de   ninguna  actividad ilícita,  de las   contempladas en el  Código ")
    p.drawString(70, 590, "Penal  Colombiano. c. No admitiré que terceros efectúen  aportes a  mis cuentas con fondos")
    p.drawString(70, 577, "ilícitos  ni  efectúen  transacciones  destinadas  a tales  actividades,  o  a favor  de  personas")
    p.drawString(70, 564, "relacionadas  con las mismas. d. Eximo a COOTRATIEMPO de toda responsabilidad que se")
    p.drawString(70, 551, "derive  por  información  errónea, falsa  o  inexacta  que  yo hubiera  proporcionado y ratifico")
    p.drawString(70, 538, "que  cualquier  falsedad,  inexactitud  o error  en  la  información suministrad, así como en el")
    p.drawString(70, 525, "incumplimiento  a cualquiera  de  mis   obligaciones   de  conformidad  con  este  documento,")
    p.drawString(70, 512, "dará  derecho  a  COOTRATIEMPO  a   terminar   unilateralmente,  y  sin  que  haya  lugar a")
    p.drawString(70, 499, "indemnización  alguna  a  mi  favor   todos   los   contratos   que   haya  celebrado  con dicha")
    p.drawString(70, 486, "entidad.  e.  De acuerdo con  lo   anterior  como  consecuencia  de  la  terminación  unilateral")
    p.drawString(70, 473, "anteriormente señalada, autorizo a COOTRATIEMPO a saldar cualquier aporte, y/o cualquier")
    p.drawString(70, 460, "otro   producto  contratado.  f.   Informaré  inmediatamente  de   cualquier  circunstancia  que")
    p.drawString(70, 447, "modifique  la  presente declaración. g. Toda  la información suministrada en este documento")
    p.drawString(70, 434, "es cierta.")
    
    p.setFont("Helvetica-Bold", 11)
    p.setFillColorRGB(0.196, 0.333, 0.627)
    p.drawString(70, 400, "AUTORIZACIÓN DE CONSULTA Y REPORTE A OPERADORES DE BASES DE DATOS")
    
    p.setFont("Helvetica", 11)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(70, 375, "Autorizo de manera irrevocable a COOTRATIEMPO a reportar, divulgar y procesar, ante las")
    p.drawString(70, 362, "Centrales  de  Riesgos  y/o  cualquier entidad  en Colombia o  en el  exterior que administra")
    p.drawString(70, 349, "bases  de  datos  con  fines análogos a los  de esta última toda la  información relacionadas")
    p.drawString(70, 336, "con  las   obligaciones   que   he   contraído   con  COOTRATIEMPO  y  específicamente  el")
    p.drawString(70, 323, "incumplimiento  y/o  mora  de   las  obligaciones   contraídas,  solicitar,  consultar  con  fines")
    p.drawString(70, 310, "estadísticos  de  control, de supervisión y  de información  comercial,  toda   mi  información")
    p.drawString(70, 297, "financiera    y    comercial,    en    general    y   especialmente   la   información   relativa   al")
    p.drawString(70, 284, "incumplimiento y/o  mora de obligaciones  que se  encuentre disponible en  la y/o  cualquier")
    p.drawString(70, 271, "otra base de datos de la misma naturaleza en Colombia o en el exterior consultar y verificar")
    p.drawString(70, 258, "con terceros toda  la información  que he  suministrado a  Cootratiempo,  lo cual incluye, sin")
    p.drawString(70, 245, "limitarse  a  referencias  comerciales,   personas   y   laborables,   información   financiera  y")
    p.drawString(70, 232, "derechos reales, suministrar a las Centrales de Información de Riesgo datos relativos a mis")
    p.drawString(70, 219, "solicitudes de crédito así  como  otros atinentes a mis relaciones comerciales, financieras  y")
    p.drawString(70, 206, "en  general  socioeconómicas   que   yo   haya  entregado  o que consten  en  los   registros")
    p.drawString(70, 193, "públicos,  bases  de  datos  públicas  o  documentos  públicos,  reportar a   las   autoridades")
    p.drawString(70, 180, "tributarias, aduaneras o judiciales la información que requieran para cumplir   sus funciones")
    p.drawString(70, 167, "de   controlar   y   velar  el  acatamiento  de   mis   deberes  constitucionales   y  legales. La")
    p.drawString(70, 154, "autorización previa no permite a la COOTRATIEMPO  o la C entral de Riesgos  transmitir la")
    p.drawString(70, 141, "información mencionada  con fines diversos, tales como evaluar los riesgos de concederme")
    p.drawString(70, 129, "un crédito,  verificar por parte de las autoridades  públicas  competentes el cumplimiento de")
    p.drawString(70, 116, "mis  obligaciones constitucionales  y  legales,  y  elaborar   estadísticas  y derivar, mediante")
    p.drawString(70, 103, "modelos  matemáticos,  conclusiones  de  ellas.  Declaro   haber   leído  cuidadosamente el")
    p.drawString(70, 90, "contenido de esta cláusula  y haberla comprendido a cabalidad,  razón por la  cual entiendo")
    p.drawString(70, 77, "sus alcances y sus implicaciones.")
    
    p.showPage()
    
    p.setFont("Helvetica-Bold", 13)
    p.setFillColorRGB(0.196, 0.333, 0.627)
    p.drawString(120, 760, "AUTORIZACIÓN TRATAMIENTO DE DATOS PERSONALES")
    
    p.setFont("Helvetica", 11)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(70, 720, "En cumplimiento de la Ley Estatutaria 1581 de 2012 de Protección de Datos y demás normas")
    p.drawString(70, 707, "concordantes,  con  mi  firma autorizo como  Titular de  mis  datos  personales para que éstos")
    p.drawString(70, 694, "sean incorporados  en una  base de datos  responsabilidad COOTRATIEMPO  para que sean")
    p.drawString(70, 681, "tratados   con   la   finalidad  de   realizar   gestión   administrativa,    verificación  de   datos  y")
    p.drawString(70, 668, "referencias,  gestión  de  cobros  y  pagos,   gestión   de   facturación,  gestión  económica   y")
    p.drawString(70, 655, "contable,  gestión   fiscal,   prospección   comercial,    publicidad   propia,   segmentación   de")
    p.drawString(70, 642, "mercados,  estudios  de  crédito,  transmisión  y/o  transferencia  nacional  e  internacional de")
    p.drawString(70, 629, "datos con  terceros  como  aliados   comerciales,  empleadores del asociado,  compañías  de")
    p.drawString(70, 616, 'seguro,  cajas  de  compensación  y  terceros  que  presten servicios  de cobranza, así como,')
    p.drawString(70, 603, "autorizo  que  mis   datos  biométricos  como  la  voz   sean  utilizados  para la verificación de")
    p.drawString(70, 590, "Penal  Colombiano. c. No admitiré que terceros efectúen   aportes a  mis  cuentas con fondos")
    p.drawString(70, 577, "identidad y aprobación y firma  de   documentos. De  igual manera,  declaro  que  cuento  con")
    p.drawString(70, 564, "la autorización  de  los  terceros  registrados  (cónyuge,  compañero  permanente,  referencia")
    p.drawString(70, 551, "personal y familiar) para proporcionar sus datos a COOTRATIEMPO con el propósito  de que")
    p.drawString(70, 538, "sean  tratados  con  la  finalidad  de  realizar  gestión  administrativa,  gestión   de  asociados,")
    p.drawString(70, 525, "mantener, controlar y  desarrollar  la  relación  y  verificación  de  datos  y   referencias. Es de")
    p.drawString(70, 512, "carácter  facultativo  suministrar información  que verse sobre   Datos   Sensibles, entendidos")
    p.drawString(70, 499, "como aquellos que afectan la  intimidad   o  generen  algún  tipo  de  discriminación,  o  sobre")
    p.drawString(70, 486, "menores  de  edad.  El titular  de los datos podrá  ejercer los derechos de acceso, corrección.")
    p.drawString(70, 473, "supresión, revocación o reclamo por  violación sobre mis datos a través de un escrito dirigido")
    p.drawString(70, 460, "a         COOTRATIEMPO           a         la          dirección          de         correo        electrónico")
    p.drawString(70, 447, "atencionalasociado@cootratiempo.com.co,    indicando en  el  asunto  el  derecho que desea")
    p.drawString(70, 434, "ejercitar, o mediante un correo ordinario remitido a la dirección CALLE 35 No. 14-12, Bogotá,")
    p.drawString(70, 421, "D.C. – Colombia.")

    
    
    # Guardar el documento
    p.save()
    
    buffer.seek(0)
    return buffer