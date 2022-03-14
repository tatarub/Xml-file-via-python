import xml.etree.ElementTree as ET
import lxml.etree as etree 
  
def GenerateXML(fileName) :
      
    root = ET.Element("List")
    l1 = ET.Element("movies")
    root.append(l1)
      
    m1 = ET.SubElement(l1, "Name")
    m1.text = "The Godfather"
    m1 = ET.SubElement(l1, "Year")
    m1.text = "1972"
    m1 = ET.SubElement(l1, "Genre")
    m1.text = "Crime"
        
    m2 = ET.SubElement(l1, "Name")
    m2.text = "The Dark Knight"
    m2 = ET.SubElement(l1, "Year")
    m2.text = "2008"
    m2 = ET.SubElement(l1, "Genre")
    m2.text = "Action"

    m3 = ET.SubElement(l1, "Name")
    m3.text = "Inception"
    m3 = ET.SubElement(l1, "Year")
    m3.text = "2010"
    m3 = ET.SubElement(l1, "Genre")
    m3.text = "Sci-Fi" 
    tree = ET.ElementTree(root)
      
    with open (fileName, "wb") as files:
        tree.write(files)
        
if __name__ == "__main__": 
    GenerateXML("List.xml")
    x = etree.parse("List.xml")
    print(etree.tostring(x, pretty_print=True, encoding="unicode", method='xml'))    
    

