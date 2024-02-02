'''
Crear una funció que retorni un XML (crear arxiu .xml i mostrar per consola l’XML). 
La funció ha de crear l’XML, crear les etiquetes i inserir text segons les següents especificacions:
Un root de nom students.
Cinc childs (del root) amb nom student.
Cada child student ha de tindre 4 subchilds:
 name
 surname
 email
 dni
Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child “student”.
El text de cada etiqueta serà de la vostra elecció.
'''
import xml.etree.ElementTree as ET

def makeXML():
    arrel = ET.Element('students')

    for i in range(5):
        ch = ET.SubElement(arrel, 'student')
        chName = ET.SubElement(ch, 'name')
        chSurname = ET.SubElement(ch, 'surname')
        chEmail = ET.SubElement(ch, 'email')
        chDni = ET.SubElement(ch, 'dni')

        ch.set('type',f'student-{i}')

        chName.text = 'Nombre{}'.format(i)
        chSurname.text = 'Apellido{}'.format(i)
        chEmail.text = 'email{}@example.com'.format(i)
        chDni.text = 'DNI{}'.format(i)
        
        arrel.append(ch)

    print('XML file')

# makeXML()