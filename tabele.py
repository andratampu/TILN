import tabula

file="httpdx.doi.org10.1016j.aap.2017.03.016.pdf"

tabula.convert_into(file, "output.csv", output_format="csv", pages=[3,4,5])